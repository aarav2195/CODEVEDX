import pandas as pd
import os
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR,"dataset.csv")

#Load data from CSV file
def load_data():
    return pd.read_csv(CSV_FILE)

#Display all records
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

#Data Visualization
def visualize_data():
    data = load_data()

    print("\nVisualization Options")
    print("1. Attendance vs Final Performance")
    print("2. Study Hours vs Marks")
    print("3. Marks Distribution")

    visual_choice = input("Enter choice: ")

    if visual_choice == "1":

        plt.scatter(data["attendance"], data["final_performance"])

        plt.xlabel("Attendance")
        plt.ylabel("Final Performance")
        plt.title("Attendance vs Final Performance")

        plt.show()
        
    elif visual_choice == "2":

        plt.scatter(data["study_hours"], data["marks"])

        plt.xlabel("Study Hours")
        plt.ylabel("Marks")
        plt.title("Study Hours vs Marks")

        plt.show()
        
    elif visual_choice == "3":

        plt.hist(data["marks"])

        plt.xlabel("Marks")
        plt.ylabel("Frequency")
        plt.title("Marks Distribution")

        plt.show()
        
    else:
        print("Invalid Choice")

#Training Linear Regression model
def train_model():
    data = load_data()

    X = data[["attendance","marks","study_hours"]]

    y = data["final_performance"]

    model = LinearRegression()

    model.fit(X,y)

    predictions = model.predict(X)

    accuracy = r2_score(y,predictions)

    print(f"\nModel Accuracy: {accuracy*100:.2f}%")

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
        visualize_data()
    elif choice == "5":
        predict_performane()
    elif choice == "6":
        print("Thank you for using the System.")
        break
    else:
        print("Invalid choice")
