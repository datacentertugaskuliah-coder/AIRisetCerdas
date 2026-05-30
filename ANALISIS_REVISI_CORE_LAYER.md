# Analisis Revisi Core Layer — ALAS v7.0 → v8.0 (Fokus Modul 10 IMRAD)

Dokumen ini berisi analisis logis dan komprehensif untuk revisi Modul 10
(Draft Artikel IMRAD), disertai konsep algoritma dan *pseudocode* sebagai dasar
*brainstorming*, lalu lima rekomendasi perbaikan yang diwujudkan ke Core Layer.

Prinsip: pertahankan yang sudah baik, perbaiki yang lemah, kembangkan yang
berpotensi. Tanpa halusinasi, tanpa data palsu, integritas dijaga.

---

## Bagian 1 — Analisis Logis

### 1.1 Yang dipertahankan (tidak direvisi)
1. Penanda epistemik 6 level (Seksi B.4) dan anti-halusinasi (Seksi E).
2. Firewall Integritas (Seksi K) dan pengungkapan AI (Seksi O.2).
3. PUBEI (Seksi C), Gerbang Kualitas (Seksi G), Seksi P (Gaya Natural).
4. Penomoran modul v7.0: M8=Dataset, M9=Statistik, M10=IMRAD.

### 1.2 Permintaan baru untuk Modul 10 (semua dipetakan ke aturan)
| Kode | Permintaan | Penanganan |
|------|-----------|-----------|
| R1 | M10 melanjutkan M0-7 lalu M8 ATAU M9 | Logika percabangan input |
| R2 | Dua skema: Scopus Q1 / SINTA 2 | Parameter bahasa & gaya |
| R3 | Tiap bagian IMRAD = 750 kata, 3 sub-heading, paragraf penuh | Struktur tetap |
| R4 | 6 pertanyaan literatur (Inggris) di paragraf akhir tiap bagian | Penutup tiap bagian |
| R5 | Methods Saintek/Ilkom: flowchart algoritma + 2 novelty (lingkaran putus-putus) | Cabang metode A |
| R6 | Methods Umum/Soshum: 4 metode populer (Kuanti, Kuali, Humaniora, Mixed) | Cabang metode B |
| R7 | Results Saintek/Ilkom: tabel+grafik + Tabel Perbandingan penelitian sebelumnya | Cabang hasil A |
| R8 | Results Soshum: data empiris + disandingkan penelitian terdahulu | Cabang hasil B |
| R9 | Discussion menjawab I-M-R | Aturan isi |
| R10 | Conclusion 250 kata + angka kuantitatif | Bagian baru |
| R11 | Abstract 300 kata (bukan dari kesimpulan) | Bagian baru |
| R12 | 5 keyword satu suku kata, dipisah ";", general | Bagian baru |
| R13 | Rekomendasi judul standar Scopus Q1 | Bagian baru |
| R14 | Daftar pustaka APA, DOI aktif+link | Bagian baru + ANTI-FABRIKASI |

### 1.3 Keputusan etis (konsisten)
- "Anti-deteksi AI" TIDAK diterapkan (langgar Seksi K & O.2; klaim tak terjamin).
- DOI "aktif dan valid": AI tidak bisa menjamin keaktifan DOI. Maka Core Layer
  mewajibkan: DOI hanya dari korpus Modul 1; jika tidak yakin tulis
  "[DOI perlu verifikasi di doi.org]". Ini mencegah fabrikasi sitasi (Seksi K
  Batas 3) dan menjaga permintaan "tidak fake".

---

## Bagian 2 — Konsep Algoritma & Pseudocode

### 2.1 Percabangan input Modul 10 (R1)
```
ALGORITMA modul10_input:
    WAJIB: output Modul 1-7 tersedia
    JIKA user_pilih == "Modul 8 (Dataset)":
        sumber_data := hasil Modul 8
    LAIN JIKA user_pilih == "Modul 9 (Statistik)":
        sumber_data := hasil Modul 9
    LAIN:
        peringatkan "pilih Modul 8 atau 9 dulu"
    lanjut ke penulisan IMRAD dengan sumber_data
```

