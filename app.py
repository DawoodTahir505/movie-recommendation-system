import streamlit as st
import pickle
import pandas as pd
import requests

movies_dict = pickle.load(open('movies_dict','rb'))
new_data = pd.DataFrame(movies_dict)


st.title("Movie Recommendation System")

def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=fe461ea20bb99950d3fab6dc5b8de4f4&language=en-US")
    data = response.json()
    return f"https://image.tmdb.org/t/p/w500{data['poster_path']}"


def recommend(movie):
    movie_index = new_data[new_data['title'] == movie].index[0]
    distance = simalarity[movie_index]
    movie_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movie_list:
        movies_id = new_data.iloc[i[0]].movie_id
        #fetch poster from api
        recommended_movies.append(new_data.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movies_id))
    return recommended_movies,recommended_movies_posters

simalarity = pickle.load(open('simalarity.pkl','rb'))

option = st.selectbox("Select a movie you like", new_data['title'].values)


if st.button("Recommend"):
    names,posters = recommend(option)
    for i in option:
        st.write(i)


if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])




