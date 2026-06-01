import pandas as pd
import os
import nltk
import pickle

nltk.download("punkt_tab")
nltk.download("punkt")
nltk.download("stopwords")

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR,"dataset.csv")

stop_words = set(stopwords.words("english"))

#Load data from CSV file
def load_data():
    return pd.read_csv(CSV_FILE)

#Display all records
def view_data():
    try:
        data = load_data()
        print(data)
    except FileNotFoundError:
        print("Dataset not found.")
    except Exception as e:
        print("Error: ", e)

#Analyze Dataset
def analyze_data():
    data = load_data()

    print("\nData Analysis")

    print("Total records: ", len(data))

    print("\nClass Distribution: ")

    print(data["label"].value_counts())

#Text Preprocessing
def preprocess_text(text):
    tokens = word_tokenize(text.lower())

    filtered_words = []

    for word in tokens:
        if word.isalpha() and word not in stop_words:
            filtered_words.append(word)

    return " ".join(filtered_words)

#Train model
def train_model():
    try:
        data = load_data()

        data["text"] = data["text"].apply(preprocess_text)

        vectorizer = TfidfVectorizer()

        X = vectorizer.fit_transform(data["text"])

        y = data["label"]

        model = LogisticRegression()

        model.fit(X,y)

        #Save Model
        with open(r"E:\AARAV\CODEVEDX\Project-3-Fake-News-Detection\model.pkl", "wb") as file:
            pickle.dump(model,file)

        #Save Vectorizer
        with open(r"E:\AARAV\CODEVEDX\Project-3-Fake-News-Detection\vectorizer.pkl", "wb") as file:
            pickle.dump(vectorizer,file)

        return model, vectorizer
    except Exception as e:
        print("Error: ", e)
        return None, None
    
#Detect News
def detect_news():
    try:
        model, vectorizer = load_model()

        news = input("Enter New Text: ")

        news = preprocess_text(news)

        news_vector = vectorizer.transform([news])

        prediction = model.predict(news_vector)

        confidence = model.predict_proba(news_vector)

        print("\nPrediction: ", prediction[0])

        print("\nConfidence Score: ", round(max(confidence[0]) * 100, 2), "%")
    except Exception as e:
        print("Error: ", e)

#Load Saved model
def load_model():
    try:
        if os.path.getsize(r"E:\AARAV\CODEVEDX\Project-3-Fake-News-Detection\model.pkl") == 0:
            print("Model file is empty. Train model again.")
            return None, None
    
        with open(r"E:\AARAV\CODEVEDX\Project-3-Fake-News-Detection\model.pkl", "rb") as file:
            model = pickle.load(file)

        with open(r"E:\AARAV\CODEVEDX\Project-3-Fake-News-Detection\vectorizer.pkl", "rb") as file:
            vectorizer = pickle.load(file)
        
        print("\nSaved Model loaded Successfully")

        return model, vectorizer
    except FileNotFoundError:
        print("Train the model first.")
        return None, None

while True:
    print("\n-------Fake News Detection-------")
    print("1. View Dataset")
    print("2. Analyze Dataset")
    print("3. Train Model")
    print("4. Detect News")
    print("5. Load Saved Model")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_data()
    elif choice == "2":
        analyze_data()
    elif choice == "3":
        model, vectorizer = train_model()
        print("Model Trained Successfully")
        print("Model Saved Successfully")
    elif choice == "4":
        detect_news()
    elif choice == "5":
        load_model()
    elif choice == "6":
        print("Thank you for using the System.")
        break
    else:
        print("Invalid choice")
