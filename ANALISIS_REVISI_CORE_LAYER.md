# Analisis Revisi Core Layer — ALAS v8.0 → v8.1 (Canvas Baru per Jawaban, Modul 10)

Dokumen ini berisi analisis logis dan komprehensif untuk revisi terfokus pada
Modul 10 (Draf Artikel IMRAD), disertai konsep algoritma dan pseudocode, lalu
lima rekomendasi perbaikan yang diwujudkan ke Core Layer. Prinsip: pertahankan
yang sudah baik, perbaiki yang lemah, kembangkan yang berpotensi. Tanpa
halusinasi, tanpa data palsu, integritas dijaga.

## Bagian 1 — Analisis Logis

### 1.1 Yang dipertahankan (tidak direvisi)
1. Struktur IMRAD: 750 kata/bagian, 3 sub-heading, 6 pertanyaan literatur.
2. Percabangan Methods (flowchart+2 novelty / 4 metode) dan Results per bidang.
3. Penutup: Conclusion 250 kata, Abstract 300 kata terpisah, 5 keyword,
   5 rekomendasi judul Scopus Q1, daftar pustaka APA anti-fabrikasi DOI.
4. Anti-halusinasi (E), Firewall (K), pengungkapan AI (O.2), PUBEI (C),
   Gaya Natural (P).

### 1.2 Masalah yang diatasi
- C1: Output IMRAD sangat panjang; menumpuk di satu kanvas menabrak batas/limit,
  khususnya ChatGPT Canvas.
- C2: Tiap AI punya istilah berbeda (Canvas, Artifacts, Gemini Canvas); instruksi
  harus netral lintas-platform.

### 1.3 Keputusan etis (konsisten)
"Anti-deteksi AI" tidak diterapkan (langgar K & O.2; klaim tak terjamin). Seksi P
(gaya natural sah) tetap dipakai. Tidak ada klaim melebihi implementasi.

## Bagian 2 — Konsep Algoritma & Pseudocode

### 2.1 Canvas baru per segmen
    ALGORITMA canvas_per_segmen:
        segmen := [Introduction, Methods, Results, Discussion, Penutup]
        UNTUK setiap s DALAM segmen:
            BUAT kanvas/dokumen BARU berjudul "[KODE] - [nama s]"
            JANGAN menambah ke kanvas sebelumnya
            tulis isi s; di akhir beri penanda "LANJUT [segmen berikut]"
        Pemetaan istilah: ChatGPT->Canvas, Claude->Artifact, Gemini->Canvas,
        lainnya->dokumen terpisah.

### 2.2 Penanda kelanjutan
    di akhir tiap kanvas: "=== AKHIR [segmen] === | LANJUT [segmen berikut]"
    sertakan KODE SESI sebagai prefiks judul setiap kanvas.

### 2.3 Konsistensi lintas-kanvas
    setiap kanvas memakai kode sesi, penomoran, glosarium, skema, bidang yang
    sama. Jika AI tak mendukung kanvas terpisah -> fallback blok berjudul.

## Bagian 3 — Lima Rekomendasi Perbaikan
1. Aturan kanvas baru per segmen IMRAD. DITERAPKAN.
2. Pemetaan istilah lintas-AI yang netral. DITERAPKAN.
3. Penanda kelanjutan antar-kanvas. DITERAPKAN.
4. Konsistensi lintas-kanvas (kode sesi, penomoran, glosarium). DITERAPKAN.
5. Fallback bila AI tak mendukung kanvas terpisah. DITERAPKAN.

## Bagian 4 — Ringkasan Peningkatan v8.1 vs v8.0
- Modul 10 memecah keluaran panjang ke beberapa kanvas baru (anti-limit).
- Instruksi netral lintas-AI dengan padanan istilah per platform.
- Penanda kelanjutan dan penjaga konsistensi antar-kanvas.
- Integritas (E, K, O.2, P) tetap utuh; tidak ada klaim berlebih.
