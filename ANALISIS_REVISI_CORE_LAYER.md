# Analisis Revisi Core Layer — ALAS v8.7 → v8.8 (Modul 14: Proposal Tesis S2)

Dokumen ini berisi analisis logis untuk penambahan Modul 14 (Proposal Tesis S2),
disertai pseudocode dan lima rekomendasi (R1-R5). Prinsip: pertahankan yang
sudah baik, perbaiki yang lemah, kembangkan yang berpotensi. Tanpa halusinasi,
tanpa data palsu, integritas dijaga.

## Bagian 1 — Analisis Logis

### 1.1 Yang dipertahankan (tidak direvisi)
1. Modul 0-13 beserta struktur dan aturannya.
2. Anti-halusinasi (E), Firewall (K), pengungkapan AI (O.2), PUBEI (C),
   Gaya Natural (P), protokol kanvas baru per bab, selektor bidang di halaman.
3. Login ACCESS_KEY dan Core Layer tersembunyi.

### 1.2 Penambahan (Modul 14 — Tesis S2)
Modul 14 paralel dengan Modul 13 (dua tahap, Bab 1-5, pertanyaan literatur di
Bab 2, selektor bidang di halaman), tetapi WAJIB berbeda dari skripsi S1 melalui
lima pembeda jenjang:
- R1: Bab 2 menghasilkan kerangka konseptual + hipotesis (kuantitatif) atau
  proposisi (kualitatif).
- R2: posisi kebaruan/state of the art eksplisit terhadap penelitian terdahulu.
- R3: metodologi tingkat S2 (justifikasi pemilihan metode, definisi operasional,
  rigor lebih ketat), tetap bercabang bidang dan jenis penelitian.
- R4: manfaat memisahkan kontribusi teoretis (ditonjolkan) dan praktis.
- R5: sumber Bab 2 = 80% internasional (Q2/Q3/Q4/IEEE) + 20% SINTA 1-2,
  utamakan open access, kemutakhiran 5-10 tahun, dominasi sumber primer.

### 1.3 Keputusan etis dan kejujuran (konsisten)
- Anti-deteksi AI TIDAK diterapkan (langgar K dan O.2; klaim tak terjamin).
- Angka hasil ditandai "[isi dari hasil penelitian Anda]"; standar kampus
  ditandai "[sesuaikan panduan kampus]".
- DOI, tautan, peringkat SINTA, status open access TIDAK dikarang; yang ragu
  ditandai "[DOI perlu verifikasi di doi.org]". AI tidak menjamin keaktifan DOI.
- Gerbang kelengkapan dan mutu rujukan adalah alat bantu, BUKAN jaminan lulus.

## Bagian 2 — Pseudocode
    ALGORITMA workflow_M14(tahap, bidang, jenis):
        PRA: Modul 0-7 selesai; sumber := Modul 8 ATAU Modul 9
        JIKA tahap = 1: keluarkan Bab 1-3 (3 kanvas)
        JIKA tahap = 2: keluarkan Bab 1-5 (5 kanvas)
        Bab 2: uraikan teori -> SINTESIS kerangka konseptual + hipotesis/proposisi
               sumber: 80% internasional (Q2-Q4/IEEE) + 20% SINTA 1-2
               utamakan open access, mutakhir 5-10 tahun, primer
               DOI dari korpus; jika ragu tandai verifikasi (tidak mengarang)
        Bab 3: justifikasi metode + definisi operasional (rigor S2); cabang
               bidang (MODEL/SOSHUM) dan jenis (Kuanti/Kuali/R&D)
        manfaat: kontribusi teoretis (utama) + praktis
        rumusan masalah -> Bab 4 -> Bab 5 (benang merah); glosarium konsisten
        gerbang kelengkapan per tahap + gerbang mutu rujukan S2

## Bagian 3 — Lima Rekomendasi (diterapkan)
1. Kerangka konseptual + hipotesis/proposisi sebagai output Bab 2.
2. Posisi kebaruan/state of the art eksplisit.
3. Metodologi tingkat S2 (justifikasi, definisi operasional, rigor).
4. Kontribusi teoretis dan praktis dipisah tegas (teoretis ditonjolkan).
5. Mutu rujukan S2: 80/20 internasional-SINTA, open access, mutakhir, primer.

## Bagian 4 — Ringkasan Peningkatan v8.8 vs v8.7
- Modul baru: Modul 14 (Proposal Tesis S2); 16 modul total.
- Pembeda jenjang S2 yang jelas (kerangka konseptual, hipotesis, novelty,
  kontribusi teoretis, rujukan internasional) — bukan skripsi yang diperbesar.
- Integritas tetap utuh; tidak ada klaim berlebih atau data palsu.
