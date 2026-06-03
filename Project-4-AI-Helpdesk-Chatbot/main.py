import pandas as pd
import os
import nltk

nltk.download("punkt_tab")
nltk.download("punkt")
nltk.download("stopwords")

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR,"faq_dataset.csv")

stop_words = set(stopwords.words("english"))

#Load data from CSV file
def load_data():
    return pd.read_csv(CSV_FILE)

#Display all records
def view_data():
    try:
        data = load_data()

        print("\nFAQ Dataset:")

        print(data)
    except FileNotFoundError:
        print("Dataset Not found.")
    except Exception as e:
        print("Error: ", e)

#
def add_faq():
    try:
        question = input("Enter question: ").strip()

        answer = input("Enter answer: ").strip()

        new_row = pd.DataFrame({
            "question":[question],
            "answer":[answer]
        })

        new_row.to_csv(CSV_FILE, mode="a", header=False, index=False)

        print("\nFAQ Added Successfuly")
    except Exception as e:
        print("Error: ", e)

#Dataset text preprocessing
def preprocess_text(text):
    tokens = word_tokenize(text.lower())

    filtered_words = []

    for word in tokens:
        if word.isalnum() and word not in stop_words:
            filtered_words.append(word)

    return set(filtered_words)

#
def chat_bot():
    try:
        data = load_data()

        user_question = input("\nAsk a question: ").strip().lower()

        user_tokens = preprocess_text(user_question)

        best_match = None
        max_score = 0

        for i in range(len(data)):
            faq_question = data.loc[i, "question"]

            faq_tokens = preprocess_text(faq_question)
            score = len(user_tokens.intersection(faq_tokens))

            if score>max_score:
                max_score = score
                best_match = i
            
        if best_match is not None and max_score > 0:
                print("\nBot: ", data.loc[best_match,"answer"])
        else:
            print("Bot: Sorry, I don't know the answer.")
    except Exception as e:
        print("Error: ", e)

while True:
    print("\n------AI Helpdesk Chatbot-------")
    print("1. View FAQ Dataset")
    print("2. Chat with Bot")
    print("3. Add FAQ")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        view_data()
    elif choice == "2":
        chat_bot()
    elif choice == "3":
        add_faq()
    elif choice == "4":
        print("Thank you for using the Chatbot.")
        break
    else:
        print("Invalid Choice")