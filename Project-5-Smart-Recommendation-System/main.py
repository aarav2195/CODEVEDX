import pandas as pd
import os

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
        print("Analyze Dataset selected")
    elif choice == "3":
        print("Get recommendations selected")
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice")

    
