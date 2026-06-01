# Analisis Revisi Core Layer — ARAS v9.0 → v9.1 (Alur Terpandu Berbasis Tujuan)

Penataan ulang ALAS menjadi ARAS dengan alur berbasis tujuan. Isi prompt inti
tidak diubah; yang ditambah adalah pemetaan tujuan, kunci sumber per bidang,
komposisi target M10, dan pemandu alur. Tanpa halusinasi, tanpa data palsu.

## Bagian 1 — Analisis Logis

### 1.1 Perubahan utama
- Ganti nama ALAS -> ARAS (Asisten Riset Akademik System).
- Beranda terpandu: Bidang + Tujuan; Jenjang/Skema otomatis dari Tujuan (Opsi 2,
  menghindari dua pilihan identik yang membingungkan).
- Tujuan menentukan modul: Skripsi->M13, Tesis->M14, Disertasi->M15,
  Hibah BIMA->M11, BRIN->M12, Publikasi Internasional->M10 (Q1-Q4),
  Publikasi SINTA->M10 (SINTA 1-4), Laporan->M16.
- Sumber data dikunci per bidang: Saintek/Ilkom->M8; Umum/Soshum->M9.
- Komposisi sumber M10 bertingkat per target (Q1 90/10 ... SINTA 4 dominan SINTA).

### 1.2 Keputusan kunci (kejujuran)
- Dua dropdown identik berisiko kontradiksi; diselesaikan dengan Opsi 2
  (Jenjang/Skema mengikuti Tujuan).
- Kunci M8/M9 per bidang mengubah modul luaran agar otomatis, bukan pilihan
  bebas; ini selaras metodologi (dataset/model untuk teknik, statistik untuk
  soshum).
- Komposisi bertingkat tetap anti-fabrikasi; tidak ada DOI/peringkat dikarang.
- Lapisan Inti tetap server-side; isi prompt inti tidak diubah.

### 1.3 Rekomendasi alur yang diterapkan
- R1: pemandu alur berbasis tujuan di Beranda.
- R2: indikator status + penguncian modul tujuan hingga M0-M7 selesai.
- R3: ringkasan konteks sebelum merakit.
- (R4 peringatan kombinasi dan R5 riwayat sesi sengaja dilewati: berisiko
  menghakimi / berlebihan untuk saat ini.)

## Bagian 2 — Pseudocode
    ALGORITMA alur_terpandu(bidang, tujuan):
        jenjang := TUJUAN_KE_JENJANG[tujuan]        # otomatis
        modul   := TUJUAN_KE_MODUL[tujuan]
        sumber  := (bidang in {Saintek, Ilkom}) ? M8 : M9
        JIKA tujuan in {Publikasi Internasional, Publikasi SINTA}:
            target := pilih dari daftar (Q1-Q4 / SINTA 1-4)
            komposisi := KOMPOSISI_TARGET[target]   # bertingkat
        JIKA tidak semua M0-M7 selesai: KUNCI tombol rakit
        LAIN: rakit_sisi_server(modul, konteks)     # hanya hasil akhir ke klien

## Bagian 3 — Lima Rekomendasi (R1-R3 diterapkan)
1. Pemandu alur berbasis tujuan (R1) - diterapkan.
2. Indikator status & validasi prasyarat M0-M7 (R2) - diterapkan.
3. Ringkasan konteks sebelum merakit (R3) - diterapkan.
4. Peringatan kombinasi tidak lazim (R4) - dilewati (berisiko menghakimi).
5. Ekspor pilihan & riwayat sesi (R5) - ditunda (berlebihan untuk sekarang).

## Bagian 4 — Ringkasan Peningkatan v9.1 vs v9.0
- ARAS dengan alur terpandu penuh; modul ditentukan tujuan; sumber per bidang;
  komposisi M10 bertingkat; modul tujuan terkunci hingga fondasi selesai.
- Integritas tetap utuh; isi prompt inti tidak berubah.

## Bagian 5 — Verifikasi
- 8/8 uji unit lulus (pemetaan tujuan, kunci sumber, jenjang otomatis, core +
  sumber, komposisi M10 internasional & SINTA, daftar target, core tak kosong).
- Uji aplikasi Streamlit: login -> Beranda -> ganti Tujuan mengubah kontrol
  (Target Publikasi muncul untuk M10); tombol rakit TERKUNCI sebelum M0-M7
  selesai dan AKTIF setelahnya; perakitan menghasilkan prompt akhir berisi Core
  Layer tanpa galat.
