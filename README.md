# 🎬 **Movie Recommendation System** 🍿

Welcome to the **Movie Recommendation System**! This is a content-based recommendation engine that suggests movies similar to the one you provide. Built using **Streamlit**, **pandas**, and **sklearn**, this system analyzes movie genres and overviews to recommend similar movies. Whether you're looking for something new to watch or want to discover hidden gems, this app is here to help! ✨

---

## 🧑‍💻 **About the Project**:
This project is a **Movie Recommendation System** that leverages **content-based filtering** to suggest movies similar to a given movie title. It combines the power of **Cosine Similarity** and movie metadata (like genre and overview) to find the most similar films from a dataset. 🎥🍿

### Key Features:
- **Content-Based Filtering**: Recommends movies based on the similarity of movie genres and overviews.
- **Cosine Similarity**: Uses Cosine Similarity to measure how similar movies are based on their tags (genre + overview).
- **Real-Time Recommendations**: Get recommendations instantly by entering any movie title.
- **Interactive UI**: Built with **Streamlit** for a user-friendly interface. 

---

## 🚀 **How to Use**:

### 1. **Install the Required Libraries**:
Before using the system, you’ll need to install some dependencies:
```bash
pip install pandas numpy scikit-learn streamlit
```

### 2. **Download the Dataset**:
Make sure to download the `dataset.csv` file, which contains the movie information (title, genre, overview, etc.). This file is essential for the recommendation system to work.

### 3. **Run the Streamlit App**:
Once everything is set up, navigate to the directory containing your app and dataset, then run the following command:
```bash
streamlit run streamlit_app.py
```
This will launch the app in your web browser at `http://localhost:8501`. 🎉

### 4. **Enter a Movie Title**:
On the homepage, type in the name of a movie you’d like recommendations for, and hit enter! The app will display a list of similar movies based on the input. 🌟

---

## 💻 **How It Works**:

- **Movie Data**: The app uses a dataset of movies, including title, genre, and overview.
- **Tags Generation**: It combines the **genre** and **overview** of each movie to generate a "tag" that describes it.
- **Vectorization**: We use **CountVectorizer** from the `sklearn` library to transform movie tags into a numeric matrix.
- **Cosine Similarity**: The system calculates the **cosine similarity** between movies based on their tags, which helps to identify the most similar ones.

---

## 🖼️ **Screenshots**:

Here’s a preview of what the app looks like:

![Movie Recommendation System](./assets/screenshot.png)  
*Screenshot of the Movie Recommendation System in action* 📸

---

## 💡 **Additional Information**:

### 🧑‍🏫 **How Recommendations Are Made**:
When you enter a movie title, the system:
1. Finds the movie's index in the dataset.
2. Computes the **cosine similarity** between that movie and all others.
3. Ranks movies based on similarity and returns the top 5.

### 🧠 **Used Libraries**:
- **pandas**: For data manipulation and loading the dataset.
- **numpy**: For numerical computations.
- **sklearn**: For machine learning algorithms, specifically **CountVectorizer** and **cosine_similarity**.
- **streamlit**: To create the user interface.

---

## 👨‍💻 **Contributing**:
We welcome contributions! If you have any improvements, bug fixes, or new features to add, feel free to open an issue or submit a pull request.

To contribute:
1. Fork this repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and push to your fork.
4. Open a pull request with a description of your changes.

---

## 🤖 **Acknowledgments**:
- This project uses **Cosine Similarity** and **Content-Based Filtering** to generate recommendations.
- **Streamlit** was used to build the interactive web app, which makes it easy to create and share data apps.

---

## 📜 **License**:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📧 **Contact**:
If you have any questions, feel free to reach out to me at:  
[hardikarora483@gmail.com] 

---

## 🎉 **Enjoy Exploring Movies**:
Start discovering movies similar to your favorites and find new ones to watch! 🍿🎬
```
