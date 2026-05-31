# ALAS v8.2 — Asisten Riset Akademik

(c) 2024-2026 **Alhumaira Store** · obrolanpintar1987@gmail.com

Penyusun *prompt* akademik untuk peneliti Indonesia, dari skripsi hingga hibah
BIMA dan BRIN. Pilih bidang, jenjang, dan modul; salin ke asisten AI pilihan
Anda. Core Layer bekerja di balik layar.

## Apa yang baru di v8.2 — Modul 11: Proposal Hibah BIMA

Modul baru untuk menyusun proposal hibah BIMA, melanjutkan Modul 0-7 lalu
memakai sumber Modul 8 (rencana dataset) atau Modul 9 (rancangan analisis).

- **Empat sub-template:** PDP, PFR (Penelitian Dasar); Terapan Luaran Model,
  Terapan Luaran Prototipe (Penelitian Terapan).
- **Struktur mengikuti template BIMA:** Judul (maks 20 kata), Ringkasan
  (300 kata), 5 kata kunci satu kata, Pendahuluan (1000 kata: latar belakang
  dan 3 rumusan masalah, pendekatan, state of the art dan kebaruan, roadmap
  5 tahun gaya fishbone), Metode (1000 kata dengan diagram alir algoritma),
  Hasil yang Diharapkan, TKT, Jadwal (13 kegiatan), Daftar Pustaka APA.
- **Metode bercabang per bidang:** Saintek/Ilmu Komputer memakai pengembangan
  model dengan flowchart algoritma; Umum/Sosial-Humaniora memakai empat metode
  populer. Novelty ditandai garis putus-putus berwarna: satu novelty untuk
  penelitian 1 tahun, dua novelty untuk multiyear.
- **Khusus skema Terapan:** Strategi Pencapaian TKT (awal ke target), Rencana
  Kemitraan (Surat Kesediaan Mitra dan MoU, wajib), dan luaran model/prototipe
  beserta HKI.
- **Bobot penilaian per skema:** Modul 11 menyelaraskan penekanan penulisan
  dengan kriteria reviewer BIMA. Ini penyelaras kriteria, BUKAN jaminan lolos;
  kelolosan tergantung kompetisi, kuota, rekam jejak, dan penilaian reviewer.

## Integritas

- Semua angka panduan (jumlah kata, dana, RAB, TKT, masa penelitian) ditandai
  "[verifikasi panduan BIMA terbaru — bima.kemdiktisaintek.go.id]" karena dapat
  berubah tiap tahun.
- DOI hanya dicantumkan dari korpus; jika ragu ditandai
  "[DOI perlu verifikasi di doi.org]".
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
   kunci benar.

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
ALAS-v8.2/
├── app.py                          Pembungkus + login ACCESS_KEY
├── dashboard.html                  Antarmuka + Core Layer tersembunyi
├── requirements.txt
├── ANALISIS_REVISI_CORE_LAYER.md   Analisis, pseudocode, 5 rekomendasi
├── .streamlit/config.toml
├── .streamlit/secrets.toml.example
├── .gitignore
└── .gitattributes
```
