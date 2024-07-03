import pickle
import streamlit as st
import requests

# Function to fetch movie poster
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=fded6455c527795f4d9762ee68d0f08c&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# Function to recommend movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:10]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movie_names, recommended_movie_posters

# Load movie data
movies = pickle.load(open('model/movie_list.pkl', 'rb'))
similarity = pickle.load(open('model/similarity.pkl', 'rb'))

# Apply custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #141414;
        color: #FFFFFF;
        font-family: 'Arial', sans-serif;
    }
    .stSelectbox label {
        color: #FFFFFF;
    }
    .stButton button {
        background-color: #E50914;
        color: #FFFFFF;
    }
    .stTextInput input {
        color: #000000;
    }
    .movie-title {
        font-size: 14px;
        font-weight: bold;
        margin-bottom: 10px;
        text-align: center;
    }
    .movie-poster {
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App header
st.markdown('<h1 style="color: #E50914; text-align: center;">Movie Recommendation System</h1>', unsafe_allow_html=True)

# Select movie
movie_list = movies['title'].values
selected_movie = st.selectbox('Type a Movie Name', movie_list)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    for i in range(0, len(recommended_movie_names), 4):
        columns = st.columns(4)
        for col, name, poster in zip(columns, recommended_movie_names[i:i+4], recommended_movie_posters[i:i+4]):
            with col:
                st.markdown(f'<div class="movie-title">{name}</div>', unsafe_allow_html=True)
                st.markdown(f'<img src="{poster}" class="movie-poster">', unsafe_allow_html=True)
