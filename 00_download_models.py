"""Download official pretrained weights and tokenizers into model_assets/."""
import os
os.environ['USE_TF'] = '0'
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib
import math
import requests
from transformers import AutoConfig, AutoTokenizer

ROOT = Path(__file__).resolve().parent
MODELS = {'indobert': ('indobenchmark/indobert-base-p1', 'pytorch_model.bin'),
          'xlmr': ('FacebookAI/xlm-roberta-base', 'model.safetensors')}
for name, (repo, filename) in MODELS.items():
    out = ROOT/'model_assets'/name
    out.mkdir(parents=True, exist_ok=True)
    AutoConfig.from_pretrained(repo).save_pretrained(out)
    AutoTokenizer.from_pretrained(repo).save_pretrained(out)
    path = out/filename
    meta = requests.get(f'https://huggingface.co/api/models/{repo}?blobs=true',timeout=30)
    meta.raise_for_status()
    entry = next(x for x in meta.json()['siblings'] if x['rfilename']==filename)
    expected = entry['size']; digest = entry['lfs']['sha256']
    if path.exists():
        sha=hashlib.sha256()
        with path.open('rb') as handle:
            while chunk := handle.read(4*1024*1024): sha.update(chunk)
        if path.stat().st_size != expected or sha.hexdigest() != digest: raise RuntimeError(f'Invalid existing file: {path}')
        print(f'{name}: existing weights SHA-256 verified', flush=True)
        continue
    tmp = path.with_suffix(path.suffix+'.part')
    start = tmp.stat().st_size if tmp.exists() else 0
    if start > expected: raise RuntimeError('Partial file is larger than expected')
    width = math.ceil((expected-start)/8)
    ranges = [(i, min(i+width-1,expected-1)) for i in range(start,expected,width)] if width else []
    def download(bounds):
        first,last=bounds; segment=out/f'{filename}.segment-{first}-{last}'
        if segment.exists() and segment.stat().st_size==last-first+1: return segment
        with requests.get(f'https://huggingface.co/{repo}/resolve/main/{filename}', headers={'Range':f'bytes={first}-{last}'}, stream=True,timeout=(30,120)) as response:
            response.raise_for_status()
            if response.status_code != 206 or not response.headers.get('Content-Range','').startswith(f'bytes {first}-{last}/'):
                raise RuntimeError(f'Invalid range response: {response.status_code} {response.headers.get("Content-Range")}')
            with segment.open('wb') as handle:
                for chunk in response.iter_content(1024*1024):
                    if chunk: handle.write(chunk)
        if segment.stat().st_size!=last-first+1: raise RuntimeError(f'Incomplete segment: {segment}')
        print(f'{name}: segment {first}-{last} selesai',flush=True)
        return segment
    with ThreadPoolExecutor(max_workers=8) as pool: segments=list(pool.map(download,ranges))
    with tmp.open('ab') as output:
        for segment in segments:
            with segment.open('rb') as source:
                while data := source.read(4*1024*1024): output.write(data)
            segment.unlink()
    if tmp.stat().st_size != expected: raise RuntimeError('Incomplete assembled model')
    sha=hashlib.sha256()
    with tmp.open('rb') as handle:
        while chunk := handle.read(4*1024*1024): sha.update(chunk)
    if sha.hexdigest()!=digest: raise RuntimeError('Model SHA-256 mismatch; do not use file')
    tmp.replace(path)
    print(f'{name}: downloaded and SHA-256 verified ({expected} bytes)', flush=True)
