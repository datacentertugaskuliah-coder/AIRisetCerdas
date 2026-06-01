# ANALISIS REVISI CORE LAYER — ARAS (v8.11 → v9.1)

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
