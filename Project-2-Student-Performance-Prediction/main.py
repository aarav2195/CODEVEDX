import pandas as pd
import os
from sklearn.linear_model import LinearRegression

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR,"dataset.csv")

#Load data from CSV file
def load_data():
    return pd.read_csv(CSV_FILE)

#View data
def view_data():
    try:
        data = load_data()
        print(data)
    except FileNotFoundError:
        print("Dataset not found")

#Exploratory Data Analysis(EDA)
def analyze_data():
    try:
        data = load_data()

        print("\nFirst 5 Records:")
        print(data.head())

        print("\nDataset Summary:")
        print(data.describe())
    except Exception as e:
        print("Error: ", e)

#Missing values handling
def handle_missing_values():
    try:
        data = load_data()

        data.loc[5,"marks"] = None

        print("\nMissing Values before cleaning:")
        print(data.isnull().sum())

        data["marks"] = data["marks"].fillna(data["marks"].mean())

        print("\nMissing Values after cleaning:")
        print(data.isnull().sum())
    except Exception as e:
        print("Error: ", e)

#Training Linear Regression model
def train_model():
    data = load_data()

    X = data[["attendance","marks","study_hours"]]

    y = data["final_performance"]

    model = LinearRegression()

    model.fit(X,y)

    return model

#Predict Performance
def predict_performane():
    try:
        model = train_model()

        attendance = int(input("Enter attenance: "))
        marks = int(input("Enter marks: "))
        study_hours = int(input("Enter study hours: "))

        input_data = pd.DataFrame({"attendance":[attendance],"marks":[marks],"study_hours":[study_hours]})

        prediction = model.predict(input_data)

        print(f"Predicted Performance: {prediction[0]:.2f}")
    except ValueError:
        print("Please enter valid numeric values.")
    except Exception as e:
        print("Error: ", e)

while True:
    print("\n-------Student Performance Prediction System-------")
    print("1. View Dataset")
    print("2. Analyze Dataset")
    print("3. Handle Missing Values")
    print("4. Visualize Data")
    print("5. Predict Performance")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_data()
    elif choice == "2":
        analyze_data()
    elif choice == "3":
        handle_missing_values()
    elif choice == "4":
        print("Visualize Data")
    elif choice == "5":
        predict_performane()
    elif choice == "6":
        print("Thank you for using the System.")
        break
    else:
        print("Invalid choice")
