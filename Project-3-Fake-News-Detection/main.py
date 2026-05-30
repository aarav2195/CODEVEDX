import pandas as pd
import os
import re

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

def preprocess_text():
    text = text.lower()

    text = re.sub(r'[^a-zA-Z ]', '', text)

    return text

while True:
    print("\n-------Fake News Detection-------")
    print("1. View Dataset")
    print("2. Train Model")
    print("3. Detect News")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == "1":
        view_data()
    elif choice == "2":
        print("Train Model Selected")
    elif choice == "3":
        print("Detect News Selected")
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice")
