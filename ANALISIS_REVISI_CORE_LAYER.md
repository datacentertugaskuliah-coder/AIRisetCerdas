# Analisis Revisi — ARAS v9.3 → v9.4 (Kembalikan Sidebar Daftar Modul Gaya v8.11)

Revisi mengembalikan cara memilih modul ke gaya v8.11 (sidebar daftar Modul
0-16, pilih langsung), tetap server-side, sambil mempertahankan pemetaan tujuan
dan kunci sumber per bidang. Isi prompt inti tidak diubah.

## Bagian 1 — Analisis Logis

### 1.1 Masalah pada v9.3
Alur berbasis tujuan (pilih Bidang -> Tujuan -> modul otomatis) terasa
membingungkan karena menghilangkan kebiasaan v8.11: memilih modul langsung dari
daftar di sidebar.

### 1.2 Solusi (v9.4)
- KEMBALIKAN sidebar daftar Modul 0-16 sebagai pemilih utama (gaya v8.11).
- Pemetaan Tujuan -> modul DIPERTAHANKAN sebagai PINTASAN opsional di Beranda;
  bukan satu-satunya jalan.
- Kunci sumber per bidang (Saintek/Ilkom -> M8; Umum/Soshum -> M9) TETAP berlaku.
- Untuk M10 yang dipilih dari sidebar: tampilkan pemilih Jenis Publikasi
  (Internasional/SINTA) lalu Target, dengan komposisi bertingkat.

### 1.3 Yang dipertahankan
- Komposisi target M10 bertingkat (Q1 90/10 ... SINTA 4 dominan SINTA).
- Core Layer server-side; prasyarat M0-M7 gaya v8.11 (pengingat, bukan kunci UI).
- Anti-deteksi AI tidak diterapkan; anti-fabrikasi. Isi prompt inti tidak berubah.

## Bagian 2 — Pseudocode
    ALGORITMA pilih_modul_v411():
        modul := sidebar_radio(Modul 0..16)           # pemilih utama (v8.11)
        JIKA pengguna pakai Pintasan Tujuan di Beranda:
            modul := TUJUAN_KE_MODUL[tujuan]           # lompatan opsional
        JIKA modul = M10:
            jenis := pilih(Internasional / SINTA)
            target := pilih(Q1-Q4 / SINTA 1-4) ; tampilkan komposisi
        rakit_sisi_server(modul, konteks)             # hanya hasil akhir ke klien

## Bagian 3 — Verifikasi
- Sidebar memuat 17 modul (Modul 0 sampai Modul 16); pilih langsung. (terverifikasi)
- M13 menampilkan Tahap + Jenis Penelitian; M0 tanpa galat. (terverifikasi)
- M10: pilih Jenis Publikasi -> Target diperbarui (SINTA 1-4 / Scopus Q1-Q4);
  perakitan menghasilkan komposisi yang benar (mis. SINTA 4 -> dominan SINTA).
  (terverifikasi)
- Perakitan menghasilkan prompt akhir berisi Core Layer. (terverifikasi)
- 8/8 uji unit assembler tetap lulus.

## Bagian 4 — Catatan jujur
Pintasan Tujuan dan sidebar bisa saling melengkapi; bila keduanya dipakai,
pilihan terakhir (sidebar atau pintasan) yang menentukan modul aktif. Tidak ada
perubahan pada isi prompt inti.
