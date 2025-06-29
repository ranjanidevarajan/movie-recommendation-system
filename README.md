# 🎬 Movie Recommendation System

A content-based movie recommendation system built using NLP techniques on the TMDB 5000 Movie Dataset. It recommends top 5 similar movies based on the overview text of a selected movie.

![Streamlit Screenshot](./screenshot.png)

---

## 🔍 Features

- Select any movie from a dropdown list
- Get top 5 similar movie recommendations
- Uses TF-IDF + Cosine Similarity for matching
- Built with **Python**, **Pandas**, **Streamlit**
- Clean, dark-themed UI using Streamlit

---

## 📁 Dataset

- Source: [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- File used: `tmdb_5000_movies.csv`

---

## 🧠 How It Works

1. **Text Vectorization**: Movie overviews are converted into vectors using TF-IDF.
2. **Similarity Calculation**: Cosine similarity is computed between all movies.
3. **Top Matches**: Top 5 most similar movies are shown for a selected movie.

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
