"""Komponen tampilan ARAS — hibrida Streamlit + sebagian HTML.

Alur terpandu berbasis tujuan (R1), indikator status prasyarat (R2), dan
ringkasan konteks sebelum merakit (R3). Tidak memuat isi Lapisan Inti.
"""
from __future__ import annotations

from alas_core import config


def header_html(version: str) -> str:
    return f"""
    <div style="display:flex;align-items:center;gap:12px;
                padding:14px 18px;border-radius:14px;
                background:linear-gradient(135deg,#0c2340,#15406b);color:#fff">
      <div style="width:40px;height:40px;border-radius:10px;background:#fff;
                  color:#0c2340;font-weight:700;display:flex;
                  align-items:center;justify-content:center">AR</div>
      <div>
        <div style="font-weight:700;font-size:18px">ARAS — Asisten Riset Akademik System</div>
        <div style="font-size:12px;opacity:.85">
          v{version} · 16 Seksi A-P · alur terpandu berbasis tujuan ·
          Core Layer di server (tersembunyi)
        </div>
      </div>
    </div>
    """


def beranda_controls(st, ctx) -> None:
    """Beranda: pilih Bidang + Tujuan; Jenjang/Skema terisi otomatis (Opsi 2)."""
    st.markdown("#### 🏠 Beranda — Dashboard & Panduan")
    c1, c2 = st.columns(2)
    with c1:
        ctx.bidang = st.selectbox(
            "Bidang Ilmu", config.FIELDS,
            index=config.FIELDS.index(ctx.bidang) if ctx.bidang in config.FIELDS else 0)
    with c2:
        ctx.tujuan = st.selectbox(
            "Tujuan", config.TUJUAN,
            index=config.TUJUAN.index(ctx.tujuan) if ctx.tujuan in config.TUJUAN else 0)

    # Jenjang/Skema otomatis (read-only).
    st.text_input("Jenjang / Skema (otomatis dari Tujuan)",
                  value=ctx.jenjang, disabled=True)

    # Sumber data dikunci per bidang.
    st.caption(
        f"Sumber data terkunci per bidang: **{config.sumber_data_label(ctx.bidang)}** "
        f"({'Saintek/Ilmu Komputer' if ctx.sumber_modul=='m8' else 'Umum/Sosial-Humaniora'}). "
        f"Modul tujuan: **{config.TUJUAN_KE_MODUL.get(ctx.tujuan,'-').upper()}**."
    )


def target_control(st, ctx) -> None:
    """Untuk M10 (Publikasi): pilih target Scopus/SINTA + tampilkan komposisi."""
    targets = config.target_untuk_tujuan(ctx.tujuan)
    if not targets:
        ctx.target = ""
        return
    ctx.target = st.selectbox("Target Publikasi", targets)
    komp = config.komposisi(ctx.target)
    if komp:
        intl, sinta, catatan = komp
        st.info(f"Komposisi sumber untuk **{ctx.target}**: {intl} + {sinta}. {catatan}.")


def topic_and_specifics(st, ctx, module_id: str) -> None:
    if module_id in config.NEEDS_TOPIC:
        ctx.topic = st.text_input("Topik Penelitian", value=ctx.topic,
                                  placeholder="mis. literasi digital guru sekolah dasar")
    if module_id in ("m13", "m14", "m15"):
        nama = {"m13": "Skripsi", "m14": "Tesis", "m15": "Disertasi"}[module_id]
        ctx.stage = st.selectbox(
            f"Tahap {nama}",
            ["Tahap 1 - Seminar Proposal (Bab 1-3)",
             "Tahap 2 - Seminar Hasil (Bab 1-5)"])
        ctx.jenis = st.selectbox("Jenis Penelitian",
                                 ["Kuantitatif", "Kualitatif", "Pengembangan (R&D)"])
    if module_id in ("m11", "m12"):
        ctx.period = st.selectbox("Masa Penelitian",
                                  ["1 tahun", "multiyear (2-3 tahun)"])
    if module_id == "m12":
        ctx.theme = st.text_input("Tema Fokus BRIN (referensi)",
                                  placeholder="pangan; kesehatan; energi; ...")


def prasyarat_note(st) -> None:
    """Gaya v8.11: prasyarat M0-M7 sebagai PENGINGAT, bukan penguncian UI.

    Urutan dijaga oleh blok PEMERIKSAAN PRA-KONDISI di dalam prompt yang dibaca
    AI tujuan (ChatGPT/Claude/dll), bukan dikunci oleh dashboard.
    """
    st.markdown("##### Prasyarat — selesaikan Modul 0 sampai Modul 7 dulu")
    st.info(
        "Sebelum modul tujuan, pastikan Modul 0 sampai Modul 7 telah dijalankan "
        "secara berurutan, lalu pilih Modul 8 (Dataset) untuk Sains/Ilmu Komputer "
        "atau Modul 9 (Statistik) untuk Umum/Sosial-Humaniora.\n\n"
        "Catatan: penjagaan urutan dilakukan oleh blok PEMERIKSAAN PRA-KONDISI di "
        "dalam prompt yang dibaca AI tujuan — sesuai gaya v8.11. Jika prasyarat "
        "belum terpenuhi, AI akan berhenti dan meminta Anda melengkapinya."
    )


def ringkasan_konteks(st, ctx, module_id: str) -> None:
    """R3: ringkasan pilihan sebelum merakit."""
    bits = [
        f"Bidang: **{ctx.bidang}**",
        f"Tujuan: **{ctx.tujuan}**",
        f"Modul: **{module_id.upper()}**",
        f"Sumber: **{config.sumber_data_label(ctx.bidang)}**",
    ]
    if ctx.target:
        bits.append(f"Target: **{ctx.target}**")
    if ctx.stage:
        bits.append(f"Tahap: **{ctx.stage.split(' - ')[0]}**")
    st.markdown("Ringkasan: " + " · ".join(bits))
