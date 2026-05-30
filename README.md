# ALAS v8.0 — Asisten Riset Akademik

(c) 2024-2026 **Alhumaira Store** · obrolanpintar1987@gmail.com

Penyusun *prompt* akademik untuk peneliti Indonesia, dari skripsi hingga hibah
BIMA dan BRIN. Pilih bidang, jenjang, dan modul; salin ke asisten AI pilihan
Anda. Core Layer bekerja di balik layar.

## Apa yang baru di v8.0 (fokus Modul 10 — IMRAD)

Modul 10 (Draft Artikel IMRAD) ditulis ulang penuh:

- **Melanjutkan rangkaian.** Memakai hasil Modul 0-7, lalu sumber data dari
  Modul 8 (Dataset) **atau** Modul 9 (Statistik) sesuai pilihan Anda.
- **Dua skema target.** Scopus Q1 International (artikel penuh Bahasa Inggris)
  atau SINTA 2 Nasional (badan Bahasa Indonesia; abstrak dan kata kunci Inggris).
- **Struktur seragam.** Tiap bagian IMRAD ~750 kata, tiga sub-heading paragraf
  penuh, ditutup enam pertanyaan literatur Bahasa Inggris.
- **Methods bercabang menurut bidang.** Sains-Teknologi dan Ilmu Komputer:
  desain pengembangan model dengan flowchart algoritma dan dua kebaruan
  (*novelty*) bertanda lingkaran putus-putus. Umum dan Sosial-Humaniora:
  empat metode populer (Kuantitatif, Kualitatif, Humaniora, Mixed Methods).
- **Results bercabang.** Saintek/Ilkom: tabel dan grafik plus tabel perbandingan
  dengan penelitian sebelumnya. Soshum: data empiris disandingkan dengan
  penelitian terdahulu untuk menunjukkan pergeseran konseptual.
- **Penutup lengkap.** Conclusion 250 kata dengan angka kuantitatif, Abstract
  300 kata yang disusun terpisah, lima kata kunci satu suku kata, rekomendasi
  judul standar Scopus Q1, dan daftar pustaka APA 7.

## Integritas

- DOI hanya dicantumkan dari korpus; jika tidak yakin ditandai
  "[DOI perlu verifikasi di doi.org]". AI tidak menjamin keaktifan DOI.
- Firewall Integritas (Seksi K), anti-halusinasi (Seksi E), pengungkapan AI
  (Seksi O.2), dan Seksi P (Gaya Natural) tetap berlaku penuh.

## Login berbasis ACCESS_KEY (Streamlit Cloud Secrets Manager)

1. Buka aplikasi di share.streamlit.io.
2. Menu tiga titik -> **Settings** -> **Secrets**.
3. Masukkan, lalu **Save**:
   ```toml
   ACCESS_KEY = "kunci-rahasia-anda"
   ```
4. Halaman login akan meminta kunci tersebut. Dashboard hanya dikirim setelah
   kunci benar. Kunci tidak pernah disimpan di kode atau repositori.

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
ALAS-v8.0/
├── app.py                          Pembungkus + login ACCESS_KEY
├── dashboard.html                  Antarmuka + Core Layer tersembunyi
├── requirements.txt
├── ANALISIS_REVISI_CORE_LAYER.md   Analisis, pseudocode, 5 rekomendasi
├── .streamlit/config.toml
├── .streamlit/secrets.toml.example
├── .gitignore
└── .gitattributes
```
