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

    # Beranda: bidang + tujuan (jenjang otomatis).
    render.beranda_controls(st, ctx)
    module_id = ctx.module_id

    st.divider()
    # R2: prasyarat fondasi M0-M7.
    siap = render.prasyarat_status(st, st.session_state)

    st.divider()
    meta = next((m for m in config.MODULES if m[0] == module_id), None)
    if meta:
        st.subheader(f"Modul Tujuan: {meta[1]} — {meta[2]}")

    # Target khusus M10 (Publikasi Internasional/SINTA).
    render.target_control(st, ctx)
    # Topik + spesifik modul.
    render.topic_and_specifics(st, ctx, module_id)

    _save_ctx(ctx)

    st.divider()
    render.ringkasan_konteks(st, ctx, module_id)  # R3

    if not siap:
        st.button("Rakit & Salin Prompt (+ Core Layer)", disabled=True)
        st.caption("Tombol terkunci sampai Modul 0-7 ditandai selesai.")
        return

    if st.button("Rakit & Salin Prompt (+ Core Layer)", type="primary"):
        final_prompt = assembler.assemble(module_id, ctx)
        st.caption("Prompt akhir (Core Layer dirakit di server dan ikut):")
        st.code(final_prompt, language="markdown")
        st.download_button("Unduh prompt (.txt)", final_prompt,
                           file_name=f"aras_{module_id}.txt")


if __name__ == "__main__":
    main()
