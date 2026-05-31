# ALAS v8.3 — Asisten Riset Akademik

(c) 2024-2026 **Alhumaira Store** · obrolanpintar1987@gmail.com

Penyusun *prompt* akademik untuk peneliti Indonesia, dari skripsi hingga hibah
BIMA dan BRIN. Pilih bidang, jenjang, dan modul; salin ke asisten AI pilihan
Anda. Core Layer bekerja di balik layar.

## Apa yang baru di v8.3 — Modul 12: Proposal BRIN RIIM Kompetisi

Modul baru untuk menyusun proposal BRIN skema RIIM Kompetisi, melengkapi Modul
11 (BIMA). Melanjutkan Modul 0-7 lalu memakai sumber Modul 8 (rencana dataset)
atau Modul 9 (rancangan analisis).

- **Workflow bertahap.** Modul 12 menarik kesenjangan dari Modul 4 dan korpus
  dari Modul 1, mengonfirmasi *novelty* lebih dulu, lalu menyusun bab secara
  berurutan. Tersedia *fallback* "langsung saja" agar tetap jalan di semua AI.
- **Struktur khas RIIM** (sesuai pedoman BRIN): Kerangka Berpikir dan Nilai
  Strategis, Susunan Tim Periset, Metode (dengan diagram alir algoritma dan
  *novelty*), Luaran dan Indikator Kinerja Riset, TKT (rentang 3-6), Jadwal
  (maksimal 3 tahun), RAB, Uji Silang metode-luaran-anggaran, Daftar Pustaka
  APA, Ringkasan (disusun terakhir), dan Mitigasi Risiko.
- **Metode bercabang per bidang:** Saintek/Ilmu Komputer memakai pengembangan
  model dengan flowchart; Umum/Sosial-Humaniora memakai empat metode populer.
  Novelty: satu untuk 1 tahun, dua untuk multiyear.
- **Tema fokus BRIN** sebagai referensi (pangan, kesehatan, energi, dan lain
  lain); pengguna memilih satu dan menautkan topiknya.
- **Gerbang Kesiapan Administratif:** pengingat eligibilitas (ketua minimal S3,
  rekam jejak sesuai tema, batas keterlibatan proposal, CV tim).

## Integritas

- Semua angka (jumlah kata, dana, RAB, pagu, TKT, masa, peringkat jurnal)
  ditandai "[verifikasi pedoman BRIN — pendanaan-risnov.brin.go.id]".
- DOI hanya dicantumkan dari korpus; jika ragu ditandai
  "[DOI perlu verifikasi di doi.org]".
- Indikator kinerja, pemetaan TKT, dan gerbang administratif adalah alat bantu
  dan pengingat, BUKAN jaminan kelolosan. Keputusan pendanaan tergantung
  kompetisi, kuota, rekam jejak, dan penilaian reviewer BRIN.
- Firewall Integritas (Seksi K), anti-halusinasi (Seksi E), pengungkapan AI
  (Seksi O.2), dan Seksi P (Gaya Natural) tetap berlaku penuh.

## Daftar modul (14 total)

Core Layer, lalu Modul 0-12: pencarian literatur, intake, kontradiksi, rantai
sitasi, kesenjangan, audit metodologi, rekomendasi judul, hibah dan publikasi,
rekomendasi dataset (8), statistik multivariat (9), draf artikel IMRAD (10),
proposal hibah BIMA (11), dan proposal BRIN RIIM Kompetisi (12).

## Login berbasis ACCESS_KEY (Streamlit Cloud Secrets Manager)

1. Buka aplikasi di share.streamlit.io.
2. Menu tiga titik -> **Settings** -> **Secrets**.
3. Masukkan, lalu **Save**:
   ```toml
   ACCESS_KEY = "kunci-rahasia-anda"
   ```
4. Halaman login akan meminta kunci tersebut.

Untuk uji lokal: salin `.streamlit/secrets.toml.example` menjadi
`.streamlit/secrets.toml`, isi kunci, lalu `streamlit run app.py`.

## Cara menjalankan secara lokal

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy ke Streamlit Cloud

Unggah seluruh isi folder ini ke GitHub, lalu deploy `app.py` di
share.streamlit.io.

## Struktur berkas

```
ALAS-v8.3/
├── app.py                          Pembungkus + login ACCESS_KEY
├── dashboard.html                  Antarmuka + Core Layer tersembunyi
├── requirements.txt
├── ANALISIS_REVISI_CORE_LAYER.md   Analisis, pseudocode, rekomendasi
├── .streamlit/config.toml
├── .streamlit/secrets.toml.example
├── .gitignore
└── .gitattributes
```
