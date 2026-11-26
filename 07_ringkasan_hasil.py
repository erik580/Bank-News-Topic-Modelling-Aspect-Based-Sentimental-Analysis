"""Verify prediction metrics independently and write a compact research report."""
import json
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

ROOT=Path(__file__).resolve().parent
out=ROOT/'results'
summary=json.loads((out/'summary.json').read_text(encoding='utf-8'))
params=json.loads((out/'selected_hyperparameters.json').read_text(encoding='utf-8'))
bootstrap=json.loads((out/'bootstrap_seed_42.json').read_text(encoding='utf-8'))
labels=['negatif','netral','positif']; seeds=range(42,47)
lines=['# Hasil eksperimen ABSA', '', 'Dataset: 3.000 pasangan kalimat–aspek; 0 negatif (837), 1 netral (871), 2 positif (1.292). Kelas terbesar / terkecil = 1,54. Split dilakukan per artikel dan teks identik: train 2.100, validasi 437, test 463. Tidak ada oversampling atau undersampling.', '', 'Kedua model memakai input pasangan kalimat–aspek, tiga epoch maksimal, batch 8, maksimal 192 token, warmup 10%, dan empat kombinasi tuning yang sama. Pilihan hyperparameter dan epoch berdasarkan macro-F1 validasi. Hasil test diringkas sebagai rata-rata dan simpangan baku lima seed.', '', '| Model | LR | Weight decay | Accuracy | Macro precision | Macro recall | Macro F1 |', '|---|---:|---:|---:|---:|---:|---:|']
for model in ['indobert','xlmr']:
    m=summary[model]; par=params[model]
    cell=lambda key:f"{m[key]['mean']:.4f} ± {m[key]['std']:.4f}"
    lines.append(f"| {model} | {par['lr']} | {par['weight_decay']} | {cell('accuracy')} | {cell('macro_precision')} | {cell('macro_recall')} | {cell('macro_f1')} |")
lines += ['', '## Metrik test per kelas', '', 'Rata-rata lima seed; support setiap kelas sama pada semua seed.', '', '| Model | Kelas | Support | Precision | Recall | F1 |', '|---|---|---:|---:|---:|---:|']
for model in ['indobert','xlmr']:
    runs=[]
    for seed in seeds:
        run=out/model/f'seed_{seed}'; result=json.loads((run/'result.json').read_text(encoding='utf-8'))
        pred=pd.read_csv(run/'predictions.csv'); assert len(pred)==463
        y=pred.sentimen; p=pred.prediksi
        for metric,value in [('accuracy',accuracy_score(y,p)),('macro_precision',precision_score(y,p,labels=[0,1,2],average='macro',zero_division=0)),('macro_recall',recall_score(y,p,labels=[0,1,2],average='macro',zero_division=0)),('macro_f1',f1_score(y,p,labels=[0,1,2],average='macro',zero_division=0))]:
            assert abs(result['test'][metric]-value)<1e-10, (model,seed,metric)
        assert np.allclose(pred[['prob_negatif','prob_netral','prob_positif']].sum(axis=1),1,atol=1e-5)
        runs.append(result)
    for label in labels:
        scores=[r['test']['per_class'][label] for r in runs]
        means=[np.mean([s[k] for s in scores]) for k in ['precision','recall','f1']]
        lines.append(f"| {model} | {label} | {scores[0]['support']} | {means[0]:.4f} | {means[1]:.4f} | {means[2]:.4f} |")
    for metric in ['accuracy','macro_precision','macro_recall','macro_f1']:
        vals=[r['test'][metric] for r in runs]
        assert np.isclose(np.mean(vals),summary[model][metric]['mean'])
        assert np.isclose(np.std(vals,ddof=1),summary[model][metric]['std'])
lo,hi=bootstrap['ci95']
lines+=['', '## Interpretasi dan batasan', '', f"Selisih macro-F1 rata-rata test (XLM-R minus IndoBERT) adalah {summary['xlmr']['macro_f1']['mean']-summary['indobert']['macro_f1']['mean']:.4f}. Bootstrap berpasangan berdasarkan artikel (2.000 pengulangan, seed 42 saja) menghasilkan interval 95% untuk IndoBERT minus XLM-R [{lo:.4f}, {hi:.4f}]. Interval ini mencakup nol dan tidak mencakup variasi antar-seed; bukti ini tidak cukup untuk menyatakan satu model unggul secara meyakinkan.", '', 'Berkas prediksi, probabilitas tiga kelas, confusion matrix, dan metrik per aspek tersedia pada direktori masing-masing model dan seed. Verifikasi provenance anotasi manusia dan penyelesaian konflik label sebelum melaporkan hasil sebagai kesimpulan penelitian. Cohen’s kappa tidak dapat dihitung dari satu label final per pasangan. Baseline TF-IDF/logistic regression, baseline artikel, dan ablasi tanpa aspek dalam proposal belum dijalankan.', '']
(out/'laporan_hasil.md').write_text('\n'.join(lines),encoding='utf-8')
print('\n'.join(lines))
