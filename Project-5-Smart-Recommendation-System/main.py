import pandas as pd
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR,"movies.csv")

recommendation_result = None

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
    global recommendation_result
    try:
        data = load_data()

        preference = input("\nEnter preferred Genre or Keyword: ")

        data["features"] = (data["genre"].astype(str) + " " + data["description"].astype(str))

        tfidf = TfidfVectorizer(stop_words="english",lowercase=True)

        movie_vectors = tfidf.fit_transform(data["features"])

        user_vector = tfidf.transform([preference.lower()])

        similarity_scores = cosine_similarity(user_vector,movie_vectors)[0]

        data["similarity"] = similarity_scores

        recommendations = data[data["similarity"] > 0].sort_values(by="similarity",ascending=False).head(5)

        recommendation_result = []

        if recommendations.empty:
            print("\nNo close recommendations found.")
            return
        print("\nRecommended Movies:\n")
        for _, row in recommendations.iterrows():
            score = round(row["similarity"] * 100,2)
            recommendation_result.append([row["movie"],score])
            print(f"{row['movie']} - {score}% match")
    except Exception as e:
        print("Error:", e)

def save_recommendations():
    global recommendation_result
    if recommendation_result is None:
        print("Get Reommendations first")
        return
    result = pd.DataFrame(recommendation_result,columns=["movie","similarity_score"])

    result.to_csv(r"Project-5-Smart-Recommendation-System\recommendations.csv",index=False)

    print("Recommendations Saved Successfully.")

while True:
    print("\n-------Smart Recommendation System-------")
    print("1. View Dataset")
    print("2. Analyze Dataset")
    print("3. Get Recommendations")
    print("4. Save Recommendations")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        view_data()
    elif choice == "2":
        analyze_data()
    elif choice == "3":
        recommend_movies()
    elif choice == "4":
        save_recommendations()
    elif choice == "5":
        print("Thank you for using the system.")
        break
    else:
        print("Invalid choice")

    
