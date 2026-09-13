# finalproject-system-recommendation-webtoon

# 📚 Sistem Rekomendasi Webtoon

Aplikasi sistem rekomendasi komik Webtoon interaktif berbasis web. Dibuat menggunakan pendekatan **Content-Based Filtering** dengan ekstraksi fitur **TF-IDF Vectorizer** dan pengukuran kemiripan **Cosine Similarity**, lalu dideploy menggunakan **Streamlit**.

---

## 🎯 Masalah & Solusi

- **Masalah:** Pembaca sering mengalami *information overload* saat memilih komik baru. Selain itu, algoritma rekomendasi umum (*Collaborative Filtering*) sering gagal merekomendasikan komik baru karena belum ada data rating/ulasan pengguna (**Item Cold-Start Problem**).
- **Solusi:** Pendekatan *Content-Based Filtering* mengekstraksi kemiripan teks dari **genre** dan **sinopsis cerita**, sehingga komik yang baru dirilis tetap dapat direkomendasikan secara akurat berdasarkan substansi narasi.

---
## Dataset
https://www.kaggle.com/datasets/victorsoeiro/webtoons-dataset

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
```

## ⚙️ Cara Menjalankan Proyek Secara Lokal
- **1. Clone Repositori**
``git clone https://github.com/RevaNia12/finalproject-system-recommendation-webtoon.git
  cd finalproject-system-recommendation-webtoon
``
- **2. Buat & Aktifkan Virtual Environment**
    ***windows***
    ``python -m venv venv
      venv\Scripts\activate``
    ***macOS dan Linux***
    ``python3 -m venv venv
     source venv/bin/activate``
- **3. Install Dependensi**
``pip install -r requirements.txt``
- **4.Jalankan aplikasi streamlit**
``streamlit run app.py``

## Link Streamlit
https://finalproject-system-recommendation-webtoon-eyjkgebjz3ob4xbvdyh.streamlit.app/

