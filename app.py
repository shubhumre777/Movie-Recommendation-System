import streamlit as st
import pandas as pd
import pickle
import requests
from sklearn.metrics.pairwise import cosine_similarity
import random
import warnings
warnings.filterwarnings("ignore")






st.markdown(
    """
    <style>
    .stApp {
        background-color: #0e1117;
    }
    </style>
    """,
    unsafe_allow_html=True
)



# PAGE TITLE


st.title("Movie Recommendation System")



# LOAD DATA


df = pickle.load(open("df.pkl","rb"))
indices = pickle.load(open("indices.pkl","rb"))
tfidf_matrix = pickle.load(open("tfidf_matrix.pkl","rb"))

df.reset_index(drop=True, inplace=True)



# API KEY


API_KEY = "191dcd0ee1772b533673233a4ee367d1"


# FETCH POSTER FUNCTION


import urllib.parse

@st.cache_data
def fetch_poster(movie_name):

    try:
        movie_name = urllib.parse.quote(movie_name)

        url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}"

        response = requests.get(url, timeout=5)
        data = response.json()

        # loop through results until poster found
        for result in data.get("results", []):
            if result.get("poster_path"):
                return "https://image.tmdb.org/t/p/w500" + result["poster_path"]

    except:
        pass

    return "https://static.vecteezy.com/system/resources/previews/025/903/813/non_2x/not-available-and-not-allowed-icon-concept-vector.jpg"


# MOVIE LIST ON THE PAGE


df2 = pd.read_csv("data/movies_metadata.csv")

st.subheader("Browse Movies")
st.divider()

# randomly pick 20 movies
if "homepage_movies" not in st.session_state:
    st.session_state.homepage_movies = df2.sample(20)["title"].reset_index(drop=True)

sample_movies = st.session_state.homepage_movies

# show 5 movies per row
for i in range(0, 20, 5):

    cols = st.columns(5 , gap="medium")

    for j in range(5):

        movie = sample_movies[i + j]

        poster = fetch_poster(movie)

        with cols[j]:
            st.image(poster, width=180)
            st.markdown(f"**{movie}**")
            st.space("medium")

# RECOMMENDATION FUNCTION


def recommend(movie_title):

    idx = indices[movie_title]

    sim_scores = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()

    sim_scores = sim_scores.argsort()[::-1][1:6]

    sim_scores = [i for i in sim_scores if i < len(df)]

    recommended_movies = df.iloc[sim_scores]['title']

    return recommended_movies



# SIDEBAR


st.sidebar.header("Movie Selector")

movie_list = df['title'].values

selected_movie = st.sidebar.selectbox(
    "Choose a movie",
    movie_list
)

recommend_button = st.sidebar.button("Recommend")



# MAIN PAGE RESULTS


if recommend_button:

    st.spinner("Recommending movies")

    recommendations = recommend(selected_movie)

    st.subheader("Recommended Movies")

    cols = st.columns(5)

    for i, movie in enumerate(recommendations):

        poster = fetch_poster(movie)

        with cols[i]:
            st.image(poster, width=180)
            st.markdown(f"**{movie}**")
