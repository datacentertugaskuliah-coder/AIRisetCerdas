"""ARAS — Asisten Riset Akademik System (entry Streamlit, server-side core).

(c) 2024-2026 Alhumaira Store. Hak cipta dilindungi.

Alur terpandu berbasis tujuan: pengguna memilih Bidang + Tujuan di Beranda;
Jenjang/Skema dan modul terisi otomatis. Modul tujuan terkunci hingga modul
fondasi M0-M7 ditandai selesai. Lapisan Inti dirakit di server; hanya hasil
akhir yang dikirim ke klien.
"""
from __future__ import annotations

import streamlit as st

from alas_core import __version__, assembler, auth, config
from ui import render

st.set_page_config(page_title="ARAS — Asisten Riset Akademik System",
                   page_icon="AR", layout="wide")


def _load_ctx() -> assembler.Context:
    ctx = assembler.Context()
    for k, v in st.session_state.get("aras_ctx", {}).items():
        setattr(ctx, k, v)
    return ctx


def _save_ctx(ctx: assembler.Context) -> None:
    st.session_state["aras_ctx"] = {
        "bidang": ctx.bidang, "tujuan": ctx.tujuan, "target": ctx.target,
        "topic": ctx.topic, "stage": ctx.stage, "jenis": ctx.jenis,
        "period": ctx.period, "theme": ctx.theme,
    }


def main() -> None:
    if not auth.gate(st):
        return

    st.markdown(render.header_html(__version__), unsafe_allow_html=True)
    st.write("")

    ctx = _load_ctx()

    # Beranda: bidang + pintasan tujuan opsional.
    pintasan_id = render.beranda_pintasan(st, ctx)

    # Sidebar daftar modul (gaya v8.11) = pemilih utama.
    # Jika pengguna memakai pintasan Tujuan, jadikan modul itu yang aktif.
    aktif = pintasan_id or st.session_state.get("aras_module_id", "m0")
    module_id = render.sidebar_modules(st, aktif)
    st.session_state["aras_module_id"] = module_id
    # Selaraskan tujuan dengan modul yang dipilih (untuk konteks jenjang).
    # Untuk M10, JANGAN paksa tujuan (biar pengguna pilih jenis publikasi sendiri).
    if module_id != "m10":
        for tj, mid in config.TUJUAN_KE_MODUL.items():
            if mid == module_id:
                ctx.tujuan = tj
                break

    st.divider()
    # Gaya v8.11: prasyarat M0-M7 sebagai PENGINGAT (bukan penguncian UI).
    render.prasyarat_note(st)

    st.divider()
    meta = next((m for m in config.MODULES if m[0] == module_id), None)
    if meta:
        st.subheader(f"{meta[1]} — {meta[2]}")

    # Target khusus M10 (Publikasi Internasional/SINTA).
    render.target_control(st, ctx, module_id)
    # Topik + spesifik modul.
    render.topic_and_specifics(st, ctx, module_id)

    _save_ctx(ctx)

    st.divider()
    render.ringkasan_konteks(st, ctx, module_id)

    if st.button("Rakit & Salin Prompt (+ Core Layer)", type="primary"):
        final_prompt = assembler.assemble(module_id, ctx)
        st.caption("Prompt akhir (Core Layer dirakit di server dan ikut):")
        st.code(final_prompt, language="markdown")
        st.download_button("Unduh prompt (.txt)", final_prompt,
                           file_name=f"aras_{module_id}.txt")


if __name__ == "__main__":
    main()
