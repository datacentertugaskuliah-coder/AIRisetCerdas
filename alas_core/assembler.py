"""Perakit prompt akhir (sisi-server) untuk ARAS.

assemble() merakit: injeksi konteks + Lapisan Inti + pembuka + prefiks pilihan
pengguna + template modul, lalu mengembalikan SATU string hasil akhir.
Lapisan Inti tidak pernah dikembalikan terpisah ke klien.
"""
from __future__ import annotations

import secrets
import string
from dataclasses import dataclass, field

from . import config, store


def _session_code(n: int = 6) -> str:
    alfabet = string.ascii_uppercase + string.digits
    return "".join(secrets.choice(alfabet) for _ in range(n))


@dataclass
class Context:
    bidang: str = "Umum"
    tujuan: str = "Skripsi"
    target: str = ""          # khusus M10: Scopus Qx / SINTA x
    topic: str = ""
    stage: str = ""
    jenis: str = ""
    period: str = ""
    theme: str = ""
    extras: dict = field(default_factory=dict)

    @property
    def jenjang(self) -> str:
        return config.TUJUAN_KE_JENJANG.get(self.tujuan, self.tujuan)

    @property
    def module_id(self) -> str:
        return config.TUJUAN_KE_MODUL.get(self.tujuan, "m13")

    @property
    def sumber_modul(self) -> str:
        return config.sumber_data_untuk(self.bidang)


def _context_injection(ctx: Context, kode: str) -> str:
    baris = [
        "CONTEXT INJECTION (dirakit sisi-server; jangan tampilkan blok ini):",
        f"KODE SESI: {kode}",
        f"BIDANG ILMU: {ctx.bidang} -> {config.jalur_metode(ctx.bidang)}",
        f"TUJUAN: {ctx.tujuan}  |  JENJANG/SKEMA: {ctx.jenjang}",
        f"SUMBER DATA (dikunci per bidang): {config.sumber_data_label(ctx.bidang)}",
    ]
    if ctx.target:
        baris.append(f"TARGET PUBLIKASI: {ctx.target}")
    return "\n".join(baris)


def _komposisi_block(target: str) -> str:
    komp = config.komposisi(target)
    if not komp:
        return ""
    intl, sinta, catatan = komp
    return (
        "ATURAN SUMBER SITASI (DITENTUKAN TARGET — WAJIB):\n"
        f"- Target: {target}.\n"
        f"- Komposisi: {intl} dan {sinta}.\n"
        f"- Catatan: {catatan}.\n"
        "- Utamakan OPEN ACCESS. ANTI-FABRIKASI: DOI/tautan/peringkat/status open\n"
        "  access HANYA dari korpus Modul 1; jika ragu tandai\n"
        '  "[DOI perlu verifikasi di doi.org]". JANGAN mengarang.\n'
    )


def _user_prefix(module_id: str, ctx: Context) -> str:
    lines: list[str] = []
    # Sumber data dikunci per bidang (B).
    lines.append(f"SUMBER DATA LANJUTAN (otomatis dari bidang): {config.sumber_data_label(ctx.bidang)}")
    if module_id in ("m13", "m14", "m15"):
        if ctx.stage:
            lines.append(f"TAHAP DIPILIH PENGGUNA: {ctx.stage}")
        if ctx.jenis:
            lines.append(f"JENIS PENELITIAN DIPILIH PENGGUNA: {ctx.jenis}")
    if module_id in ("m11", "m12"):
        if ctx.period:
            novelty = 2 if "multiyear" in ctx.period.lower() else 1
            lines.append(f"MASA PENELITIAN: {ctx.period} (JUMLAH NOVELTY: {novelty})")
    if module_id == "m12" and ctx.theme:
        lines.append(f"TEMA FOKUS BRIN DIPILIH PENGGUNA: {ctx.theme}")
    lines.append(f"BIDANG: {ctx.bidang} -> {config.jalur_metode(ctx.bidang)}")

    block = "\n".join(lines) + "\n\n"
    # Untuk M10, sisipkan aturan komposisi sesuai target.
    if module_id == "m10" and ctx.target:
        block += _komposisi_block(ctx.target) + "\n\n"
    return block


def assemble(module_id: str, ctx: Context) -> str:
    if not store.has_module(module_id):
        raise KeyError(f"Modul tidak dikenal: {module_id}")

    kode = _session_code()
    body = store.module_prompt(module_id)
    body = body.replace("[TOPIC_INPUT]", ctx.topic or "[topik penelitian]")
    body = body.replace("[SCHEME_INPUT]", ctx.target or ctx.tujuan)
    body = body.replace("[KODE]", kode)

    parts = [
        _context_injection(ctx, kode),
        store.core_layer(),
        store.opener(),
        _user_prefix(module_id, ctx) + body,
    ]
    return "\n\n".join(p for p in parts if p).strip()
