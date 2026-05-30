"""
ALAS v8.0 — Asisten Riset Akademik
(c) 2024-2026 Alhumaira Store | obrolanpintar1987@gmail.com

Pembungkus Streamlit untuk dashboard ALAS v8.0 dengan gerbang login berbasis
ACCESS_KEY yang disimpan di Streamlit Cloud Secrets Manager.

Catatan keamanan:
- Kunci akses TIDAK pernah disimpan di kode atau repositori; hanya dibaca dari
  st.secrets (Secrets Manager).
- Dashboard (dashboard.html) baru dikirim ke browser SETELAH kunci benar.
- Perbandingan kunci memakai hmac.compare_digest (tahan serangan timing).
- Ada pembatasan jumlah percobaan per sesi untuk mengurangi tebakan beruntun.
"""
import hmac
import time
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="ALAS v8.0 - Asisten Riset Akademik",
    page_icon="\U0001F4DA",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        "About": (
            "ALAS v8.0 - Asisten Riset Akademik\n"
            "16 Seksi (A-P) - 12 Modul - Core Layer Tersembunyi\n"
            "(c) 2024-2026 Alhumaira Store\n"
            "obrolanpintar1987@gmail.com"
        )
    },
)

MAX_ATTEMPTS = 5          # batas percobaan per sesi
LOCK_SECONDS = 60         # jeda kunci setelah batas tercapai


def _get_secret_key() -> str:
    """Ambil ACCESS_KEY dari Secrets Manager. Kosong jika belum diatur."""
    try:
        return str(st.secrets["ACCESS_KEY"])
    except Exception:
        return ""


def _login_styles() -> None:
    st.markdown(
        """<style>
        #MainMenu, header, [data-testid="stToolbar"], [data-testid="stDecoration"],
        .stDeployButton { display:none !important; visibility:hidden !important; }
        .block-container { max-width: 460px; padding-top: 8vh; }
        .alas-card {
            background:#fffdf8; border:1px solid #ddd6c7; border-radius:16px;
            padding:30px 28px; box-shadow:0 8px 30px rgba(21,19,15,.08);
        }
        .alas-logo {
            width:54px; height:54px; border-radius:12px; background:#13314f;
            color:#f3ecd6; display:flex; align-items:center; justify-content:center;
            font-weight:700; font-size:22px; font-family:Georgia,serif;
            letter-spacing:1px; margin-bottom:16px;
        }
        .alas-title { font-family:Georgia,serif; font-size:24px; font-weight:700;
            color:#15130f; margin:0 0 4px; }
        .alas-sub { font-size:13px; color:#7c766a; margin-bottom:6px;
            font-family:ui-monospace,monospace; }
        </style>""",
        unsafe_allow_html=True,
    )


def _render_login() -> None:
    _login_styles()
    secret_key = _get_secret_key()

    st.markdown(
        '<div class="alas-card">'
        '<div class="alas-logo">AL</div>'
        '<div class="alas-title">ALAS v8.0</div>'
        '<div class="alas-sub">Asisten Riset Akademik &middot; Akses Terbatas</div>',
        unsafe_allow_html=True,
    )

    if not secret_key:
        st.error(
            "ACCESS_KEY belum diatur di Secrets Manager. "
            "Tambahkan terlebih dahulu melalui menu Settings -> Secrets "
            "pada aplikasi Streamlit Cloud Anda."
        )
        st.markdown("</div>", unsafe_allow_html=True)
        st.stop()

    # Status kunci percobaan
    locked_until = st.session_state.get("locked_until", 0)
    now = time.time()
    if now < locked_until:
        sisa = int(locked_until - now)
        st.warning(f"Terlalu banyak percobaan. Coba lagi dalam {sisa} detik.")
        st.markdown("</div>", unsafe_allow_html=True)
        st.stop()

    with st.form("login_form", clear_on_submit=False):
        key_input = st.text_input("Kunci Akses", type="password",
                                  placeholder="Masukkan kunci akses")
        submitted = st.form_submit_button("Masuk", use_container_width=True)

    if submitted:
        attempts = st.session_state.get("attempts", 0)
        # Perbandingan tahan-timing
        if hmac.compare_digest(key_input or "", secret_key):
            st.session_state["authenticated"] = True
            st.session_state["attempts"] = 0
            st.rerun()
        else:
            attempts += 1
            st.session_state["attempts"] = attempts
            if attempts >= MAX_ATTEMPTS:
                st.session_state["locked_until"] = time.time() + LOCK_SECONDS
                st.error(f"Kunci salah {attempts} kali. Dikunci {LOCK_SECONDS} detik.")
            else:
                sisa = MAX_ATTEMPTS - attempts
                st.error(f"Kunci akses salah. Sisa percobaan: {sisa}.")

    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()


def _render_app() -> None:
    st.markdown(
        """<style>
        #MainMenu, header, footer,
        [data-testid="stHeader"], [data-testid="stToolbar"],
        [data-testid="stDecoration"], .stDeployButton {
          display:none !important; visibility:hidden !important;
        }
        .main .block-container { padding:0 !important; margin:0 !important; max-width:100% !important; }
        .main { padding:0 !important; }
        html, body { margin:0 !important; padding:0 !important; overflow-x:hidden; }
        iframe { width:100% !important; border:none !important; display:block !important; }
        </style>""",
        unsafe_allow_html=True,
    )

    html_path = Path(__file__).parent / "dashboard.html"
    if not html_path.exists():
        st.error("Berkas dashboard.html tidak ditemukan.")
        st.stop()

    # Dashboard hanya dikirim ke browser setelah login berhasil.
    components.html(html_path.read_text(encoding="utf-8"), height=5400, scrolling=True)


# ----- Alur utama -----
if not st.session_state.get("authenticated", False):
    _render_login()
else:
    _render_app()
