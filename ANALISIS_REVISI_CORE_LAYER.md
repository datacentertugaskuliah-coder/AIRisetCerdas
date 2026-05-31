# Analisis Revisi Core Layer — ALAS v8.3 → v8.4 (Penguatan Protokol Kanvas M11 & M12)

Dokumen ini berisi analisis logis untuk penguatan protokol kanvas baru per
segmen pada Modul 11 (Proposal BIMA) dan Modul 12 (Proposal BRIN RIIM), disertai
pseudocode dan lima rekomendasi. Prinsip: pertahankan yang sudah baik, perbaiki
yang lemah. Tanpa halusinasi, tanpa data palsu, integritas dijaga.

## Bagian 1 — Analisis Logis

### 1.1 Temuan awal (jujur)
Protokol kanvas baru per segmen SUDAH ADA di M10, M11, dan M12 sejak v8.1-v8.3.
Maka revisi ini BUKAN menambah fitur yang hilang, melainkan MEMPERKUAT dan
MEMPERJELAS instruksi yang sudah ada agar lebih sulit dilanggar oleh AI tujuan.

### 1.2 Kelemahan yang diperbaiki
- C1: Instruksi lama hanya menyebut "tulis di kanvas baru" tanpa aturan tegas
  satu-segmen-satu-kanvas, sehingga sebagian AI menggabung segmen.
- C2: Belum ada penanganan bila ruang kanvas menipis di TENGAH segmen.
- C3: Belum ada penegasan menunggu aba-aba "LANJUT" sebelum segmen berikutnya.

### 1.3 Yang dipertahankan (tidak diubah)
Seluruh isi substansi M11 dan M12 (struktur proposal, TKT, RAB, IKR, novelty,
daftar pustaka APA), Core Layer, modul lain, login ACCESS_KEY, Seksi P.

### 1.4 Keputusan etis (konsisten)
Anti-deteksi AI TIDAK diterapkan. Tidak ada angka/DOI fabrikasi. Semua angka
panduan tetap bertanda verifikasi.

## Bagian 2 — Pseudocode Penguatan
    ALGORITMA kanvas_per_segmen_kuat:
        ATURAN: satu kanvas = satu segmen (tidak boleh gabung)
        UNTUK setiap segmen s:
            BUAT kanvas baru berjudul "[KODE] - s"
            tulis s sampai SELESAI
            JIKA ruang menipis di tengah s:
                tutup "[BERSAMBUNG — ketik LANJUT untuk sisa segmen ini]"
                lanjut sisa s di kanvas baru saat diminta
            akhiri: "=== AKHIR s === | LANJUT [segmen berikutnya]"
            BERHENTI; tunggu aba-aba "LANJUT" sebelum segmen berikutnya
        FALLBACK: jika platform tak punya kanvas -> blok berjudul, satu per respons

## Bagian 3 — Lima Rekomendasi (diterapkan)
1. Aturan tegas SATU KANVAS = SATU SEGMEN. DITERAPKAN.
2. Wajib membuat kanvas baru SEBELUM menulis segmen berikutnya. DITERAPKAN.
3. Penanganan "BERSAMBUNG" bila ruang menipis di tengah segmen. DITERAPKAN.
4. Penegasan berhenti dan menunggu aba-aba "LANJUT". DITERAPKAN.
5. Daftar segmen eksplisit per modul + pemetaan istilah lintas-AI + fallback.
   DITERAPKAN.

## Bagian 4 — Ringkasan Peningkatan v8.4 vs v8.3
- Protokol kanvas M11 dan M12 diperkuat dengan 5 aturan inti yang lebih tegas.
- Penanganan ruang-menipis dan aba-aba LANJUT ditambahkan.
- Substansi proposal tidak diubah; hanya instruksi kanvas yang diperjelas.
- Integritas tetap utuh; tidak ada klaim berlebih atau data palsu.
