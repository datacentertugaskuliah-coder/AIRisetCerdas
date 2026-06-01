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


def prasyarat_status(st, ss) -> bool:
    """R2: status fondasi M0-M7 BERTAHAP BERURUTAN dengan cascade reset.

    Aturan:
    - M0 aktif sejak awal; M(n) terkunci sampai M(n-1) selesai.
    - Membatalkan centang M(n) ikut membatalkan M(n+1)..M7 (cascade reset),
      agar status selalu konsisten dengan urutan.
    """
    st.markdown("##### Prasyarat — selesaikan Modul 0 sampai Modul 7 dulu (bertahap)")
    fondasi = config.FONDASI

    # Pra-pass: tegakkan aturan berurutan pada state widget (ss[f"fon_{m}"]).
    # Begitu menemukan modul yang belum dicentang, semua sesudahnya dipaksa False.
    putus = False
    for i, m in enumerate(fondasi):
        key = f"fon_{m}"
        if putus:
            # Prasyarat tidak terpenuhi -> paksa batal (cascade reset).
            if ss.get(key, False):
                ss[key] = False
        else:
            if not ss.get(key, False):
                putus = True  # mulai dari sini ke bawah terkunci/batal

    # Render checkbox dengan penguncian berurutan.
    cols = st.columns(4)
    done: dict[str, bool] = {}
    for i, m in enumerate(fondasi):
        key = f"fon_{m}"
        prasyarat_ok = all(done.get(fondasi[j], False) for j in range(i))
        with cols[i % 4]:
            val = st.checkbox(
                f"{m.upper()} selesai",
                key=key,
                disabled=not prasyarat_ok,
            )
        done[m] = bool(val) and prasyarat_ok

    ss["aras_fondasi_done"] = done

    semua = all(done.values())
    if semua:
        st.success("Semua modul fondasi (M0-M7) selesai berurutan. Modul tujuan aktif.")
    else:
        berikut = next((m.upper() for m in fondasi if not done[m]), None)
        st.warning(
            f"Modul tujuan masih TERKUNCI. Langkah berikutnya: selesaikan "
            f"{berikut}. (Modul setelahnya terkunci sampai {berikut} dicentang.)"
        )
    return semua


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
