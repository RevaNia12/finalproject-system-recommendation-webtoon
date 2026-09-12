import re
import pandas as pd
import sklearn.feature_extraction.text
import sklearn.metrics.pairwise
import streamlit as st

#Cleaning teks
def bersihkan_teks(text):
  text = str(text).lower()
  text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
  return text


# Dashboard
st.set_page_config(
    page_title="Sistem Rekomendasi Webtoon", page_icon="📚", layout="wide"
)


# Perhitungan matriks
@st.cache_data
def load_data_and_compute():
  df = pd.read_csv('data.csv')

  # Handling missing values
  df['genre'] = df['genre'].fillna('')
  summary_col = (
      'summary'
      if 'summary' in df.columns
      else ('synopsis' if 'synopsis' in df.columns else 'genre')
  )
  df['summary_clean'] = df[summary_col].fillna('')

  df['text_features'] = df['genre'] + ' ' + df['summary_clean']

  df['text_clean'] = df['text_features'].apply(bersihkan_teks)

  # TF-IDF
  tfidf = sklearn.feature_extraction.text.TfidfVectorizer()
  tfidf_matrix = tfidf.fit_transform(df['text_clean'])

  cosine_sim = sklearn.metrics.pairwise.cosine_similarity(
      tfidf_matrix, tfidf_matrix
  )

  return df, cosine_sim

try:
  df, cosine_sim = load_data_and_compute()
  data_loaded = True
except Exception as e:
  st.error(f'Gagal membaca file data.csv: {e}')
  data_loaded = False


# Fungsi rekomendasi
def get_recommendations(selected_title, top_n=5):
  idx = df[df['title'] == selected_title].index[0]

  sim_scores = list(enumerate(cosine_sim[idx]))
  sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
  sim_scores = sim_scores[1 : top_n + 1]

  webtoon_indices = [i[0] for i in sim_scores]

  result = df.iloc[webtoon_indices].copy()
  result['similarity_score'] = [round(i[1], 3) for i in sim_scores]
  return result


# Streamlit
st.title('📚 Sistem Rekomendasi Webtoon')
st.caption('Content-Based Filtering menggunakan TF-IDF & Cosine Similarity')

if data_loaded:
  tab1, tab2 = st.tabs(['🎯 Cari Rekomendasi', '🏷️ Filter Genre'])

  # TAB 1: REKOMENDASI UTAMA
  with tab1:
    st.subheader('Cari Webtoon Favoritmu')

    col1, col2 = st.columns([3, 1])

    with col1:
      title_list = sorted(df['title'].unique().tolist())
      selected_title = st.selectbox(
          'Pilih Judul Webtoon:',
          options=title_list,
          help='Menggunakan dropdown agar bebas dari typo!',
      )

    with col2:
      top_n = st.slider(
          'Jumlah Rekomendasi:', min_value=3, max_value=10, value=5
      )

    if st.button('🔎 Dapatkan Rekomendasi', type='primary'):
      results = get_recommendations(selected_title, top_n)

      st.success(
          f'Berikut {top_n} Webtoon yang mirip dengan **{selected_title}**:'
      )

      # Tampilan Kartu Rekomendasi
      cols = st.columns(top_n)
      for i, (_, row) in enumerate(results.iterrows()):
        with cols[i]:
          st.markdown(f'### 📖 {i+1}')
          st.markdown(f"**{row['title']}**")
          st.caption(f"🎭 **Genre:** {row['genre']}")
          st.info(f"⭐ **Similarity:** {row['similarity_score']}")

          # Tampilkan summary
          summary_text = (
              row.get('summary')
              if pd.notna(row.get('summary'))
              else row.get('synopsis', '')
          )
          if summary_text:
            st.write(f'*{str(summary_text)[:90]}...*')

  # TAB 2: EXPLORE GENRE
  with tab2:
    st.subheader('Eksplorasi Berdasarkan Genre')

    all_genres = set()
    for g in df['genre'].dropna():
      for genre_item in g.split(','):
        genre_cleaned = genre_item.strip()
        if genre_cleaned:
          all_genres.add(genre_cleaned)

    selected_genre = st.selectbox('Pilih Genre:', sorted(list(all_genres)))

    if selected_genre:
      filtered_df = df[
          df['genre'].str.contains(selected_genre, case=False, na=False)
      ]
      st.write(
          f'Menampilkan **{len(filtered_df)}** Webtoon genre'
          f' **{selected_genre}**:'
      )

      display_cols = [
          c
          for c in ['title', 'genre', 'view', 'likes', 'summary']
          if c in df.columns
      ]
      st.dataframe(filtered_df[display_cols], use_container_width=True)