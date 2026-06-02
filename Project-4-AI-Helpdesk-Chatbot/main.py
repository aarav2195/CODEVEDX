import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR,"faq_dataset.csv")

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
        print("Chat feature coming next")
    elif choice == "3":
        add_faq()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid Choice")