# Daftar Aspek (Pedoman Anotasi)

Dokumen ini mendefinisikan **15 aspek** hasil pemetaan topik BERTopic ke taksonomi **FiQA** (Corporate, Stock, Market, Economy; Maia dkk. 2018; Lengkeek dkk. 2023). Dipakai sebagai acuan saat anotasi sentimen per pasangan (kalimat, aspek).

- Setiap kalimat menerima **satu aspek primer** (dari hasil topic modeling, dapat dikoreksi anotator bila jelas salah).
- Sentimen diberi **per (kalimat, aspek)**: positif / netral / negatif.
- Kalimat yang masuk kategori **Lainnya** (outlier atau topik tak jelas) tidak dianotasi sebagai salah satu dari 15 aspek.
- Daftar aspek ini **dikunci sebelum anotasi dimulai** dan tidak diubah selama proses anotasi berjalan.

Status: **DRAF** (belum dikunci). Definisi dan contoh batas disempurnakan oleh kedua anotator, lalu dikunci.

---

## CORPORATE
Hal-hal internal perusahaan/bank: kinerja, kredit, dividen, manajemen, produk, strategi.

### 1. Kinerja Keuangan & Laba
**Definisi:** Kalimat yang membahas laba, pendapatan, atau kinerja finansial bank secara umum.
**Termasuk:** "Laba bersih BBRI tumbuh 12% secara tahunan."; "Pendapatan bunga bersih meningkat pada kuartal III."
**Tidak termasuk:** kredit/NPL (-> *Kredit & Kualitas Aset*); harga saham (-> *Pergerakan Saham Bank*).

### 2. Kredit & Kualitas Aset
**Definisi:** Penyaluran/pertumbuhan kredit, dana pihak ketiga (DPK), dan kualitas aset (NPL/kredit macet).
**Termasuk:** "Penyaluran kredit BRI tumbuh 8% yoy."; "Rasio NPL Bank Mandiri turun ke 1,2%."
**Tidak termasuk:** laba umum (-> *Kinerja Keuangan & Laba*).

### 3. Dividen & Aksi Korporasi
**Definisi:** Pembagian dividen, jadwal RUPS, buyback, dan aksi korporasi lain.
**Termasuk:** "BMRI membagikan dividen interim Rp66 per saham."; "Perseroan menjadwalkan RUPS pada Mei 2026."
**Tidak termasuk:** laba sebagai sumber dividen bila fokusnya kinerja (-> *Kinerja Keuangan & Laba*).

### 4. Manajemen & Kepemimpinan
**Definisi:** Pengangkatan/penggantian direksi, komisaris, atau sosok pemimpin bank.
**Termasuk:** "Hery ditunjuk sebagai Direktur Utama."; "RUPS menyetujui perombakan jajaran komisaris."
**Tidak termasuk:** pernyataan strategi bisnis oleh manajemen (-> *Strategi & Ekspansi Bisnis*).

### 5. Layanan & Produk
**Definisi:** Produk dan layanan bank: digital banking, kartu, tabungan, rekening, pembayaran.
**Termasuk:** "BNI meluncurkan fitur pembayaran baru di aplikasi."; "Saldo minimum tabungan diturunkan."
**Tidak termasuk:** penyaluran kredit (-> *Kredit & Kualitas Aset*).

### 6. Strategi & Ekspansi Bisnis
**Definisi:** Arah strategi, ekspansi, kemitraan, segmen bisnis (mis. UMKM), termasuk bank syariah.
**Termasuk:** "BRI memperkuat pembiayaan UMKM."; "Bank memperluas layanan syariah."
**Tidak termasuk:** produk ritel spesifik (-> *Layanan & Produk*).

---

## STOCK
Saham dan aksi pasar atas emiten tertentu.

### 7. Pergerakan Saham Bank
**Definisi:** Pergerakan harga/kontribusi saham bank (BBCA/BBRI/BMRI/BBNI) terhadap indeks.
**Termasuk:** "Saham BBCA menjadi pemberat terbesar indeks."; "BBRI memimpin penguatan saham perbankan."
**Tidak termasuk:** aksi beli/jual asing (-> *Aksi Investor Asing*).

