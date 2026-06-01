"""Konfigurasi ARAS: bidang ilmu, tujuan, pemetaan modul, dan aturan alur.

Tidak memuat isi Lapisan Inti. Aman untuk dirujuk lapisan UI.
"""
from __future__ import annotations

APP_NAME = "ARAS — Asisten Riset Akademik System"

FIELDS = ["Umum", "Sosial dan Humaniora", "Sains dan Teknologi", "Ilmu Komputer"]

TUJUAN = [
    "Skripsi", "Tesis", "Disertasi", "Hibah BIMA", "BRIN",
    "Publikasi Internasional", "Publikasi SINTA", "Laporan Penelitian",
]

TUJUAN_KE_MODUL = {
    "Skripsi": "m13", "Tesis": "m14", "Disertasi": "m15",
    "Hibah BIMA": "m11", "BRIN": "m12",
    "Publikasi Internasional": "m10", "Publikasi SINTA": "m10",
    "Laporan Penelitian": "m16",
}

TUJUAN_KE_JENJANG = {
    "Skripsi": "Skripsi (S1)", "Tesis": "Tesis (S2)", "Disertasi": "Disertasi (S3)",
    "Hibah BIMA": "Hibah BIMA", "BRIN": "Hibah BRIN RIIM",
    "Publikasi Internasional": "Artikel Jurnal Internasional",
    "Publikasi SINTA": "Artikel Jurnal Nasional (SINTA)",
    "Laporan Penelitian": "Laporan Penelitian",
}

TARGET_INTERNASIONAL = ["Scopus Q1", "Scopus Q2", "Scopus Q3", "Scopus Q4"]
TARGET_SINTA = ["SINTA 1", "SINTA 2", "SINTA 3", "SINTA 4"]

KOMPOSISI_TARGET = {
    "Scopus Q1": ("90% internasional (Q1 diutamakan)", "10% SINTA 1-2",
                  "standar tertinggi; kemutakhiran 5 tahun; sumber primer"),
    "Scopus Q2": ("80% internasional (Q1/Q2)", "20% SINTA 1-2",
                  "kemutakhiran 5-7 tahun"),
    "Scopus Q3": ("70% internasional (Q2/Q3)", "30% SINTA 1-2",
                  "kemutakhiran 5-10 tahun"),
    "Scopus Q4": ("60% internasional (Q3/Q4/IEEE)", "40% SINTA 1-3",
                  "kemutakhiran 5-10 tahun"),
    "SINTA 1": ("30% internasional (Q3/Q4)", "70% SINTA 1-2",
                "dominan nasional bereputasi"),
    "SINTA 2": ("20% internasional (Q4/IEEE)", "80% SINTA 1-3",
                "dominan nasional bereputasi"),
    "SINTA 3": ("10% internasional", "90% SINTA 1-4", "mayoritas nasional"),
    "SINTA 4": ("0-10% internasional", "90-100% SINTA 1-5", "dominan SINTA"),
}

FONDASI = ["m0", "m1", "m2", "m3", "m4", "m5", "m6", "m7"]

MODULES = [
    ("m0", "Modul 0", "Pencarian Literatur", "Fondasi"),
    ("m1", "Modul 1", "Protokol Intake", "Fondasi"),
    ("m2", "Modul 2", "Pencari Kontradiksi", "Fondasi"),
    ("m3", "Modul 3", "Rantai Sitasi", "Fondasi"),
    ("m4", "Modul 4", "Pemindai Kesenjangan", "Fondasi"),
    ("m5", "Modul 5", "Audit Metodologi", "Fondasi"),
    ("m6", "Modul 6", "10 Rekomendasi Judul", "Fondasi"),
    ("m7", "Modul 7", "Hibah & Publikasi", "Fondasi"),
    ("m8", "Modul 8", "Rekomendasi Dataset", "Sumber Data"),
    ("m9", "Modul 9", "Statistik Multivariat", "Sumber Data"),
    ("m10", "Modul 10", "Draft Artikel IMRAD", "Tujuan: Publikasi"),
    ("m11", "Modul 11", "Proposal Hibah BIMA", "Tujuan: Hibah"),
    ("m12", "Modul 12", "Proposal BRIN RIIM", "Tujuan: Hibah"),
    ("m13", "Modul 13", "Proposal Skripsi", "Tujuan: Akademik"),
    ("m14", "Modul 14", "Proposal Tesis S2", "Tujuan: Akademik"),
    ("m15", "Modul 15", "Proposal Disertasi S3", "Tujuan: Akademik"),
    ("m16", "Modul 16", "Laporan Penelitian", "Tujuan: Laporan"),
]

NEEDS_TOPIC = {"m6", "m7", "m8", "m9", "m10", "m11", "m12", "m13", "m14", "m15", "m16"}
NEEDS_FIELD = {"m10", "m13", "m14", "m15", "m16"}


def jalur_metode(bidang: str) -> str:
    if bidang in ("Sains dan Teknologi", "Ilmu Komputer"):
        return "JALUR MODEL"
    return "JALUR SOSHUM"


def sumber_data_untuk(bidang: str) -> str:
    if bidang in ("Sains dan Teknologi", "Ilmu Komputer"):
        return "m8"
    return "m9"


def sumber_data_label(bidang: str) -> str:
    mid = sumber_data_untuk(bidang)
    return "Modul 8 (Dataset)" if mid == "m8" else "Modul 9 (Statistik)"


def target_untuk_tujuan(tujuan: str) -> list:
    if tujuan == "Publikasi Internasional":
        return list(TARGET_INTERNASIONAL)
    if tujuan == "Publikasi SINTA":
        return list(TARGET_SINTA)
    return []


def komposisi(target: str):
    return KOMPOSISI_TARGET.get(target)
