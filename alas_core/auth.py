"""Gerbang akses berbasis ACCESS_KEY.

Membaca ACCESS_KEY dari Streamlit Secrets. Membandingkan dengan hmac.
Membatasi percobaan dan menerapkan penguncian sementara. Tidak menyimpan
kunci di kode; tidak mengirim Lapisan Inti sebelum lolos.
"""
from __future__ import annotations

import hmac
import time

MAX_ATTEMPTS = 5
LOCK_SECONDS = 60


def _expected_key() -> str | None:
    try:
        import streamlit as st
        return st.secrets.get("ACCESS_KEY")
    except Exception:
        return None


def verify(candidate: str) -> bool:
    expected = _expected_key()
    if not expected:
        return False
    return hmac.compare_digest(str(candidate), str(expected))


def gate(st) -> bool:
    """Render gerbang login. Kembalikan True jika sudah terautentikasi.

    Menggunakan session_state untuk menghitung percobaan dan penguncian.
    """
    ss = st.session_state
    if ss.get("alas_auth_ok"):
        return True

    if _expected_key() is None:
        st.error(
            "ACCESS_KEY belum diatur. Tambahkan di Settings -> Secrets:\n\n"
            'ACCESS_KEY = "kunci-rahasia-anda"'
        )
        return False

    locked_until = ss.get("alas_lock_until", 0)
    now = time.time()
    if now < locked_until:
        sisa = int(locked_until - now)
        st.warning(f"Terlalu banyak percobaan. Coba lagi dalam {sisa} detik.")
        return False

    st.title("ARAS — Asisten Riset Akademik System")
    st.caption("Masukkan kunci akses untuk melanjutkan.")
    key = st.text_input("Kunci Akses", type="password")
    if st.button("Masuk"):
        if verify(key):
            ss["alas_auth_ok"] = True
            ss["alas_attempts"] = 0
            st.rerun()
        else:
            ss["alas_attempts"] = ss.get("alas_attempts", 0) + 1
            sisa = MAX_ATTEMPTS - ss["alas_attempts"]
            if sisa <= 0:
                ss["alas_lock_until"] = now + LOCK_SECONDS
                ss["alas_attempts"] = 0
                st.error("Percobaan habis. Terkunci sementara 60 detik.")
            else:
                st.error(f"Kunci salah. Sisa percobaan: {sisa}.")
    return False
