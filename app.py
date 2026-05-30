"""
ALAS v7.0 — Asisten Riset Akademik
(c) 2024-2026 Alhumaira Store | obrolanpintar1987@gmail.com

Pembungkus Streamlit untuk dashboard ALAS v7.0. Memuat satu berkas
dashboard.html dan menampilkannya penuh. Core Layer disimpan sebagai data
tersembunyi dan tetap ikut tersalin saat pengguna menekan "Salin Prompt".
"""
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="ALAS v7.0 - Asisten Riset Akademik",
    page_icon="\U0001F4DA",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        "About": (
            "ALAS v7.0 - Asisten Riset Akademik\n"
            "16 Seksi (A-P) - 12 Modul - Core Layer Tersembunyi\n"
            "(c) 2024-2026 Alhumaira Store\n"
            "obrolanpintar1987@gmail.com"
        )
    },
)

st.markdown(
    """<style>
#MainMenu, header, footer,
[data-testid="stHeader"], [data-testid="stToolbar"],
[data-testid="stDecoration"], .stDeployButton {
  display: none !important; visibility: hidden !important;
}
.main .block-container { padding: 0 !important; margin: 0 !important; max-width: 100% !important; }
.main { padding: 0 !important; }
html, body { margin: 0 !important; padding: 0 !important; overflow-x: hidden; }
iframe { width: 100% !important; border: none !important; display: block !important; }
</style>""",
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "dashboard.html"
if not html_path.exists():
    st.error("Berkas dashboard.html tidak ditemukan.")
    st.stop()

components.html(html_path.read_text(encoding="utf-8"), height=5400, scrolling=True)