### 8. Aksi Investor Asing
**Definisi:** Pembelian/penjualan bersih investor asing (net buy / net sell) atas saham.
**Termasuk:** "Asing mencatat net sell Rp442 miliar di pasar reguler."; "Investor asing memborong saham BBRI."
**Tidak termasuk:** pergerakan indeks agregat (-> *Pergerakan IHSG & Indeks*).

### 9. Saham Spesifik Non-Bank
**Definisi:** Pergerakan saham emiten non-bank yang disebut bersama konteks 4 bank (mis. BUMI, Barito, Amman).
**Termasuk:** "Saham Barito Renewables melonjak."; "BUMI Resources masuk daftar net buy."
**Tidak termasuk:** saham bank (-> *Pergerakan Saham Bank*).

### 10. Valuasi & Kapitalisasi
**Definisi:** Kapitalisasi pasar dan valuasi saham/emiten.
**Termasuk:** "Kapitalisasi pasar kembali ke Rp12.010 triliun."
**Tidak termasuk:** harga saham harian (-> *Pergerakan Saham Bank*).

---

## MARKET
Kondisi pasar/indeks/transaksi secara agregat.

### 11. Pergerakan IHSG & Indeks
**Definisi:** Pergerakan Indeks Harga Saham Gabungan (IHSG) dan level/penutupan indeks domestik.
**Termasuk:** "IHSG ditutup menguat 1,18% ke 7.398."; "Sebanyak 452 saham turun, 262 naik."
**Tidak termasuk:** bursa luar negeri (-> *Bursa Global*).

### 12. Sektor & Transaksi Pasar
**Definisi:** Pergerakan sektoral, nilai transaksi, dan segmen pasar (reguler/negosiasi/tunai).
**Termasuk:** "Sektor teknologi memimpin penguatan."; "Nilai transaksi mencapai Rp12 triliun."
**Tidak termasuk:** IHSG agregat (-> *Pergerakan IHSG & Indeks*).

### 13. Bursa Global
**Definisi:** Pergerakan bursa luar negeri (Wall Street, Asia-Pasifik, Nikkei, Kospi, Dow, Nasdaq).
**Termasuk:** "Nikkei 225 menguat 4,5%."; "Dow Jones ditutup melemah."
**Tidak termasuk:** IHSG/indeks domestik (-> *Pergerakan IHSG & Indeks*).

---

## ECONOMY
Faktor makroekonomi, moneter, dan global.

### 14. Kebijakan Moneter & Nilai Tukar
**Definisi:** Suku bunga (BI, The Fed), inflasi, dan nilai tukar rupiah/dolar; indeks global MSCI.
**Termasuk:** "BI menahan suku bunga di 5,75%."; "Rupiah melemah ke Rp16.800 per dolar AS."
**Tidak termasuk:** pertumbuhan ekonomi umum (-> *Makroekonomi & Faktor Global*).

### 15. Makroekonomi & Faktor Global
**Definisi:** Pertumbuhan ekonomi, perang dagang/tarif, geopolitik, dan harga komoditas (emas, minyak).
**Termasuk:** "Pertumbuhan ekonomi RI diproyeksi 5%."; "Harga minyak naik akibat ketegangan Timur Tengah."
**Tidak termasuk:** suku bunga/nilai tukar (-> *Kebijakan Moneter & Nilai Tukar*).

---

## Lainnya (bukan aspek)
Outlier topik (`-1`) dan topik tak jelas (kutipan percakapan, profil tokoh, pengantar tabel). Tidak dianotasi sebagai salah satu dari 15 aspek; dikeluarkan dari evaluasi per aspek.

---

## Pedoman Sentimen (ringkas)
| Kelas | Aturan |
|---|---|
| Positif | kabar baik / perbaikan bagi aspek |
| Negatif | kabar buruk / penurunan bagi aspek |
| Netral | laporan faktual, tanpa arah jelas, atau sinyal campuran seimbang |

Sentimen dinilai dari sudut pandang ekonomi/pasar terhadap aspek pada kalimat tersebut. Kasus abu-abu dicatat dan dibahas bersama.
