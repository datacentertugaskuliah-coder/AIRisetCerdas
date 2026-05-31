# Analisis Revisi Core Layer — ALAS v8.6 → v8.7 (Selektor Bidang Ilmu di Halaman Modul 13)

Dokumen ini berisi analisis logis untuk peningkatan akses pemilihan bidang ilmu
pada Modul 13 (Proposal Skripsi), disertai pseudocode dan lima rekomendasi.
Prinsip: pertahankan yang sudah baik, perbaiki yang lemah. Tanpa halusinasi,
tanpa data palsu, integritas dijaga.

## Bagian 1 — Analisis Logis

### 1.1 Temuan awal (jujur)
Pemilihan bidang ilmu (Umum, Sosial dan Humaniora, Sains dan Teknologi, Ilmu
Komputer) SUDAH ADA sebagai parameter global sejak v7.0, dan Modul 13 SUDAH
membacanya untuk mencabangkan Metode Bab 3 (JALUR MODEL vs JALUR SOSHUM).
Maka revisi ini BUKAN menambah fitur yang hilang, melainkan MENINGKATKAN AKSES:
menaruh selektor bidang langsung di halaman Modul 13.

### 1.2 Kelemahan yang diperbaiki
- C1: Selektor bidang hanya ada di Beranda; pengguna yang langsung membuka
  Modul 13 harus kembali ke Beranda untuk menggantinya. Tidak praktis.
- C2: Perubahan bidang sebelumnya hanya me-render ulang Beranda, bukan halaman
  modul yang sedang dibuka.

### 1.3 Yang dipertahankan (tidak diubah)
Seluruh substansi Modul 13 (dua tahap, Bab 1-5, aturan sumber Bab 2 70/30 SINTA,
benang merah rumusan masalah, gerbang per tahap), modul lain, Core Layer, login
ACCESS_KEY, Seksi P, protokol kanvas per bab.

### 1.4 Keputusan etis (konsisten)
Anti-deteksi AI TIDAK diterapkan. Tidak ada data/DOI fabrikasi.

## Bagian 2 — Pseudocode
    ALGORITMA pilih_bidang_di_modul:
        tampilkan selektor bidang di halaman Modul 13 (nilai = CTX.bidang global)
        KETIKA pengguna mengubah bidang:
            CTX.bidang := nilai baru ; simpan
            JIKA halaman saat ini = modul -> render ulang halaman modul
            perbarui badge konteks
        # bidang yang sama dipakai konsisten lintas modul dan saat menyalin

## Bagian 3 — Lima Rekomendasi (diterapkan)
1. Selektor bidang ilmu langsung di halaman Modul 13.
2. Perubahan bidang me-render ulang halaman modul yang sedang dibuka (live).
3. Nilai bidang tetap sinkron dengan parameter global (tidak ada duplikasi state).
4. Catatan percabangan Metode (MODEL/SOSHUM) tampil mengikuti bidang terpilih.
5. Konsistensi: bidang yang dipilih ikut tersalin ke prompt (sudah ada, dijaga).

## Bagian 4 — Ringkasan Peningkatan v8.7 vs v8.6
- Modul 13 kini punya selektor bidang ilmu di halaman, dengan render ulang live.
- Tidak ada perubahan substansi; hanya akses dan kenyamanan pemilihan bidang.
- Integritas tetap utuh; tidak ada klaim berlebih atau data palsu.
