# ALAS v7.0 — Asisten Riset Akademik

(c) 2024-2026 **Alhumaira Store** · obrolanpintar1987@gmail.com

Penyusun *prompt* akademik untuk peneliti Indonesia, dari skripsi hingga hibah
BIMA dan BRIN. Pilih bidang ilmu, jenjang, dan modul; salin ke asisten AI
pilihan Anda (ChatGPT, Claude, Gemini, dan lainnya).

## Apa yang baru di v7.0

- **Modul ditata ulang.** Urutan kerja kini lebih logis:
  Modul 8 = Rekomendasi Dataset, Modul 9 = Statistik Multivariat,
  Modul 10 = Draft Artikel IMRAD (langkah penulisan terakhir).
- **Pemilih bidang ilmu eksplisit.** Umum, Sosial dan Humaniora,
  Sains dan Teknologi, serta Ilmu Komputer. Untuk Ilmu Komputer, Modul 9
  (statistik multivariat) tidak diwajibkan dan sistem menyarankan kerangka
  evaluasi *machine learning*.
- **Fokus jenjang & hibah.** Skripsi, Tesis, Disertasi, Hibah BIMA
  (PDP, PFR, Terapan Model, Terapan Prototipe), dan BRIN.
- **Core Layer tersembunyi.** Fondasi 16 seksi (A-P) berjalan di balik layar
  dan tetap ikut tersalin saat Anda menekan "Salin Prompt".
- **Seksi P: Gaya Penulisan Natural.** Prosa luwes dan manusiawi dengan tanda
  baca rapi, tanpa mengorbankan integritas. Bukan alat anti-deteksi.

## Integritas

Core Layer mempertahankan Firewall Integritas (Seksi K), aturan anti-halusinasi
(Seksi E), dan pengungkapan AI (Seksi O.2). Setiap penggunaan AI tetap wajib
diungkapkan sesuai kebijakan jurnal target.

## Cara menjalankan secara lokal

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy ke Streamlit Cloud

1. Unggah seluruh isi folder ini ke repositori GitHub Anda.
2. Buka share.streamlit.io, pilih repositori, atur `app.py` sebagai berkas utama.
3. Klik Deploy.

## Kompatibel

Smartphone iOS/Android, tablet, dan laptop/desktop.

## Struktur berkas

```
ALAS-v7.0/
├── app.py                          Pembungkus Streamlit
├── dashboard.html                  Antarmuka + Core Layer tersembunyi
├── requirements.txt
├── ANALISIS_REVISI_CORE_LAYER.md   Analisis, pseudocode, 5 rekomendasi
├── .streamlit/config.toml
├── .gitignore
└── .gitattributes
```

## Login berbasis ACCESS_KEY (Streamlit Cloud Secrets Manager)

Aplikasi ini dilindungi gerbang login. Dashboard hanya dikirim ke browser
setelah kunci akses benar. Kunci TIDAK disimpan di kode atau repositori.

### Mengaktifkan di Streamlit Cloud

1. Buka aplikasi Anda di share.streamlit.io.
2. Klik menu kanan bawah (tiga titik) -> **Settings** -> **Secrets**.
3. Masukkan baris berikut, lalu **Save**:

   ```toml
   ACCESS_KEY = "kunci-rahasia-anda"
   ```

4. Aplikasi otomatis dimuat ulang. Halaman login akan meminta kunci tersebut.

### Menjalankan secara lokal

1. Salin `.streamlit/secrets.toml.example` menjadi `.streamlit/secrets.toml`.
2. Isi `ACCESS_KEY` dengan kunci Anda.
3. Jalankan `streamlit run app.py`.

Berkas `.streamlit/secrets.toml` sudah masuk `.gitignore` sehingga tidak ikut
ter-commit.

### Catatan keamanan (jujur)

- Login ini melindungi AKSES masuk. Setelah seseorang berhasil masuk, isi
  dashboard berada di browser mereka. Login mencegah orang masuk, bukan
  menyembunyikan isi dari orang yang sudah masuk.
- Perbandingan kunci memakai `hmac.compare_digest` (tahan serangan timing).
- Ada pembatasan 5 percobaan per sesi dengan jeda kunci 60 detik.
- Untuk keamanan lebih kuat (mis. banyak pengguna, peran berbeda), pertimbangkan
  autentikasi resmi seperti OIDC/SSO bawaan Streamlit, bukan satu kunci bersama.
