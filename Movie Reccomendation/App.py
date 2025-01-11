import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
movies = pd.read_csv('dataset.csv')

# Combine 'genre' and 'overview' into a 'tags' column
movies['tags'] = movies['genre'] + ' ' + movies['overview']

# Create a new DataFrame with only relevant columns
new_df = movies[['id', 'title', 'genre', 'overview', 'tags']]

# Drop unnecessary columns
new_df = new_df.drop(columns=['genre', 'overview'])

# Vectorize the 'tags' column
cv = CountVectorizer(max_features=10000, stop_words='english')
vec = cv.fit_transform(new_df['tags'].values.astype('U')).toarray()

# Calculate cosine similarity
sim = cosine_similarity(vec)

# Function to recommend movies
def recommend(movies):
    index = new_df[new_df['title'] == movies].index[0]
    distance = sorted(list(enumerate(sim[index])), reverse=True, key=lambda vec: vec[1])
    
    recommendations = []
    for i in distance[1:6]:  # Skip the first movie (itself)
        recommendations.append(new_df.iloc[i[0]].title)
    
    return recommendations

# Streamlit UI
st.title("🎬 Movie Recommendation System 🍿")
st.markdown("""
Welcome to the **Movie Recommendation System**! 
Here, you can discover movies similar to your favorites. Just enter a movie title and get recommendations instantly. 🎥
""")

# User input for movie selection
user_movie = st.text_input("Enter a movie title to get recommendations: 🎬", "")

if user_movie:
    st.subheader(f"Recommendations based on: {user_movie} 🌟")
    
    # Check if the movie exists in the dataset
    if user_movie in new_df['title'].values:
        recommendations = recommend(user_movie)
        
        # Display the results
        st.write("Here are the top 5 similar movies:")
        
        for i, movie in enumerate(recommendations, 1):
            st.markdown(f"{i}. {movie} 🎥")
    else:
        st.error("Sorry, we couldn't find that movie in our database. Please try another one! 😔")

# Add some styling and information
st.sidebar.header("About")
st.sidebar.markdown("""
This Movie Recommendation System uses **content-based filtering** to suggest movies that are similar to the one you provide. 
It analyzes the genre and overview of movies and finds the most similar ones using cosine similarity.
""")

st.sidebar.header("How It Works 🤖")
st.sidebar.markdown("""
1. **Enter a movie title**: Type the name of any movie you'd like recommendations for.
2. **See similar movies**: Based on the genre and description, get the top 5 similar movies.
3. **Enjoy!** 🎉
""")

# Additional visual enhancements
st.markdown("""
### ✨ Fun Fact ✨
Did you know that **The Godfather** is considered one of the greatest films of all time? 🎬🍿

""")
