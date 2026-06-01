# Analisis Revisi — ARAS v9.1 → v9.2 (Prasyarat M0-M7 Bertahap Berurutan)

Revisi terfokus pada perilaku prasyarat fondasi: dari centang bebas menjadi
bertahap berurutan dengan cascade reset. Isi prompt inti tidak diubah. Tanpa
halusinasi, tanpa data palsu.

## Bagian 1 — Analisis Logis

### 1.1 Masalah pada v9.1
Kedelapan checkbox M0-M7 dapat dicentang dalam urutan apa pun. Ini memungkinkan
keadaan janggal (mis. M5 tercentang tanpa M0-M4), padahal alur riset bersifat
berurutan: pencarian literatur -> intake -> analisis -> dst.

### 1.2 Solusi (v9.2)
- BERTAHAP: M0 aktif sejak awal; M(n) terkunci (disabled) sampai M(n-1) selesai.
- CASCADE RESET: membatalkan centang M(n) otomatis membatalkan M(n+1)..M7,
  sehingga status selalu konsisten dengan urutan.
- Modul tujuan tetap terkunci sampai seluruh M0-M7 selesai.

### 1.3 Keputusan kunci (kejujuran)
- Dipilih cascade reset (bukan "kunci ke depan saja") karena paling konsisten
  dengan aturan berurutan: mustahil M(n) benar selesai bila prasyaratnya batal.
- Implementasi menegakkan aturan pada state widget (key fon_*) agar checkbox
  hilir benar-benar ter-uncheck secara visual, bukan hanya di data.
- Tidak ada penanda visual khusus "giliran berikutnya" (sesuai pilihan pengguna);
  cukup penguncian + pesan langkah berikutnya.

## Bagian 2 — Pseudocode
    ALGORITMA prasyarat_berurutan(fondasi):
        # pra-pass: tegakkan urutan pada state widget
        putus := salah
        UNTUK m DALAM fondasi (urut):
            JIKA putus: paksa state[m] := False        # cascade reset
            LAIN JIKA NOT state[m]: putus := benar
        # render
        UNTUK i, m DALAM fondasi:
            prasyarat_ok := semua(done[fondasi[j]] untuk j < i)
            tampilkan checkbox(m, disabled = NOT prasyarat_ok)
            done[m] := nilai_centang AND prasyarat_ok
        KEMBALIKAN semua(done)

## Bagian 3 — Verifikasi
- Awal: hanya M0 aktif; M1-M7 terkunci. (terverifikasi)
- Setelah M0 dicentang: M1 terbuka; M2-M7 tetap terkunci. (terverifikasi)
- Setelah M0,M1,M2 lalu M1 dibatalkan: M2 ikut batal dan terkunci kembali;
  M0 tetap. (terverifikasi cascade reset)
- Setelah M0-M7 dicentang berurutan: tombol rakit aktif; perakitan menghasilkan
  prompt akhir berisi Core Layer tanpa galat. (terverifikasi)
- 8/8 uji unit assembler tetap lulus.

## Bagian 4 — Yang dipertahankan
Seluruh pemetaan tujuan, kunci sumber per bidang, komposisi target M10, Core
Layer server-side, anti-deteksi AI tidak diterapkan, anti-fabrikasi. Isi prompt
inti tidak berubah.