### 2.2 Percabangan Methods berdasar bidang (R5, R6)
```
ALGORITMA methods(bidang):
    JIKA bidang DALAM {Sains dan Teknologi, Ilmu Komputer}:
        tulis desain pengembangan model/metode
        sajikan FLOWCHART ALGORITMA (ASCII)
        tandai 2 bagian sebagai NOVELTY:
            gambar lingkaran putus-putus berwarna di luar box
    LAIN (Umum, Sosial dan Humaniora):
        sajikan 4 metode populer:
            1 Kuantitatif (kuesioner; Regresi/SEM; SPSS/SmartPLS/Path)
            2 Kualitatif (Etnografi/Fenomenologi; wawancara; observasi)
            3 Humaniora (studi teks; hermeneutika; analisis wacana kritis)
            4 Mixed Methods (gabung angka + narasi)
        user memilih sesuai tujuan kajian
```

### 2.3 Percabangan Results berdasar bidang (R7, R8)
```
ALGORITMA results(bidang):
    sajikan hasil dari Methods: tabel + grafik/gambar
    JIKA bidang DALAM {Saintek, Ilkom}:
        tambah TABEL PERBANDINGAN dengan penelitian sebelumnya
    LAIN (Soshum):
        sajikan data empiris (grafik, tabel dampak)
        sandingkan dengan penelitian terdahulu
        tunjukkan pergeseran konseptual + kontribusi teoritis
```

### 2.4 Struktur tiap bagian IMRAD (R3, R4)
```
ALGORITMA bagian_imrad(nama):
    target := 750 kata
    susun 3 sub-heading terstruktur, masing-masing paragraf penuh
    di paragraf TERAKHIR:
        tambah 6 pertanyaan literatur (bahasa Inggris)
        tujuan: memperkuat pembahasan bagian ini
```

### 2.5 Penutup artikel (R10-R14)
```
ALGORITMA penutup:
    conclusion := jawaban I-M-R-D + angka kuantitatif, 250 kata
    abstract := 300 kata, DISUSUN TERPISAH (bukan salinan kesimpulan)
    keywords := 5 kata (satu suku kata, general), pisah ";"
    judul_scopus := rekomendasi judul standar Scopus Q1
    daftar_pustaka := gaya APA; DOI hanya dari korpus + link;
                      jika ragu -> "[DOI perlu verifikasi di doi.org]"
```

---

## Bagian 3 — Lima Rekomendasi Perbaikan

### Rekomendasi 1 — Percabangan input & bidang yang eksplisit
Modul 10 membaca pilihan M8/M9 dan bidang ilmu untuk menentukan isi Methods
dan Results. Status: DITERAPKAN.

### Rekomendasi 2 — Struktur IMRAD 750 kata + 3 sub-heading + 6 pertanyaan
Tiap bagian seragam: 750 kata, tiga sub-heading paragraf penuh, enam pertanyaan
literatur bahasa Inggris di akhir. Status: DITERAPKAN.

### Rekomendasi 3 — Methods dua jalur (flowchart+novelty / 4 metode)
Saintek-Ilkom memakai flowchart algoritma dengan 2 novelty bertanda lingkaran
putus-putus; Umum-Soshum memakai 4 metode populer. Status: DITERAPKAN.

### Rekomendasi 4 — Penutup lengkap (Conclusion, Abstract, Keywords, Judul, Pustaka)
Conclusion 250 kata berangka, Abstract 300 kata terpisah, 5 keyword general,
rekomendasi judul Scopus Q1, daftar pustaka APA. Status: DITERAPKAN.

### Rekomendasi 5 — Aturan anti-fabrikasi DOI (jujur)
DOI hanya dari korpus; jika ragu ditandai untuk verifikasi manual. Menjaga
integritas sitasi (Seksi K). Status: DITERAPKAN.

---

## Bagian 4 — Ringkasan Peningkatan v8.0 vs v7.0
- Modul 10 ditulis ulang penuh sesuai 14 spesifikasi (R1-R14).
- Methods & Results bercabang otomatis menurut bidang ilmu.
- Penutup lengkap dengan abstrak terpisah dan pustaka APA anti-fabrikasi.
- Integritas (Seksi E, K, O.2, P) tetap utuh; tidak ada klaim berlebih.
