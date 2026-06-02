# ARAS v9.4 — Asisten Riset Akademik System

(c) 2024-2026 **Alhumaira Store** · obrolanpintar1987@gmail.com

Penyusun *prompt* akademik untuk peneliti Indonesia (skripsi, tesis, disertasi,
Hibah BIMA, BRIN, publikasi internasional/Sinta, laporan penelitian). Beranda
menjadi panel manajemen proses; salin prompt tiap modul ke asisten AI mana pun.
**Core Layer berjalan tersembunyi.**

## Beranda — Dashboard & panduan

Tiga pilihan menggerakkan seluruh sistem:

1. **Bidang Ilmu**: Umum · Sosial & Humaniora · Sains & Teknologi · Ilmu Komputer
2. **Jenjang / Skema** (8 item; penegas konteks)
3. **Tujuan** (driver routing)

Routing modul terminal mengikuti **Tujuan**:
Skripsi→M13 · Tesis→M14 · Disertasi→M15 · Hibah Bima→M11 · BRIN→M12 ·
Publikasi Internasional→M10 (tier Scopus Q1–Q4) · Publikasi Sinta→M10
(tier Sinta 1–4) · Laporan Penelitian→M16.

Cabang per bidang: **M8 (dataset)** untuk Sains & Teknologi / Ilmu Komputer;
**M9 (statistik multivariat)** untuk Umum / Sosial & Humaniora.

Rail proses menampilkan **M0–M7 saja**. Cabang M8/M9 dan modul terminal hanya
tersimpan sebagai routing (dijalankan setelah M7), dengan tombol salin prompt
terpisah di kotak routing.

## Prompt per modul (salin-tempel)

Klik M0–M7 untuk memunculkan prompt yang sudah menyertakan konteks pilihan,
MCB, dan aturan integritas, lalu salin ke ChatGPT/Claude/Gemini/Copilot/DeepSeek.

Adaptasi konteks (Opsi B): **M0** basis data per bidang · **M5** jenis audit
(eksperimental vs naratif/kualitatif) · **M7** mode desain + jumlah novelty.
M1–M4 dan M6 berstruktur sama (invarian). M7 menyediakan alat bertahap: tempel
10 judul (dari M6) → tombol per judul → prompt A–F di canvas baru, satu per
canvas (siasati limit).

## Core Layer (tersembunyi) — pipeline 7 tahap

intake → context-lock (MCB) → router → firewall integritas → gerbang
konsistensi C→D→E→F → naturalizer (gaya natural, pengungkapan AI tetap) →
output (canvas baru + checkpoint). Rincian: `ANALISIS_REVISI_CORE_LAYER.md`.

## Integritas

Angka, DOI, peringkat, dan ketersediaan tidak dikarang; yang ragu ditandai untuk
verifikasi. Tidak ada fitur pengelabuan detektor AI; pengungkapan AI
dipertahankan.

## Login (Streamlit Cloud Secrets Manager)

Settings → Secrets, lalu:

    ACCESS_KEY = "kunci-rahasia-anda"

Uji lokal: salin `.streamlit/secrets.toml.example` → `.streamlit/secrets.toml`,
isi kunci, lalu `streamlit run app.py`.

## Jalankan lokal

```
pip install -r requirements.txt
streamlit run app.py
```

## Deploy

Unggah seluruh isi folder ke GitHub, deploy `app.py` di share.streamlit.io.

## Struktur

```
ARAS-v9.1/
|- app.py
|- dashboard.html
|- requirements.txt
|- ANALISIS_REVISI_CORE_LAYER.md
|- .streamlit/config.toml
|- .streamlit/secrets.toml.example
|- .gitignore
|- .gitattributes
```

## Catatan v9.4
- Penguat 77 kata (tak berlabel) memperkuat M0–M7.
- M7/C kini: 5 penelitian terdahulu → GAP → 1 penelitian saat ini yang menjawab
  GAP (kontribusi diusulkan, bukan data dikarang).
- M7/D: novelty bertipe per tingkat — S1 Application, S2 Improvement,
  S3 Invention; BIMA & BRIN tetap (2 novelty multiyear).

## Catatan v9.4
- M0 punya dua mode: Standar (default) dan Analisis Dokumen Manual.
- Mode Analisis Dokumen: ARAS hanya menyiapkan prompt; PDF (≤10) Anda lampirkan
  langsung di mesin AI. ARAS tidak menerima atau memproses file.
- M1–M7 tetap standar.

## Catatan v9.4
- Sub-skema kini untuk empat Tujuan: Hibah Bima (PDP, PDP Afirmasi, Fundamental
  Reguler, PKDN, Terapan-Model, Terapan-Prototipe), BRIN (RIIM Kompetisi,
  Ekspedisi, Invitasi, Kolaborasi, Start-Up), Publikasi Internasional (Scopus
  Q1-Q4), Publikasi Sinta (Sinta 1-4).
- Sub-skema masuk MCB dan menyetel standar penulisan di modul terminal.
- Nama skema BIMA/BRIN diverifikasi dari sumber resmi; UI mengingatkan untuk
  menyesuaikan dengan panduan tahun berjalan karena dapat berubah.
