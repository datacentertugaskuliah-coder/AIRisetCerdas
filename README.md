# ALAS v8.5 — Asisten Riset Akademik

(c) 2024-2026 **Alhumaira Store** · obrolanpintar1987@gmail.com

Penyusun *prompt* akademik untuk peneliti Indonesia, dari skripsi hingga hibah
BIMA dan BRIN. Pilih bidang, jenjang, dan modul; salin ke asisten AI pilihan
Anda. Core Layer bekerja di balik layar.

## Apa yang baru di v8.5 — Modul 13: Proposal Skripsi

Modul baru untuk menyusun draf proposal/laporan skripsi, melanjutkan Modul 0-7
lalu memakai sumber Modul 8 (rencana dataset) atau Modul 9 (rancangan analisis).

- **Dua tahap:** Tahap 1 Seminar Proposal (Bab 1-3), Tahap 2 Seminar Hasil
  (Bab 1-5). Saat Tahap 1 dipilih, kerangka Bab 4-5 tidak dimunculkan.
- **Bab 1 Pendahuluan:** latar belakang, rumusan masalah, batasan, tujuan,
  manfaat, sistematika penulisan.
- **Bab 2 Kajian Pustaka:** heading dan empat sub-heading terstruktur, masing
  masing ditutup lima pertanyaan literatur Bahasa Inggris sebagai bagian naskah,
  sitasi gaya APA.
- **Bab 3 Metodologi:** bercabang bidang (Saintek/Ilmu Komputer dengan flowchart;
  Umum/Sosial-Humaniora) dan bercabang jenis penelitian (Kuantitatif, Kualitatif,
  Pengembangan/R&D).
- **Bab 4-5:** kerangka bertanda "[isi dari hasil penelitian Anda]"; Bab 5
  menyesuaikan jenis (data angka untuk kuantitatif, temuan tematik untuk
  kualitatif).
- **Penjaga koherensi:** rumusan masalah menjadi benang merah (dijawab di Bab 4,
  disimpulkan di Bab 5); konsistensi istilah dari glosarium Modul 1; konsistensi
  sitasi Bab 2 dengan Daftar Pustaka; gerbang kelengkapan per tahap.
- **Kanvas baru per bab:** tiap bab ditulis di kanvas/dokumen terpisah agar tidak
  menabrak batas panjang (warisan protokol v8.4 yang diperkuat).

## Integritas

- Angka hasil tidak dikarang; ditandai "[isi dari hasil penelitian Anda]".
- Standar khas kampus ditandai "[sesuaikan panduan kampus]".
- DOI hanya dari korpus; jika ragu "[DOI perlu verifikasi di doi.org]".
- Gerbang kelengkapan adalah alat bantu, BUKAN jaminan lulus seminar.
- Firewall Integritas (Seksi K), anti-halusinasi (Seksi E), pengungkapan AI
  (Seksi O.2), dan Seksi P (Gaya Natural) tetap berlaku penuh.

## Daftar modul (15 total)

Core Layer, lalu Modul 0-13: pencarian literatur, intake, kontradiksi, rantai
sitasi, kesenjangan, audit metodologi, rekomendasi judul, hibah dan publikasi,
rekomendasi dataset (8), statistik multivariat (9), draf artikel IMRAD (10),
proposal hibah BIMA (11), proposal BRIN RIIM Kompetisi (12), dan proposal
skripsi (13).

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

    ALAS-v8.5/
    |- app.py
    |- dashboard.html
    |- requirements.txt
    |- ANALISIS_REVISI_CORE_LAYER.md
    |- .streamlit/config.toml
    |- .streamlit/secrets.toml.example
    |- .gitignore
    |- .gitattributes
