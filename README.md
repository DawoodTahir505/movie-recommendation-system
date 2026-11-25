<h1 align="center">🎬 Movie Recommendation System</h1> <p align="center"> A content-based movie recommender that suggests five similar movies, with posters, for any title you select. </p> <p align="center"> <a href="https://movie-recommender-app01.streamlit.app/"><b>🚀 Live Demo</b></a> </p> <p align="center"> <img src="https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white" alt="Python"> <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit"> <img src="https://img.shields.io/badge/Scikit--learn-ML-F7931E?logo=scikitlearn&logoColor=white" alt="Scikit-learn"> <img src="https://img.shields.io/badge/License-MIT-green" alt="License"> </p> <p align="center"> <a href="https://movie-recommender-app01.streamlit.app/"> <img src="assets/app-image.png" alt="Movie Recommendation System Screenshot" width="800"> </a> </p>
Table of Contents
Features
How It Works
Tech Stack
Project Structure
Getting Started
Configuration
Dataset
License
Features
Content-based recommendations using cosine similarity
Five similar movies for any selected title
Movie posters fetched from the TMDB API
Clean, interactive interface built with Streamlit
Deployed on Streamlit Community Cloud
How It Works
Data preparation: The TMDB 5000 Movies and Credits datasets are merged and cleaned.
Feature engineering: Overview, genres, keywords, top 3 cast members, and director are combined into a single tags field.
Text processing: Tags are lowercased and stemmed with the Porter Stemmer.
Vectorization: Tags are converted to vectors using CountVectorizer (5000 features, English stop words removed).
Similarity: Cosine similarity is computed between every pair of movies.
Recommendation: For the selected movie, the app returns the 5 closest titles and loads their posters from TMDB.
Tech Stack
Category	Tools
Language	Python
Data processing	Pandas, NumPy
Machine learning	Scikit-learn, NLTK
Web app	Streamlit
External API	TMDB API
Project Structure
movie-recommendation-system/
├── assets/
│   └── app-image.png                  # App screenshot
├── app.py                             # Streamlit application
├── Movie-Recomendation-System.ipynb   # Data processing and model building
├── movies_dict                        # Processed movie data
├── simalarity.pkl                     # Precomputed similarity matrix
├── requirements.txt                   # Dependencies
└── README.md
Getting Started
1. Clone the repository
bash
git clone https://github.com/YOUR-USERNAME/movie-recommendation-system.git
cd movie-recommendation-system
2. Create a virtual environment (optional)
bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux
3. Install dependencies
bash
pip install -r requirements.txt
4. Run the app
bash
streamlit run app.py

Open http://localhost:8501 in your browser.

Configuration

Posters are loaded from the TMDB API. Create a free account, generate an API key, and use it in app.py in place of the existing key.

Dataset

TMDB 5000 Movie Dataset on Kaggle.

License

This project is licensed under the MIT License.
