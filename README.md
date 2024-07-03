# Movie Recommendation System

The Movie Recommendation System is an application designed to help users discover movies similar to their favorites. By leveraging data from The Movie Database (TMDb) and advanced machine learning techniques, the system provides accurate and personalized movie recommendations.

## How the Recommender System Works

1. **Data Collection**:
   - The system uses datasets containing movie details and credits (cast and crew information) from TMDb.
   - https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

2. **Data Processing**:
   - Merge and clean the datasets.
   - Extract and preprocess relevant features (genres, cast, crew, keywords).
   - Combine these features into a single text representation for each movie.

3. **Vectorization and Similarity Calculation**:
   - Convert text data into numerical vectors using TF-IDF (Term Frequency-Inverse Document Frequency).
   - Compute the cosine similarity matrix to find similar movies.

4. **Model Deployment**:
   - Save the processed data and similarity matrix as pickle files.
   - Develop a Streamlit app to provide a user-friendly interface for movie recommendations.
   - Use the saved data and similarity matrix to recommend movies based on user input.

## Project Workflow

### Data Preparation (Jupyter Notebook)

1. **Import Libraries**:
   ```python
   import numpy as np
   import pandas as pd
