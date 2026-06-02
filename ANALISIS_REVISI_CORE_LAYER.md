# ANALISIS REVISI CORE LAYER — ARAS (v8.11 → v9.4)

(c) 2024-2026 Alhumaira Store · obrolanpintar1987@gmail.com
Catatan internal; tidak dirender ke pengguna.

## 1. Diagnosis
Core Layer lama berupa aturan datar, sekali jalan, tanpa gerbang. Pada skala
besar (10 judul) muncul risiko drift konteks, inkonsistensi C→D→E→F, dan
halusinasi sitasi/dataset.

## 2. Dipertahankan (invarian)
Anti-halusinasi, firewall integritas, penandaan "[verifikasi]", pengungkapan AI,
gaya natural, dan sifat tersembunyi Core Layer.

## 3. Pseudocode pipeline v9.1
```
FUNCTION core_layer(intake, module):
    ctx = parse(intake)
    IF missing(ctx.bidang|ctx.skema|ctx.tujuan): RETURN minta_lengkapi()   # gerbang intake
    MCB = lock(ctx); MCB.novelty = (ctx.tujuan IN {bima,brin}) ? 2 : 1
    MCB.mode = (ctx.bidang IN {saintek,ilkom}) ? "eksperimental" : "naratif"
    payload = route(module, MCB)               # M0..M7 + cabang + terminal
    draft = LLM(payload + FIREWALL)
    ASSERT peneliti(D) SUBSET peneliti(C)       # gerbang konsistensi
    ASSERT tahapan(F) SUBSET simpul(E)
    ASSERT count(novelty) == MCB.novelty
    draft = naturalize(draft); keep(disclosure_AI)
    RETURN emit(draft, canvas="BARU", checkpoint=true)
```

## 4. Konsistensi: invarian vs parameter (Opsi B)
- Invarian (sama di semua jalur & sepanjang M0–M7): pipeline, firewall, gerbang,
  pengungkapan AI, gaya natural.
- Parameter (mengalir via MCB): cabang M8/M9 (bidang), mode outline (bidang),
  kedalaman (jenjang), terminal + standar Scopus/Sinta (tujuan), novelty (tujuan).
- M0–M7 memakai Core Layer yang sama; hanya M0 (basis data), M5 (jenis audit),
  dan M7 (mode desain + novelty) yang menyesuaikan isi. M1–M4 & M6 invarian.

## 5. Routing Beranda
Tujuan→terminal: skripsi→13, tesis→14, disertasi→15, bima→11, brin→12,
intl→10 (Scopus Q1–Q4), sinta→10 (Sinta 1–4), laporan→16.
Bidang→cabang: {saintek,ilkom}→M8; {umum,soshum}→M9.
Rail menampilkan M0–M7 saja; cabang + terminal tersimpan sebagai routing.

## 6. Tidak diimplementasikan
Fitur "lolos AI detector" tidak dibuat (bertentangan dengan integritas akademik
dan pengungkapan AI). Diganti peningkatan gaya natural yang etis.

## 7. Tambahan v9.2
- Blok penguat 77 kata (tanpa label) disisipkan sebelum CORE_LAYER pada semua
  prompt M0-M7 (juga cabang & terminal) untuk memperkuat integritas & gaya, tanpa
  menampakkan bahwa itu lapisan inti.
- M7 bagian C: sintesis 5 penelitian terdahulu (APA, DOI [verifikasi]) -> GAP ->
  posisi 1 "penelitian saat ini" yang menjawab GAP, disajikan sebagai kontribusi
  DIUSULKAN (bukan hasil/angka dikarang).
- M7 bagian D: novelty menjawab GAP, dengan TIPE per tingkat:
  S1 Application, S2 Improvement, S3 Invention; BIMA/BRIN tetap (kontribusi
  orisinal peta jalan, jumlah 2 multiyear). Default tingkat untuk non-gelar:
  Publikasi Internasional -> Improvement/Invention; Sinta -> Improvement;
  Laporan -> Application. Jumlah & tipe novelty adalah dua atribut terpisah.
- Tipe novelty masuk ke MCB ("Tipe novelty") agar konsisten di modul terminal.

## 8. Tambahan v9.3
- M0 dua mode: (1) Standar (default, bawaan ARAS) = prompt strategi pencarian;
  (2) Analisis Dokumen Manual = prompt yang memerintahkan mesin AI menganalisis
  hingga 10 PDF yang dilampirkan PENGGUNA di mesin AI. ARAS tidak menerima/
  memproses file (tanpa kotak unggah); pemicu ada di M0. M1-M7 tetap standar.
- Pengaman integritas mode-2: simpulkan hanya dari isi PDF; "[tidak ditemukan di
  dokumen]" bila tak ada; larangan sumber luar & fabrikasi; saran proses bertahap.

## 9. Tambahan v9.4 (sub-skema, terverifikasi dari sumber resmi)
- Pola sub-skema (yang sebelumnya hanya Scopus/Sinta) diperluas ke Hibah BIMA
  dan BRIN. Sub-skema masuk MCB ("Sub-skema/Tier") dan menyetel standar di prompt
  modul terminal (M10/M11/M12). Routing terminal TIDAK berubah.
- BIMA (DRTPM/Kemdiktisaintek), 6 skema relevan dosen: PDP, PDP Afirmasi,
  Penelitian Fundamental (Reguler), PKDN, Terapan-Luaran Model, Terapan-Luaran
  Prototipe. Sumber: pengumuman DRTPM/BIMA 2024-2025.
- BRIN (RIIM), Opsi 1 (stabil): RIIM Kompetisi, RIIM Ekspedisi, RIIM Invitasi,
  RIIM Kolaborasi, RIIM Start-Up. UI memberi catatan "sesuaikan panduan tahun
  berjalan" karena nama/jumlah skema berubah per tahun/batch (anti data basi).
- Scopus Q1-Q4 & Sinta 1-4 tetap. Tiap sub-skema mengubah standar penulisan,
  bukan sekadar label.
