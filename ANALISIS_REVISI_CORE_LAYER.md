# Analisis Revisi Core Layer — ALAS v8.10 → v8.11 (Penyeragaman Justifikasi & Bidang: M10, M13)

Revisi terfokus untuk menyeragamkan tiga fitur di Modul 10, 13, 14, 15. Audit
menunjukkan sebagian SUDAH ADA; revisi hanya melengkapi yang belum, tanpa
menumpuk fitur ganda. Tanpa halusinasi, tanpa data palsu, integritas dijaga.

## Bagian 1 — Analisis Logis

### 1.1 Temuan audit (jujur)
| Fitur                         | M10 | M13 | M14 | M15 |
|-------------------------------|-----|-----|-----|-----|
| Protokol kanvas baru          | ada | ada | ada | ada |
| 5 pertanyaan literatur        | ada*| ada | ada | ada |
| Justifikasi tiap heading/sub  | -   | -   | ada | ada |
| Selektor bidang di halaman    | -   | ada | ada | ada |
(*M10 memakai pola lama 6 pertanyaan IMRAD.)

### 1.2 Yang dikerjakan (hanya yang belum ada)
- M10: tambah JUSTIFIKASI; ganti pola 6-pertanyaan menjadi 5 pertanyaan dalam
  BLOK bertanda "hapus sebelum submit jurnal" (R1, R3); tambah selektor bidang
  di halaman dengan render live (R4).
- M13: tambah JUSTIFIKASI di paragraf terakhir tiap heading/sub-heading (R2);
  5 pertanyaan dan selektor bidang sudah ada (tidak diduplikasi).
- M14, M15: sudah lengkap; tidak disentuh.

### 1.3 Keputusan kunci (kejujuran)
- Tidak menumpuk dua sistem pertanyaan di M10 (R1) - pola lama diganti, bukan
  ditambah.
- M10 (artikel jurnal) memakai blok "hapus sebelum submit" karena artikel
  bereputasi tidak lazim memuat blok pertanyaan literatur (R3).
- Tidak menambah selektor bidang kedua di M13 yang sudah punya (anti-duplikasi).
- Anti-deteksi AI TIDAK diterapkan; data/DOI tidak dikarang.

## Bagian 2 — Pseudocode
    ALGORITMA seragamkan(modul):
        JIKA modul belum punya justifikasi -> tambah di paragraf terakhir tiap
            heading/sub-heading (rumusan seragam R2)
        JIKA modul = M10 -> 5 pertanyaan dalam blok "hapus sebelum submit";
            JANGAN biarkan pola 6-pertanyaan lama tersisa (R1)
        JIKA modul belum punya selektor bidang di halaman -> tambah + render live
        JIKA modul sudah punya fitur -> JANGAN duplikasi

## Bagian 3 — Lima Rekomendasi (diterapkan)
1. Hindari penumpukan dua sistem pertanyaan di M10 (ganti, bukan tambah).
2. Rumusan justifikasi seragam di M10, M13, M14, M15.
3. M10 memakai blok "hapus sebelum submit jurnal" demi kelayakan submit.
4. Selektor bidang di halaman M10 dengan render live.
5. Perapian versi dan registry saat rilis v8.11.

## Bagian 4 — Ringkasan Peningkatan v8.11 vs v8.10
- M10 dan M13 kini seragam dengan M14/M15 untuk justifikasi; M10 dapat selektor
  bidang dan blok pertanyaan yang aman untuk jurnal.
- Tidak ada fitur ganda; konsistensi lintas-modul meningkat.
- Integritas tetap utuh; tidak ada klaim berlebih atau data palsu.
