import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

# Load and preprocess data
@st.cache_data
def load_data():
    df = pd.read_csv("tmdb_5000_movies.csv")
    df = df[['title', 'overview']].dropna()
    return df

# Compute cosine similarity
@st.cache_data
def compute_similarity(df):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['overview'])
    similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return similarity

# Get top 5 recommendations
def get_recommendations(title, df, similarity):
    index = df[df['title'].str.lower() == title.lower()].index
    if len(index) == 0:
        return ["Movie not found."]
    index = index[0]
    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    top_indices = [i[0] for i in scores[1:6]]
    return df['title'].iloc[top_indices].tolist()

# Streamlit UI
def main():
    st.title("\U0001F3AC Movie Recommendation System")
    df = load_data()
    similarity = compute_similarity(df)

    movie_list = df['title'].sort_values().tolist()
    selected_movie = st.selectbox("Select or type a movie:", movie_list)

    if st.button("Get Recommendations"):
        results = get_recommendations(selected_movie, df, similarity)
        st.subheader("Top 5 Similar Movies:")
        for movie in results:
            st.write("\u27A1", movie)

if __name__ == '__main__':
    main()
