# finalproject-system-recommendation-webtoon

# 📚 Sistem Rekomendasi Webtoon

Aplikasi sistem rekomendasi komik Webtoon interaktif berbasis web. Dibuat menggunakan pendekatan **Content-Based Filtering** dengan ekstraksi fitur **TF-IDF Vectorizer** dan pengukuran kemiripan **Cosine Similarity**, lalu dideploy menggunakan **Streamlit**.

---

## 🎯 Masalah & Solusi

- **Masalah:** Pembaca sering mengalami *information overload* saat memilih komik baru. Selain itu, algoritma rekomendasi umum (*Collaborative Filtering*) sering gagal merekomendasikan komik baru karena belum ada data rating/ulasan pengguna (**Item Cold-Start Problem**).
- **Solusi:** Pendekatan *Content-Based Filtering* mengekstraksi kemiripan teks dari **genre** dan **sinopsis cerita**, sehingga komik yang baru dirilis tetap dapat direkomendasikan secara akurat berdasarkan substansi narasi.

---

## 🛠️ Stack Teknologi

- **Pemrograman:** Python 3.x
- **Analisis Data & ML:** `pandas`, `numpy`, `scikit-learn` (`TfidfVectorizer`, `cosine_similarity`)
- **Web App:** `streamlit`

---

## 📁 Struktur Repositori

```text
├── app.py                   # Aplikasi web Streamlit
├── notebook_analysis.ipynb  # Notebook analisis data (EDA & Model)
├── data.csv                 # Dataset komik Webtoon
├── requirements.txt         # Dependencies Python
└── README.md                # Dokumentasi proyek

---

## 🎯 Masalah & Solusi
