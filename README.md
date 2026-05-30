# ALAS v6.0 — Academic Literature Analysis System

(c) 2024-2026 **Alhumaira Store** · obrolanpintar1987@gmail.com

Penyusun *prompt* akademik untuk peneliti Indonesia. Pilih modul, isi konteks,
lalu salin ke asisten AI pilihan Anda (ChatGPT, Claude, Gemini, dan lainnya).

## Apa yang baru di v6.0

- **Core Layer tersembunyi.** Fondasi 16 seksi (A-P) berjalan di balik layar.
  Antarmuka tampil rapi sebagai dashboard, tetapi Core Layer tetap ikut tersalin
  setiap kali Anda menekan tombol "Salin Prompt".
- **Seksi P: Protokol Gaya Penulisan Natural.** Prosa yang lebih luwes dan
  manusiawi dengan tanda baca rapi, tanpa mengorbankan integritas akademik atau
  penanda epistemik. Bukan alat anti-deteksi.
- **Dashboard pengembangan.** Beranda menampilkan ringkasan fitur, statistik
  sistem, dan diagram alur 12 modul yang mudah dipahami.
- **Klaim jujur.** Deskripsi fitur kini sesuai dengan implementasi nyata.
  Penanda sesi opsional dan nonaktif secara default.
- **Versi konsisten.** Seluruh berkas diseragamkan ke v6.0 (2024-2026).

## Integritas

Core Layer mempertahankan Firewall Integritas (Seksi K), aturan anti-halusinasi
(Seksi E), dan standar pengungkapan AI (Seksi O.2). Setiap penggunaan AI tetap
wajib diungkapkan sesuai kebijakan jurnal target.

## Cara menjalankan secara lokal

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy ke Streamlit Cloud

1. Unggah seluruh isi folder ini ke repositori GitHub Anda.
2. Buka share.streamlit.io, pilih repositori, dan atur `app.py` sebagai berkas utama.
3. Klik Deploy.

## Kompatibel

Smartphone iOS/Android, tablet, dan laptop/desktop.

## Struktur berkas

```
ALAS-v6.0/
├── app.py                          Pembungkus Streamlit
├── dashboard.html                  Antarmuka + Core Layer tersembunyi
├── requirements.txt
├── ANALISIS_REVISI_CORE_LAYER.md   Analisis, pseudocode, 5 rekomendasi
├── .streamlit/config.toml
├── .gitignore
└── .gitattributes
```
