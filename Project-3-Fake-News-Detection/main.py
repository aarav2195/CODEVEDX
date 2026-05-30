import pandas as pd
import os
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR,"dataset.csv")

def load_data():
    return pd.read_csv(CSV_FILE)

def view_data():
    try:
        data = load_data()
        print(data)
    except FileNotFoundError:
        print("Dataset not found.")
    except Exception as e:
        print("Error: ", e)

def preprocess_text(text):
    text = text.lower()

    text = re.sub(r'[^a-zA-Z ]', '', text)

    return text

def train_model():
    data = load_data()

    data["text"] = data["text"].apply(preprocess_text)

    vectorizer = TfidfVectorizer()

    X = vectorizer.fit_transform(data["text"])

    y = data["label"]

    model = LogisticRegression()

    model.fit(X,y)

    return model, vectorizer

def detect_news():
    try:
        model, vectorizer = train_model()

        news = input("Enter New Text: ")

        news = preprocess_text(news)

        news_vector = vectorizer.transform([news])

        prediction = model.predict(news_vector)

        print("\nPrediction: ", prediction[0])
    except Exception as e:
        print("Error: ", e)

while True:
    print("\n-------Fake News Detection-------")
    print("1. View Dataset")
    print("2. Train Model")
    print("3. Detect News")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_data()
    elif choice == "2":
        model, vectorizer = train_model()
        print("Model Trained Successfully")
    elif choice == "3":
        detect_news()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice")
