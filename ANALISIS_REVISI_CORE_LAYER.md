# Analisis Revisi Core Layer — ALAS v8.4 → v8.5 (Modul 13: Proposal Skripsi)

Dokumen ini berisi analisis logis untuk penambahan Modul 13 (Proposal Skripsi),
disertai pseudocode dan lima rekomendasi inti (R1-R5) plus satu rekomendasi
pendukung (R8). Prinsip: pertahankan yang sudah baik, perbaiki yang lemah,
kembangkan yang berpotensi. Tanpa halusinasi, tanpa data palsu, integritas
dijaga.

## Bagian 1 — Analisis Logis

### 1.1 Yang dipertahankan (tidak direvisi)
1. Modul 0-12 beserta struktur dan aturannya.
2. Anti-halusinasi (E), Firewall (K), pengungkapan AI (O.2), PUBEI (C),
   Gaya Natural (P), protokol kanvas baru per segmen yang diperkuat (v8.4).
3. Login ACCESS_KEY dan Core Layer tersembunyi.

### 1.2 Penambahan (Modul 13 — Proposal Skripsi)
- Melanjutkan Modul 0-7, lalu sumber Modul 8 (rencana dataset) atau Modul 9
  (rancangan analisis).
- Dua tahap: Tahap 1 Seminar Proposal (Bab 1-3); Tahap 2 Seminar Hasil (Bab 1-5).
- Bab 2 (Kajian Pustaka) memakai heading + 4 sub-heading, masing-masing ditutup
  5 pertanyaan literatur Bahasa Inggris sebagai bagian naskah; sitasi APA.
- Bab 4-5 berupa kerangka bertanda anti-fabrikasi "[isi dari hasil penelitian
  Anda]"; bentuk Bab 5 menyesuaikan jenis penelitian (angka/tematik).

### 1.3 Keputusan etis dan kejujuran (konsisten)
- Anti-deteksi AI TIDAK diterapkan (langgar K dan O.2; klaim tak terjamin).
- Angka hasil tidak dikarang; ditandai "[isi dari hasil penelitian Anda]".
- Standar khas kampus ditandai "[sesuaikan panduan kampus]".
- DOI hanya dari korpus; jika ragu "[DOI perlu verifikasi di doi.org]".
- Gerbang kelengkapan adalah alat bantu, BUKAN jaminan lulus seminar.

## Bagian 2 — Pseudocode
    ALGORITMA workflow_M13(tahap, bidang, jenis):
        PRA: Modul 0-7 selesai; sumber := Modul 8 ATAU Modul 9
        JIKA tahap = 1: keluarkan Bab 1, 2, 3 (3 kanvas)
        JIKA tahap = 2: keluarkan Bab 1..5 (5 kanvas)
        Bab 3 bercabang bidang (MODEL/SOSHUM) DAN jenis (Kuanti/Kuali/R&D)
        rumusan masalah (Bab 1) -> dijawab Bab 4 -> disimpulkan Bab 5 (benang merah)
        glosarium konsisten dari Modul 1 lintas-bab
        cek konsistensi sitasi Bab 2 <-> Daftar Pustaka
        gerbang kelengkapan per tahap sebelum selesai

## Bagian 3 — Lima Rekomendasi Inti (diterapkan)
1. Pembagian kanvas sadar-tahap (Tahap 1 = 3 kanvas; Tahap 2 = 5 kanvas).   [R1]
2. Benang merah rumusan masalah (RM -> Bab 4 -> Bab 5).                      [R2]
3. Bab 3 bercabang jenis penelitian (Kuantitatif/Kualitatif/R&D).           [R3]
4. Konsistensi terminologi/glosarium dari Modul 1 lintas-bab.               [R4]
5. Gerbang kelengkapan per tahap (alat bantu, bukan jaminan lulus).         [R5]
Pendukung: konsistensi sitasi Bab 2 <-> Daftar Pustaka.                     [R8]

## Bagian 4 — Ringkasan Peningkatan v8.5 vs v8.4
- Modul baru: Modul 13 (Proposal Skripsi); 15 modul total.
- Dua tahap, Bab 2 dengan pertanyaan literatur per heading/sub-heading, Bab 3
  bercabang bidang dan jenis, Bab 4-5 anti-fabrikasi.
- Integritas tetap utuh; tidak ada klaim berlebih atau data palsu.
