# 🎬 Movie Recommendation System

A content-based movie recommender built with Python and Streamlit. Select a movie and get five similar recommendations with posters.

<p align="center">
  <img src="app-image.png" alt="Movie Recommendation System Screenshot" width="800">
</p>

## Features
- Content-based recommendations using cosine similarity
- Movie posters fetched from the TMDB API
- Simple, interactive web interface

## How It Works
1. The TMDB 5000 Movies and Credits datasets are merged and cleaned.
2. Overview, genres, keywords, top 3 cast members, and director are combined into a single `tags` field.
3. Tags are stemmed (Porter Stemmer) and vectorized using `CountVectorizer` (5000 features).
4. Cosine similarity is computed between all movies.
5. The app returns the 5 most similar movies to the selected title.

## Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn, NLTK
- Streamlit
- TMDB API

## Project Structure
```
├── app.py                           # Streamlit application
├── Movie-Recomendation-System.ipynb # Data processing and model building
├── movies_dict                      # Movie data (pickle)
├── movies.pkl                       # Movie data (pickle)
├── simalarity.pkl                   # Similarity matrix (pickle)
└── requirements.txt                 # Dependencies
```

## Installation
```bash
git clone https://github.com/username/repo-name.git
cd repo-name
pip install -r requirements.txt
```

## Configuration
Get a free API key from [TMDB](https://www.themoviedb.org/settings/api) and add it to `app.py` in place of the existing key.

## Usage
```bash
streamlit run app.py
```
Open `http://localhost:8501` in your browser.

## Dataset
[TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) (Kaggle)

## License
This project is licensed under the MIT License.
