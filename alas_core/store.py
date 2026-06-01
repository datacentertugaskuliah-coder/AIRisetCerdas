"""Penyimpan prompt sisi-server.

Memuat Lapisan Inti (Core Layer) dan template modul dari berkas data lokal.
Modul ini HANYA dijalankan di server. Isi mentah tidak pernah dikembalikan ke
klien; lihat assembler.assemble() yang hanya mengembalikan hasil akhir.
"""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

_DATA = Path(__file__).resolve().parent / "data" / "prompts.json"


@lru_cache(maxsize=1)
def _load() -> dict:
    with open(_DATA, encoding="utf-8") as fh:
        return json.load(fh)


def core_layer() -> str:
    """Kembalikan teks Lapisan Inti (server-only)."""
    return _load()["prompts"]["core"]


def opener() -> str:
    """Kembalikan teks pembuka injeksi konteks (server-only)."""
    return _load()["prompts"].get("opener", "")


def module_prompt(module_id: str) -> str:
    """Kembalikan template prompt sebuah modul (server-only)."""
    prompts = _load()["prompts"]
    if module_id not in prompts:
        raise KeyError(f"Modul tidak dikenal: {module_id}")
    return prompts[module_id]


def schemes() -> list[dict]:
    return _load().get("schemes", [])


def m8_schemes() -> list[dict]:
    return _load().get("m8_schemes", [])


def has_module(module_id: str) -> bool:
    return module_id in _load()["prompts"]
