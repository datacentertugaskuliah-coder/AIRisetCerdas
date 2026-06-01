"""Uji perakitan prompt ARAS (alur berbasis tujuan)."""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from alas_core import assembler, config, store  # noqa: E402


def test_goal_maps_to_module():
    assert config.TUJUAN_KE_MODUL["Skripsi"] == "m13"
    assert config.TUJUAN_KE_MODUL["Tesis"] == "m14"
    assert config.TUJUAN_KE_MODUL["Disertasi"] == "m15"
    assert config.TUJUAN_KE_MODUL["Hibah BIMA"] == "m11"
    assert config.TUJUAN_KE_MODUL["BRIN"] == "m12"
    assert config.TUJUAN_KE_MODUL["Publikasi Internasional"] == "m10"
    assert config.TUJUAN_KE_MODUL["Publikasi SINTA"] == "m10"
    assert config.TUJUAN_KE_MODUL["Laporan Penelitian"] == "m16"


def test_source_locked_by_field():
    assert config.sumber_data_untuk("Sains dan Teknologi") == "m8"
    assert config.sumber_data_untuk("Ilmu Komputer") == "m8"
    assert config.sumber_data_untuk("Umum") == "m9"
    assert config.sumber_data_untuk("Sosial dan Humaniora") == "m9"


def test_context_module_and_jenjang():
    ctx = assembler.Context(tujuan="Tesis", bidang="Umum", topic="x")
    assert ctx.module_id == "m14"
    assert "Tesis" in ctx.jenjang
    assert ctx.sumber_modul == "m9"


def test_assemble_has_core_and_source():
    ctx = assembler.Context(tujuan="Skripsi", bidang="Ilmu Komputer", topic="uji")
    out = assembler.assemble(ctx.module_id, ctx)
    assert "Core Layer" in out or "LAPISAN INTI" in out
    assert "Modul 8 (Dataset)" in out      # bidang Ilkom -> M8
    assert "JALUR MODEL" in out


def test_m10_target_composition_internasional():
    ctx = assembler.Context(tujuan="Publikasi Internasional", bidang="Umum",
                            topic="x", target="Scopus Q1")
    out = assembler.assemble("m10", ctx)
    assert "90% internasional" in out
    assert "Scopus Q1" in out


def test_m10_target_composition_sinta():
    ctx = assembler.Context(tujuan="Publikasi SINTA", bidang="Umum",
                            topic="x", target="SINTA 4")
    out = assembler.assemble("m10", ctx)
    assert "SINTA 4" in out
    assert "dominan SINTA" in out


def test_target_lists():
    assert config.target_untuk_tujuan("Publikasi Internasional") == \
        ["Scopus Q1", "Scopus Q2", "Scopus Q3", "Scopus Q4"]
    assert config.target_untuk_tujuan("Publikasi SINTA") == \
        ["SINTA 1", "SINTA 2", "SINTA 3", "SINTA 4"]
    assert config.target_untuk_tujuan("Skripsi") == []


def test_core_layer_not_empty():
    assert len(store.core_layer()) > 1000


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    passed = 0
    for fn in fns:
        fn(); passed += 1; print(f"OK  {fn.__name__}")
    print(f"\n{passed}/{len(fns)} tes lulus.")
