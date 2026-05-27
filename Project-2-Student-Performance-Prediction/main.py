import pandas as pd
from sklearn.linear_model import LinearRegression

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
        try:
            data = pd.read_csv(r"E:\AARAV\CODEVEDX\Project-2-Student-Performance-Prediction\dataset.csv")
            print(data)
        except FileNotFoundError:
            print("Dataset not found")
    elif choice == "2":
        try:
            data = pd.read_csv(r"E:\AARAV\CODEVEDX\Project-2-Student-Performance-Prediction\dataset.csv")

            print("\nFirst 5 Records:")
            print(data.head())

            print("\nDataset Summary:")
            print(data.describe())
        except Exception as e:
            print("Error: ", e)
    elif choice == "3":
        try:
            data = pd.read_csv(r"E:\AARAV\CODEVEDX\Project-2-Student-Performance-Prediction\dataset.csv")

            data.loc[5,"marks"] = None

            print("\nMissing Values before cleaning:")
            print(data.isnull().sum())

            data["marks"] = data["marks"].fillna(data["marks"].mean())

            print("\nMissing Values after cleaning:")
            print(data.isnull().sum())
        except Exception as e:
            print("Error: ", e)
    elif choice == "4":
        print("Visualize Data")
    elif choice == "5":
        print("Predict Performance")
    elif choice == "6":
        print("Thank you for using the System.")
        break
    else:
        print("Invalid choice")
