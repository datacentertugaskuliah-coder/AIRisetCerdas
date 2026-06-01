# ARAS v9.4 — Asisten Riset Akademik System

(c) 2024-2026 **Alhumaira Store** · obrolanpintar1987@gmail.com

Penyusun *prompt* akademik terpandu untuk peneliti Indonesia. Versi 9.1
mengubah ALAS menjadi **ARAS** dengan alur berbasis tujuan: pengguna memilih
bidang dan tujuan, lalu sistem menentukan modul dan aturannya secara otomatis.
Lapisan Inti (Core Layer) tetap di sisi server.

## Apa yang baru di v9.4

- **Ganti nama:** ALAS menjadi **ARAS — Asisten Riset Akademik System**.
- **Sidebar daftar modul (gaya v8.11).** Pilih Modul 0-16 langsung dari
  sidebar kiri. Pintasan Tujuan di Beranda tetap tersedia (opsional) untuk
  melompat ke modul yang sesuai. Kunci sumber per bidang tetap berlaku.
  membingungkan).
- **Pemetaan Tujuan ke modul:**
  - Skripsi -> Modul 13
  - Tesis -> Modul 14
  - Disertasi -> Modul 15
  - Hibah BIMA -> Modul 11
  - BRIN -> Modul 12
  - Publikasi Internasional -> Modul 10 (target Scopus Q1/Q2/Q3/Q4)
  - Publikasi SINTA -> Modul 10 (target SINTA 1/2/3/4)
  - Laporan Penelitian -> Modul 16
- **Sumber data dikunci per bidang.** Sains dan Teknologi / Ilmu Komputer ->
  Modul 8 (Dataset). Umum / Sosial dan Humaniora -> Modul 9 (Statistik).
- **Komposisi sumber bertingkat untuk publikasi (Modul 10):** makin tinggi
  target, makin dominan rujukan internasional bermutu; makin nasional, makin
  dominan SINTA. (Q1 90/10 ... SINTA 4 dominan SINTA.)
- **Prasyarat fondasi gaya v8.11 (tanpa penguncian UI).** Modul 0-7 ditampilkan
  sebagai PENGINGAT; penjagaan urutan dilakukan oleh blok PEMERIKSAAN PRA-KONDISI
  di dalam prompt yang dibaca AI tujuan. Pengguna bebas merakit prompt; AI akan
  berhenti jika prasyarat belum terpenuhi.
- **Ringkasan konteks (R3)** sebelum merakit prompt.
- **Core Layer tetap di server.** Hanya hasil rakitan akhir dikirim ke klien.

## Komposisi sumber per target (Modul 10)

| Target | Internasional | SINTA |
|--------|---------------|-------|
| Scopus Q1 | 90% (Q1 diutamakan) | 10% (SINTA 1-2) |
| Scopus Q2 | 80% (Q1/Q2) | 20% (SINTA 1-2) |
| Scopus Q3 | 70% (Q2/Q3) | 30% (SINTA 1-2) |
| Scopus Q4 | 60% (Q3/Q4/IEEE) | 40% (SINTA 1-3) |
| SINTA 1 | 30% (Q3/Q4) | 70% (SINTA 1-2) |
| SINTA 2 | 20% (Q4/IEEE) | 80% (SINTA 1-3) |
| SINTA 3 | 10% | 90% (SINTA 1-4) |
| SINTA 4 | 0-10% | 90-100% (SINTA 1-5) |

Anti-fabrikasi berlaku di semua tingkat: DOI, tautan, peringkat, dan status open
access tidak dikarang; yang ragu ditandai untuk verifikasi.

## Struktur paket

```
ARAS-v9.4/
├── app.py                       # entry Streamlit (alur terpandu)
├── alas_core/
│   ├── __init__.py
│   ├── config.py                # bidang, tujuan, pemetaan modul, komposisi
│   ├── store.py                 # pemuat prompt (SERVER ONLY)
│   ├── assembler.py             # perakit prompt akhir (SERVER ONLY)
│   ├── auth.py                  # gerbang ACCESS_KEY (hmac)
│   └── data/prompts.json        # Lapisan Inti + modul (RAHASIA)
├── ui/render.py                 # komponen tampilan + alur
├── tests/test_assembler.py      # 8 uji
├── requirements.txt
├── LICENSE
├── README.md
├── .gitignore
├── .gitattributes
└── .streamlit/{config.toml, secrets.toml.example}
```

## Menjalankan secara lokal

```bash
pip install -r requirements.txt
cp .streamlit/secrets.toml.example .streamlit/secrets.toml   # isi ACCESS_KEY
streamlit run app.py
```

## Deploy ke Streamlit Cloud

Unggah folder ini ke GitHub (tanpa secrets.toml), deploy `app.py` di
share.streamlit.io, lalu isi `ACCESS_KEY` di Settings -> Secrets.

## Integritas (konsisten)

- Anti-deteksi AI tidak diterapkan; Seksi P (Gaya Natural) sebagai gantinya.
- Tidak ada angka, DOI, peringkat, atau data yang dikarang.
- Pengungkapan AI (Seksi O.2) tetap berlaku.
