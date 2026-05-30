# Analisis Revisi Core Layer — ALAS v6.0 → v7.0

Dokumen ini berisi analisis logis dan komprehensif untuk rombak ALAS v7.0,
disertai konsep algoritma dan *pseudocode* sebagai dasar *brainstorming*,
lalu lima rekomendasi perbaikan yang seluruhnya diwujudkan dalam Core Layer v7.0.

Prinsip: pertahankan yang sudah baik, perbaiki yang lemah, kembangkan yang
berpotensi. Tanpa halusinasi, tanpa data palsu, integritas dijaga.

---

## Bagian 1 — Analisis Logis

### 1.1 Yang dipertahankan (tidak direvisi karena sudah kuat)
1. Sistem penanda epistemik 6 level (Seksi B.4) — fondasi anti-halusinasi.
2. Aturan data tidak ada → nyatakan eksplisit (Seksi E.2).
3. Aturan integritas kuantitas — dilarang fabrikasi demi target (Seksi E.3).
4. Firewall Integritas Akademik (Seksi K) — 4 batas tak dapat dilanggar.
5. Pengungkapan AI sesuai kebijakan jurnal (Seksi O.2).
6. Protokol PUBEI (Seksi C) dan Gerbang Kualitas (Seksi G).
7. Seksi P (Gaya Penulisan Natural) dari v6.0 — dipertahankan dan diperkuat.

### 1.2 Perubahan yang diminta (semua terverifikasi dampaknya)
| Kode | Perubahan | Dampak logis |
|------|-----------|--------------|
| C1 | Penataan ulang modul: 8=Dataset, 9=Statistik, 10=IMRAD | Dependensi & registri Seksi H, G.2 harus ikut diperbarui |
| C2 | Pilihan bidang ilmu eksplisit (Umum, Soshum, Saintek, Ilmu Komputer) | Mesin Konteks Seksi L parameter 1 |
| C3 | Fokus jenjang & hibah (Skripsi, Tesis, Disertasi, BIMA, BRIN) | Mesin Konteks Seksi L parameter 2 & 3, daftar skema |
| C4 | Judul aplikasi → "ALAS — Asisten Riset Akademik" | Branding di seluruh berkas |
| C5 | Versi → v7.0 | Konsistensi versi |

### 1.3 Keputusan etis (ditegakkan konsisten)
Permintaan "anti-deteksi AI detector / menyamar manusia" TIDAK diimplementasikan.
Alasan: bertentangan dengan Seksi K dan O.2 (nilai inti ALAS), dan klaim
"tidak terdeteksi" tak dapat dijamin sehingga menanamnya = klaim palsu.
Gantinya: Seksi P (gaya natural sah) tetap dipakai.

---

## Bagian 2 — Konsep Algoritma & Pseudocode

### 2.1 Penataan ulang modul (inti permintaan C1)
Pemetaan lama → baru, isi ikut pindah:
```
  Dataset      : M9_lama  -> M8_baru
  Statistik    : M10_lama -> M9_baru
  IMRAD        : M8_lama  -> M10_baru
```
```
ALGORITMA petakan_ulang_modul:
    peta := { 'm8':'m10', 'm9':'m8', 'm10':'m9' }   # sumber -> tujuan
    UNTUK setiap (lama, baru) DALAM peta:
        konten_baru[baru] := konten_lama[lama]
    # perbarui rujukan internal nomor modul di teks
    UNTUK setiap konten:
        ganti "Modul 8" (IMRAD)    -> "Modul 10"
        ganti "Modul 9" (Dataset)  -> "Modul 8"
        ganti "Modul 10" (Statistik)-> "Modul 9"
    perbarui registri Seksi H dan urutan dependensi Seksi G.2/H.4
    VERIFIKASI: tidak ada nomor modul yatim atau rujukan silang yang salah
```
Justifikasi: rotasi 3-siklus. Karena IMRAD (penulisan artikel) kini jadi modul
terakhir (10), urutan kerja jadi lebih logis: cari data (8) → analisis statistik
(9) → tulis artikel (10).

### 2.2 Pemilihan bidang ilmu & kalibrasi (C2, C3)
```
ALGORITMA kalibrasi_konteks(bidang, jenjang, target):
    JIKA bidang == "Ilmu Komputer":
        eligibilitas_M9_statistik := TIDAK   # statistik multivariat tak wajib
        sarankan := "cross-validation / benchmark ML"
    LAIN:
        eligibilitas_M9_statistik := YA
    novelty_min := { Skripsi:1, Tesis:2, Disertasi:3, Hibah:2 }[jenjang]
    skema := pilih_skema(target)   # PDP/PFR/Terapan/Prototipe/BRIN/Scopus/SINTA
    KEMBALIKAN profil_konteks
```

### 2.3 Core Layer tersembunyi (tetap dipertahankan dari v6.0)
```
ALGORITMA core_tersembunyi:
    simpan core sebagai DATA (bukan teks terlihat)
    render UI -> dashboard ringkas
    KETIKA "Salin": teks := injeksi_konteks + core + prompt_modul
    # core ikut tersalin meski tak tampil
```

### 2.4 Gaya natural sah (Seksi P, dipertahankan)
```
ALGORITMA gaya_natural(teks):
    variasikan panjang kalimat; hindari klise; PUBEI aktif
    tanda baca hanya: . , ; : - ? ! " " ' ' ( ) [ ] / ...
    JANGAN klaim "bukan AI" atau "lolos detektor"   # dilarang
    pertahankan semua penanda epistemik
```

---

## Bagian 3 — Lima Rekomendasi Perbaikan

### Rekomendasi 1 — Penataan ulang modul yang konsisten
Tukar nomor beserta isi (8=Dataset, 9=Statistik, 10=IMRAD), perbarui seluruh
rujukan silang dan registri. Status: DITERAPKAN.

### Rekomendasi 2 — Pemilih bidang ilmu eksplisit di Beranda
Empat bidang (Umum, Soshum, Saintek, Ilmu Komputer) sebagai parameter pertama
Mesin Konteks, dengan aturan eligibilitas modul statistik. Status: DITERAPKAN.

### Rekomendasi 3 — Fokus jenjang & hibah yang jelas
Skripsi, Tesis, Disertasi + skema BIMA (PDP, PFR, Terapan Model, Prototipe) dan
BRIN tampil sebagai pilihan terstruktur. Status: DITERAPKAN.

### Rekomendasi 4 — Dashboard interaktif + visualisasi alur baru
Beranda menampilkan ringkasan pengembangan dan diagram alur 12 modul dengan
urutan baru, mudah dipahami lintas latar. Status: DITERAPKAN.

### Rekomendasi 5 — Core Layer tersembunyi + Seksi P diperkuat, versi v7.0
Core Layer tetap berjalan di balik layar; Seksi P dipertahankan; seluruh berkas
diseragamkan ke v7.0. Status: DITERAPKAN.

---

## Bagian 4 — Ringkasan Peningkatan v7.0 vs v6.0
- Penomoran modul: 8=Dataset, 9=Statistik, 10=IMRAD (urutan kerja lebih logis).
- Pemilih bidang ilmu & jenjang/hibah eksplisit di Beranda.
- Judul: "ALAS — Asisten Riset Akademik".
- Versi seragam v7.0; integritas (Seksi E, K, O.2, P) tetap utuh.
- Tidak ada fitur yang diklaim melebihi implementasi nyata.
