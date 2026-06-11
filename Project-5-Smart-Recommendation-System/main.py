import pandas as pd
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR,"movies.csv")

def load_data():
    return pd.read_csv(CSV_FILE)

def view_data():
    try:
        data = load_data()

        print("\nMovie Dataset:")

        print(data)
    except FileNotFoundError:
        print("Dataset not found.")
    except Exception as e:
        print("Error: ",e)

def analyze_data():
    try:
        data = load_data()

        print("\nDataset Analysis:")
        
        print("\nTotal Movies: ", len(data))
        
        print("\nGenre Distribution:")
        print(data["genre"].value_counts())

        print("\nAverage Rating:")
        print(round(data["rating"].mean(),2))

        best_movie = data.loc[data["rating"].idxmax()]

        print("\nHighest Rated Movie: ")

        print(best_movie["movie"], " - " ,best_movie["rating"])
    except Exception as e:
        print("Error: ", e)

def recommend_movies():
    try:
        data = load_data()

        preference = input("\nEnter preferred Genre: ")

        tfidf = TfidfVectorizer()

        tfidf_matrix = tfidf.fit_transform(data["genre"])

        user_vector = tfidf.transform([preference])

        similarity_scores = cosine_similarity(user_vector,tfidf_matrix)

        scores = similarity_scores.flatten()

        top_indices = scores.argsort()[::-1][:5]

        print("\nRecommended Movies:\n")

        for index in top_indices:
            print(data.iloc[index]["movie"])
    except Exception as e:
        print("Error: ",e)

while True:
    print("\n-------Smart Recommendation System-------")
    print("1. View Dataset")
    print("2. Analyze Dataset")
    print("3. Get Recommendations")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        view_data()
    elif choice == "2":
        analyze_data()
    elif choice == "3":
        recommend_movies()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice")

    
