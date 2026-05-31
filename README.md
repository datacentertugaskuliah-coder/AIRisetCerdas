# ALAS v8.8 — Asisten Riset Akademik

(c) 2024-2026 **Alhumaira Store** · obrolanpintar1987@gmail.com

Penyusun *prompt* akademik untuk peneliti Indonesia, dari skripsi dan tesis
hingga hibah BIMA dan BRIN. Pilih bidang, jenjang, dan modul; salin ke asisten
AI pilihan Anda. Core Layer bekerja di balik layar.

## Apa yang baru di v8.8 — Modul 14: Proposal Tesis (S2)

Modul baru untuk menyusun draf proposal/laporan tesis S2, melanjutkan Modul 0-7
lalu memakai sumber Modul 8 (rencana dataset) atau Modul 9 (rancangan analisis).
Modul 14 sengaja DIBEDAKAN dari Modul 13 (skripsi S1) melalui pembeda jenjang:

- **Kerangka konseptual dan hipotesis/proposisi:** Bab 2 tidak berhenti pada
  uraian teori, tetapi mensintesisnya menjadi kerangka konseptual dan hipotesis
  (kuantitatif) atau proposisi (kualitatif).
- **Posisi kebaruan:** Bab 1-2 menegaskan kebaruan terhadap penelitian terdahulu.
- **Metodologi tingkat S2:** justifikasi pemilihan metode, definisi operasional,
  dan rigor yang lebih ketat; tetap bercabang bidang dan jenis penelitian.
- **Kontribusi teoretis ditonjolkan:** manfaat memisahkan kontribusi teoretis
  (utama) dan praktis.
- **Rujukan lebih internasional:** Bab 2 memakai 80% jurnal internasional
  bereputasi (Scopus Q2/Q3/Q4/IEEE) dan 20% SINTA 1-2, utamakan open access,
  mutakhir 5-10 tahun, dominan sumber primer.

Dua tahap (seperti Modul 13): Tahap 1 Seminar Proposal (Bab 1-3), Tahap 2
Seminar Hasil (Bab 1-5). Bab 4-5 berupa kerangka bertanda anti-fabrikasi.
Tiap bab ditulis di kanvas/dokumen terpisah. Selektor bidang ilmu tersedia
langsung di halaman Modul 14 dengan pembaruan tampilan secara langsung.

## Integritas

- Angka hasil tidak dikarang; ditandai "[isi dari hasil penelitian Anda]".
- Standar khas kampus ditandai "[sesuaikan panduan kampus]".
- DOI, tautan, peringkat SINTA, dan status open access tidak dikarang; yang ragu
  ditandai "[DOI perlu verifikasi di doi.org]".
- Gerbang kelengkapan dan mutu rujukan adalah alat bantu, BUKAN jaminan lulus.
- Firewall Integritas (Seksi K), anti-halusinasi (Seksi E), pengungkapan AI
  (Seksi O.2), dan Seksi P (Gaya Natural) tetap berlaku penuh.

## Daftar modul (16 total)

Core Layer, lalu Modul 0-14: pencarian literatur, intake, kontradiksi, rantai
sitasi, kesenjangan, audit metodologi, rekomendasi judul, hibah dan publikasi,
rekomendasi dataset (8), statistik multivariat (9), draf artikel IMRAD (10),
proposal hibah BIMA (11), proposal BRIN RIIM Kompetisi (12), proposal skripsi
S1 (13), dan proposal tesis S2 (14).

## Login berbasis ACCESS_KEY (Streamlit Cloud Secrets Manager)

1. Buka aplikasi di share.streamlit.io.
2. Menu tiga titik -> Settings -> Secrets.
3. Masukkan, lalu Save:

   ACCESS_KEY = "kunci-rahasia-anda"

4. Halaman login akan meminta kunci tersebut.

Untuk uji lokal: salin `.streamlit/secrets.toml.example` menjadi
`.streamlit/secrets.toml`, isi kunci, lalu `streamlit run app.py`.

## Cara menjalankan secara lokal

    pip install -r requirements.txt
    streamlit run app.py

## Deploy ke Streamlit Cloud

Unggah seluruh isi folder ini ke GitHub, lalu deploy `app.py` di
share.streamlit.io.

## Struktur berkas

    ALAS-v8.8/
    |- app.py
    |- dashboard.html
    |- requirements.txt
    |- ANALISIS_REVISI_CORE_LAYER.md
    |- .streamlit/config.toml
    |- .streamlit/secrets.toml.example
    |- .gitignore
    |- .gitattributes
