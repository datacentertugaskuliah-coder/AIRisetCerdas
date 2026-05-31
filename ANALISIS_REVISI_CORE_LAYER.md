# Analisis Revisi Core Layer — ALAS v8.1 → v8.2 (Modul 11: Proposal Hibah BIMA)

Dokumen ini berisi analisis logis dan komprehensif untuk penambahan Modul 11
(Proposal Hibah BIMA), disertai konsep algoritma dan pseudocode, lalu lima
rekomendasi perbaikan yang diwujudkan ke Core Layer. Prinsip: pertahankan yang
sudah baik, perbaiki yang lemah, kembangkan yang berpotensi. Tanpa halusinasi,
tanpa data palsu, integritas dijaga.

## Bagian 1 — Analisis Logis

### 1.1 Yang dipertahankan (tidak direvisi)
1. Modul 0-10 beserta struktur dan aturannya.
2. Anti-halusinasi (E), Firewall (K), pengungkapan AI (O.2), PUBEI (C),
   Gaya Natural (P), protokol kanvas baru per segmen (warisan v8.1).
3. Login ACCESS_KEY dan Core Layer tersembunyi.

### 1.2 Penambahan (Modul 11)
- Modul 11 melanjutkan Modul 0-7, lalu memakai sumber Modul 8 (rencana dataset)
  atau Modul 9 (rancangan analisis), untuk menyusun proposal hibah BIMA.
- Empat sub-template: PDP, PFR (Penelitian Dasar); Terapan Luaran Model,
  Terapan Luaran Prototipe (Penelitian Terapan).
- Struktur PDP/PFR mengikuti template resmi yang diberikan pengguna.
- Struktur Terapan = struktur Dasar + Strategi Pencapaian TKT + Kemitraan wajib
  + luaran model/prototipe dan KI.

### 1.3 Keputusan etis dan kejujuran (konsisten)
- Anti-deteksi AI TIDAK diterapkan (langgar K dan O.2; klaim tak terjamin).
- Semua angka panduan (jumlah kata, dana, RAB, TKT, masa) ditandai
  "[verifikasi panduan BIMA terbaru — bima.kemdiktisaintek.go.id]".
- DOI hanya dari korpus; jika ragu "[DOI perlu verifikasi di doi.org]".
- Rubrik penilaian dipakai sebagai PENYELARAS kriteria, BUKAN jaminan lolos.
  Kelolosan tergantung kompetisi, kuota, rekam jejak, dan penilaian reviewer.

## Bagian 2 — Konsep Algoritma dan Pseudocode

### 2.1 Percabangan skema dan masa penelitian
    ALGORITMA modul11(skema, bidang, masa):
        WAJIB: Modul 0-7 selesai; sumber := Modul 8 ATAU Modul 9
        JIKA skema = PDP        -> masa = 1 tahun ; novelty = 1
        JIKA skema = PFR        -> masa = pilihan user (1/multiyear)
                                    novelty = 1 jika 1 tahun, 2 jika multiyear
        JIKA skema = Terapan    -> masa = pilihan user (umumnya multiyear)
                                    novelty = 1 jika 1 tahun, 2 jika multiyear
                                    aktifkan: Strategi Pencapaian TKT + Kemitraan
        [semua aturan masa/TKT ditandai verifikasi panduan BIMA]

### 2.2 Bobot rubrik per skema (penekanan penulisan)
    ALGORITMA bobot(skema):
        kembalikan tabel bobot (%) per butir sesuai kelompok:
            Dasar-PDP | Dasar-lain | Terapan
        instruksi: beri penekanan lebih pada butir berbobot tinggi
        catatan: bobot = penyelaras kriteria, bukan jaminan lolos

### 2.3 Metode dan flowchart bernovelty (bercabang bidang)
    ALGORITMA metode(bidang, jumlah_novelty):
        JIKA bidang DALAM {Saintek, Ilmu Komputer}:
            desain model + algoritma flowchart (ASCII)
            tandai jumlah_novelty bagian sebagai kebaruan:
                garis putus-putus berwarna di luar box
        LAIN (Umum, Soshum):
            sajikan 4 metode populer; pilih sesuai tujuan
        sertakan instruksi: AI tujuan boleh render visual bila platform mendukung

### 2.4 Roadmap fishbone 5 tahun
    tulang utama = garis waktu 5 tahun ; duri = capaian/luaran per tahun
    render ASCII + instruksi render visual bila platform mendukung

### 2.5 Pertanyaan literatur (alat kerja, bukan naskah submit)
    di akhir tiap komponen Pendahuluan: 5 pertanyaan (Inggris) dalam blok
    "[Pertanyaan Literatur — untuk pencarian referensi, hapus sebelum submit]"

## Bagian 3 — Lima Rekomendasi Perbaikan
1. Modul 11 empat sub-template sesuai template resmi + temuan terverifikasi.
2. Percabangan masa penelitian -> jumlah novelty (1/2), ikut skema dan bidang.
3. Bobot rubrik penilaian per skema sebagai penyelaras kriteria.
4. Strategi Pencapaian TKT + Kemitraan wajib untuk skema Terapan.
5. Semua angka panduan ditandai verifikasi; sitasi APA; DOI anti-fabrikasi.

## Bagian 4 — Ringkasan Peningkatan v8.2 vs v8.1
- Modul baru: Modul 11 (Proposal Hibah BIMA), 13 modul total (Core + M0-M11).
- Empat sub-template berbasis template resmi pengguna + temuan web terverifikasi.
- Bobot rubrik penilaian per skema sebagai penyelaras kriteria.
- Integritas tetap utuh; tidak ada klaim berlebih atau data palsu.
