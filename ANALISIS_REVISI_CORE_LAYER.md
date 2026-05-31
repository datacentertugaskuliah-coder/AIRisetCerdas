# Analisis Revisi Core Layer — ALAS v8.2 → v8.3 (Modul 12: Proposal BRIN RIIM Kompetisi)

Dokumen ini berisi analisis logis dan komprehensif untuk penambahan Modul 12
(Proposal BRIN RIIM Kompetisi), disertai konsep algoritma dan pseudocode, lalu
lima rekomendasi inti yang diwujudkan ke Core Layer. Prinsip: pertahankan yang
sudah baik, perbaiki yang lemah, kembangkan yang berpotensi. Tanpa halusinasi,
tanpa data palsu, integritas dijaga.

## Bagian 1 — Analisis Logis

### 1.1 Yang dipertahankan (tidak direvisi)
1. Modul 0-11 beserta struktur dan aturannya.
2. Anti-halusinasi (E), Firewall (K), pengungkapan AI (O.2), PUBEI (C),
   Gaya Natural (P), protokol kanvas baru per segmen.
3. Login ACCESS_KEY dan Core Layer tersembunyi.

### 1.2 Penambahan (Modul 12 — RIIM Kompetisi)
- Melanjutkan Modul 0-7, lalu sumber Modul 8 (rencana dataset) atau Modul 9
  (rancangan analisis), untuk menyusun proposal BRIN skema RIIM Kompetisi.
- Workflow bertahap: konfirmasi novelty di awal, lalu bab disusun lurus sesuai
  pedoman BRIN; tersedia fallback "langsung saja" untuk lintas-AI.
- Struktur khas RIIM: Kerangka Berpikir dan Nilai Strategis (bukan Pendahuluan
  gaya BIMA), Metode, Indikator Kinerja Riset, TKT 3-6, Jadwal maksimal 3 tahun,
  RAB, Daftar Pustaka APA.

### 1.3 Keputusan etis dan kejujuran (konsisten)
- Anti-deteksi AI TIDAK diterapkan (langgar K dan O.2; klaim tak terjamin).
- Semua angka (kata, dana, RAB, TKT, masa, pagu, peringkat jurnal) ditandai
  "[verifikasi pedoman BRIN — pendanaan-risnov.brin.go.id]".
- DOI hanya dari korpus; jika ragu "[DOI perlu verifikasi di doi.org]".
- Indikator kinerja, gerbang administratif, dan pemetaan TKT dibingkai sebagai
  alat bantu/pengingat, BUKAN jaminan kelolosan.

## Bagian 2 — Konsep Algoritma dan Pseudocode

### 2.1 Workflow bertahap RIIM
    ALGORITMA workflow_M12:
        PRA: Modul 0-7 selesai; sumber := Modul 8 ATAU Modul 9
        LANGKAH 0: tarik gap (M4) + korpus (M1), tampilkan untuk dikoreksi  [R1]
        LANGKAH 1: usulkan novelty dari gap; tanya konfirmasi user
                   fallback: jika user "langsung saja" -> pakai novelty usulan
                   ditandai "[novelty usulan — mohon ditinjau]"
        LANGKAH 2: susun bab berurutan (tanpa cek-balik novelty per bab)
        LANGKAH 3: gerbang kualitas + gerbang administratif + kanvas per segmen

### 2.2 Metode bercabang bidang + novelty
    JIKA bidang DALAM {Saintek, Ilmu Komputer}:
        desain model + algoritma flowchart (ASCII), novelty putus-putus berwarna
        jumlah novelty: 1 jika 1 tahun, 2 jika multiyear (maks 3 tahun)
    LAIN (Umum, Soshum): empat metode populer

### 2.3 Uji silang kelayakan
    untuk tiap tahapan metode: pastikan ADA luaran dan ADA pos RAB terkait  [R9]
    TKT: nyatakan awal -> target (rentang 3-6) dengan justifikasi realistis [R6]

## Bagian 3 — Lima Rekomendasi Inti (diwujudkan)
1. Lembar tarik-data M4 (gap) + M1 (korpus) di awal untuk dikoreksi.        [R1]
2. Tabel Indikator Kinerja Riset (IKR) per tahun (KTI + HKI).               [R2]
3. Pemandu Nilai Strategis berbasis pertanyaan + tema fokus BRIN.       [R3,R7]
4. RAB pos standar yang sinkron dengan metode + uji silang.             [R4,R9]
5. Gerbang Kesiapan Administratif (S3, rekam jejak, maks 2 proposal, CV).   [R5]

Rekomendasi pendukung yang juga diterapkan: pemetaan TKT awal->target [R6],
susunan tim periset [R8], ringkasan disusun terakhir [R10], validasi referensi
mutakhir 5 tahun [R11], mitigasi risiko riset [R13].

## Bagian 4 — Ringkasan Peningkatan v8.3 vs v8.2
- Modul baru: Modul 12 (Proposal BRIN RIIM Kompetisi); 14 modul total.
- Workflow bertahap dengan konfirmasi novelty + fallback lintas-AI.
- Struktur khas RIIM, IKR per tahun, TKT 3-6, RAB sinkron metode, APA.
- Integritas tetap utuh; tidak ada klaim berlebih atau data palsu.
