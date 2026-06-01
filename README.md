# ALAS v8.11 — Asisten Riset Akademik

(c) 2024-2026 **Alhumaira Store** · obrolanpintar1987@gmail.com

Penyusun *prompt* akademik untuk peneliti Indonesia, dari skripsi dan tesis
hingga hibah BIMA dan BRIN. Pilih bidang, jenjang, dan modul; salin ke asisten
AI pilihan Anda. Core Layer bekerja di balik layar.

## Apa yang baru di v8.11 — Modul 16: Laporan Penelitian

Jalur luaran baru: menyusun draf LAPORAN penelitian (bukan proposal),
melanjutkan Modul 0-7 lalu memakai sumber Modul 8 atau Modul 9.

- **Struktur 5 bagian** fleksibel: Pendahuluan, Metode, Hasil, Pembahasan,
  Simpulan. Tiap bagian memakai heading dan empat sub-heading, disusun sebagai
  outline sesuai bidang ilmu.
- **Justifikasi dan pertanyaan literatur:** paragraf terakhir tiap heading dan
  sub-heading memuat justifikasi pembahasan, ditutup lima pertanyaan literatur
  Bahasa Inggris sebagai bagian naskah.
- **Data kuantitatif anti-fabrikasi:** kerangka tabel, gambar, dan grafik dengan
  judul dan deskripsi interpretatif; sel angka ditandai
  "[isi data hasil penelitian Anda]". Tidak ada angka, tabel, atau grafik fiktif.
- **Outline bercabang bidang:** Saintek/Ilmu Komputer memakai outline teknis
  eksperimental; Umum/Sosial-Humaniora memakai outline naratif-analitis.
- **Sumber:** 80% jurnal internasional bereputasi (Scopus Q2/Q3/Q4/IEEE) dan 20%
  SINTA 1-2, sitasi APA, anti-fabrikasi DOI.
- Tiap bagian ditulis di kanvas/dokumen terpisah. Selektor bidang ilmu tersedia
  langsung di halaman Modul 16.


## Integritas

- Angka hasil tidak dikarang; ditandai "[isi dari hasil penelitian Anda]".
- Standar khas kampus ditandai "[sesuaikan panduan kampus]".
- DOI, tautan, peringkat SINTA, dan status open access tidak dikarang; yang ragu
  ditandai "[DOI perlu verifikasi di doi.org]".
- Gerbang kelengkapan dan mutu rujukan adalah alat bantu, BUKAN jaminan lulus.
- Firewall Integritas (Seksi K), anti-halusinasi (Seksi E), pengungkapan AI
  (Seksi O.2), dan Seksi P (Gaya Natural) tetap berlaku penuh.

## Daftar modul (18 total)

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

    ALAS-v8.11/
    |- app.py
    |- dashboard.html
    |- requirements.txt
    |- ANALISIS_REVISI_CORE_LAYER.md
    |- .streamlit/config.toml
    |- .streamlit/secrets.toml.example
    |- .gitignore
    |- .gitattributes
