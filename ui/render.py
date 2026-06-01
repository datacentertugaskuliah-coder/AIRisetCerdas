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


def sidebar_modules(st, current_id: str) -> str:
    """Sidebar daftar Modul 0-16 (gaya v8.11): pilih modul langsung.

    Kembalikan id modul terpilih. Dikelompokkan sesuai grup di config.MODULES.
    """
    st.sidebar.markdown("### Daftar Modul")
    grup: dict[str, list] = {}
    for mid, judul, sub, g in config.MODULES:
        grup.setdefault(g, []).append((mid, judul, sub))

    label_to_id: dict[str, str] = {}
    semua_label: list[str] = []
    for g, items in grup.items():
        for mid, judul, sub in items:
            label = f"{judul} — {sub}"
            label_to_id[label] = mid
            semua_label.append(label)

    # Tentukan indeks awal sesuai modul aktif.
    id_to_label = {v: k for k, v in label_to_id.items()}
    idx = semua_label.index(id_to_label.get(current_id, semua_label[0])) \
        if current_id in id_to_label else 0

    pilih = st.sidebar.radio("Pilih modul", semua_label, index=idx,
                             label_visibility="collapsed")
    return label_to_id[pilih]


def beranda_pintasan(st, ctx) -> str | None:
    """Beranda: Bidang + (opsional) pintasan Tujuan -> modul. Gaya v8.11 plus.

    Kembalikan module_id jika pengguna memakai pintasan Tujuan, selain itu None.
    """
    st.markdown("#### 🏠 Beranda — Dashboard & Panduan")
    c1, c2 = st.columns(2)
    with c1:
        ctx.bidang = st.selectbox(
            "Bidang Ilmu", config.FIELDS,
            index=config.FIELDS.index(ctx.bidang) if ctx.bidang in config.FIELDS else 0)
    with c2:
        opsi = ["— pilih modul dari sidebar —"] + config.TUJUAN
        pilih = st.selectbox("Pintasan Tujuan (opsional)", opsi, index=0)

    st.caption(
        f"Sumber data terkunci per bidang: **{config.sumber_data_label(ctx.bidang)}**. "
        "Pilih modul langsung dari sidebar kiri, atau pakai Pintasan Tujuan untuk "
        "melompat ke modul yang sesuai."
    )
    if pilih != "— pilih modul dari sidebar —":
        ctx.tujuan = pilih
        return config.TUJUAN_KE_MODUL.get(pilih)
    return None


def target_control(st, ctx, module_id: str = "") -> None:
    """Untuk M10 (Publikasi): pilih jenis publikasi + target + komposisi.

    Bila M10 dipilih dari sidebar (tujuan belum tentu Publikasi), tampilkan
    pemilih jenis publikasi lebih dulu.
    """
    if module_id != "m10":
        ctx.target = ""
        return

    if ctx.tujuan not in ("Publikasi Internasional", "Publikasi SINTA"):
        jenis_pub = st.selectbox("Jenis Publikasi",
                                 ["Publikasi Internasional", "Publikasi SINTA"],
                                 key="aras_jenis_pub")
        ctx.tujuan = jenis_pub
    else:
        # Izinkan pengguna mengganti jenis publikasi walau sudah terset.
        opsi = ["Publikasi Internasional", "Publikasi SINTA"]
        jenis_pub = st.selectbox("Jenis Publikasi", opsi,
                                 index=opsi.index(ctx.tujuan),
                                 key="aras_jenis_pub")
        ctx.tujuan = jenis_pub

    targets = config.target_untuk_tujuan(ctx.tujuan)
    if not targets:
        ctx.target = ""
        return
    ctx.target = st.selectbox("Target Publikasi", targets, key="aras_target_pub")
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
