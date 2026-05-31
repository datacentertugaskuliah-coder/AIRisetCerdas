# Analisis Revisi Core Layer — ALAS v8.5 → v8.6 (Aturan Sitasi Bab 2 Modul 13)

Dokumen ini berisi analisis logis untuk revisi terfokus pada aturan sumber
sitasi Bab 2 Modul 13 (Proposal Skripsi), disertai pseudocode dan lima
rekomendasi. Prinsip: pertahankan yang sudah baik, perbaiki yang lemah. Tanpa
halusinasi, tanpa data palsu, integritas dijaga.

## Bagian 1 — Analisis Logis

### 1.1 Yang dipertahankan (tidak direvisi)
Seluruh struktur Modul 13 (dua tahap, Bab 1-5, percabangan bidang/jenis, benang
merah rumusan masalah, gerbang per tahap), modul lain, Core Layer, login
ACCESS_KEY, Seksi P, protokol kanvas per bab.

### 1.2 Penambahan (aturan sitasi Bab 2)
- Komposisi sumber: MINIMAL 70% jurnal terindeks SINTA (1-5), MAKSIMAL 30%
  jurnal internasional bereputasi (Scopus Q3, Q4, atau IEEE). Fleksibel selama
  70/30 terjaga.
- Utamakan jurnal OPEN ACCESS; sertakan DOI dan tautan akses bila tersedia.
- Penanda jenis sumber ringkas, mis. "[SINTA 2, open access]".

### 1.3 Tegangan yang diselesaikan (kejujuran)
Permintaan "DOI valid + open access" bertabrakan dengan kenyataan bahwa AI tidak
dapat menjamin keaktifan DOI maupun status open access. Memerintahkan "DOI valid"
secara membabi buta justru mendorong fabrikasi DOI. Solusi: DOI/tautan HANYA dari
korpus Modul 1; jika ragu ditandai "[DOI perlu verifikasi di doi.org]" dan
"[tautan akses perlu diverifikasi]". JANGAN mengarang DOI, tautan, peringkat
SINTA, atau status open access. Verifikasi akhir di tangan penulis.

### 1.4 Keputusan etis (konsisten)
Anti-deteksi AI TIDAK diterapkan. Tidak ada sumber/DOI/peringkat fabrikasi.

## Bagian 2 — Pseudocode
    ALGORITMA sumber_bab2(korpus_M1):
        target := { SINTA: ">=70%", internasional_Q3Q4_IEEE: "<=30%" }
        UNTUK setiap sumber DALAM korpus_M1:
            klasifikaslikan: SINTA(1-5) atau internasional(Q3/Q4/IEEE)
            tandai open access bila diketahui dari korpus
            JIKA DOI/tautan ada di korpus -> cantumkan (https://doi.org/[DOI])
            LAIN -> tandai "[DOI perlu verifikasi di doi.org]"
        JIKA komposisi belum 70/30:
            tandai "[perlu tambahan sumber sesuai komposisi]"  # jangan mengarang
        JANGAN mengarang DOI/tautan/peringkat/status open access

## Bagian 3 — Lima Rekomendasi (diterapkan)
1. Komposisi 70% SINTA (1-5) / 30% internasional (Q3/Q4/IEEE), fleksibel.
2. Utamakan open access; sertakan DOI dan tautan bila dari korpus.
3. Anti-fabrikasi tegas: DOI/tautan/peringkat/status open access tidak dikarang;
   ditandai verifikasi bila ragu.
4. Penanda jenis sumber ringkas per entri (mis. "[SINTA 2, open access]").
5. Gerbang komposisi sumber Bab 2 + butir cek tahap (T1-6) sebelum lanjut.

## Bagian 4 — Ringkasan Peningkatan v8.6 vs v8.5
- Bab 2 Modul 13 kini punya aturan komposisi sumber 70/30 dan utamakan open
  access, dengan anti-fabrikasi DOI/tautan/peringkat yang tegas.
- Struktur lain Modul 13 tidak diubah.
- Integritas tetap utuh; tidak ada klaim berlebih atau data palsu.
