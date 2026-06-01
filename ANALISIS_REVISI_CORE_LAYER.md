# Analisis Revisi — ARAS v9.2 → v9.3 (Prasyarat M0-M7 Mengikuti Gaya v8.11)

Revisi mengembalikan perilaku prasyarat ke gaya v8.11: PENGINGAT berbasis teks,
tanpa penguncian UI. Isi prompt inti tidak diubah. Tanpa halusinasi, tanpa data
palsu.

## Bagian 1 — Analisis Logis

### 1.1 Latar
Pada v9.2, prasyarat M0-M7 dikunci di UI (checkbox bertahap + cascade reset).
Pengguna meminta mengikuti gaya v8.11.

### 1.2 Fakta v8.11
Di v8.11 TIDAK ada penguncian UI untuk M0-M7. Pengecekan "Modul 0-7 selesai?"
hanya berupa blok PEMERIKSAAN PRA-KONDISI di dalam teks prompt, yang dibaca oleh
AI tujuan. Pengguna bebas membuka/merakit modul; AI yang menjaga urutan.

### 1.3 Perubahan (v9.3)
- HAPUS checkbox penguncian bertahap dan cascade reset dari UI.
- GANTI dengan catatan pengingat (prasyarat_note) bergaya v8.11.
- Tombol "Rakit & Salin Prompt" tidak lagi terkunci; pengguna bebas merakit.
- Blok PEMERIKSAAN PRA-KONDISI tetap ada di dalam prompt (sudah sejak awal) dan
  menjadi penjaga urutan, persis seperti v8.11.

### 1.4 Konsekuensi (kejujuran)
- Dashboard tidak lagi mencegah perakitan sebelum M0-M7; penjagaan urutan
  bergantung pada AI tujuan yang membaca pra-kondisi. Ini perilaku v8.11 yang
  diminta pengguna, disampaikan apa adanya.
- Tidak ada perubahan pada isi prompt inti, pemetaan tujuan, kunci sumber per
  bidang, komposisi target M10, maupun Core Layer server-side.

## Bagian 2 — Pseudocode
    ALGORITMA prasyarat_gaya_v811():
        tampilkan catatan: "selesaikan M0-M7 berurutan, lalu M8/M9 per bidang"
        # tidak ada penguncian UI
    # tombol rakit selalu aktif; AI tujuan membaca PEMERIKSAAN PRA-KONDISI
    # dan berhenti bila prasyarat kosong.

## Bagian 3 — Verifikasi
- Tidak ada checkbox di UI (0). (terverifikasi)
- Tombol rakit aktif tanpa syarat; perakitan bebas menghasilkan prompt akhir
  berisi Core Layer DAN blok PEMERIKSAAN PRA-KONDISI. (terverifikasi)
- 8/8 uji unit assembler tetap lulus.

## Bagian 4 — Yang dipertahankan
Pemetaan tujuan->modul, kunci sumber per bidang, komposisi target M10, Core
Layer server-side, anti-deteksi AI tidak diterapkan, anti-fabrikasi. Isi prompt
inti tidak berubah.
