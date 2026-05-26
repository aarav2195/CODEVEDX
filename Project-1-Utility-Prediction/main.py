import pandas as pd
import os
import random
from sklearn.linear_model import LinearRegression

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR,"dataset.csv")

#Load data from CSV file
def load_data():
    return pd.read_csv(CSV_FILE)

#Display all records
def view_data():
    try:
        data = load_data()
        print("\nCurrent Data:")
        print(data)
    except FileNotFoundError:
        print("Dataset file not found.")
    except Exception as e:
        print("Error: ", e)

#Add new record to dataset
def add_data():
    try:
        members = int(input("Enter family members: "))
        hours = int(input("Enter usage hours: "))
        usage = (members * 25) + (hours * 15) + random.randint(-15,15) 

        new_row = pd.DataFrame({"members":[members],"hours":[hours],"usage":[usage]})
        new_row.to_csv(CSV_FILE,mode="a",header=False,index=False)
        print("Data added successfully!")
    except ValueError:
        print("Please enter valid numeric values.")
    except Exception as e:
        print("Error: ", e)

#Update an existing record
def update_data():
    try:
        data = load_data()
        print("\nCurrent Data:")
        print(data)

        row = int(input("Enter the row number to update: "))
        if row not in data.index:
            print("Invalid Row number")
        else:
            members = int(input("Enter new family members: "))
            hours = int(input("Enter new usage hours: "))
            usage = (members * 25) + (hours * 15) + random.randint(-15,15)

            data.loc[row] = [members,hours,usage]

            data.to_csv(CSV_FILE,index=False)
            print("Record updated successfully!")
    except ValueError:
        print("Please enter valid numeric values.")
    except FileNotFoundError:
        print("Dataset file not found.")
    except Exception as e:
        print("Error: ", e)

#Train Linear Regression Model
def train_model():
    data = load_data()

    X = data[["members","hours"]]
    y = data["usage"]

    model = LinearRegression()
    model.fit(X,y)

    return model

#Predict utility usage
def predict_usage():
    try:
        model = train_model()

        members = int(input("Enter family members: "))
        hours = int(input("Enter usage hours: "))

        input_data = pd.DataFrame({"members":[members],"hours":[hours]})

        prediction = model.predict(input_data)

        print(f"\nPredicted Utility Usage: {prediction[0]:.2f} units")
    except ValueError:
        print("Please enter valid numeric values.")
    except Exception as e:
        print("Error:", e)

#Delete an existing record
def delete_data():
    try:
        data = load_data()

        print("\nCurrent Data:")
        print(data)

        row = int(input("\nEnter row number to delete: "))

        if row not in data.index:
            print("Invalid row index.")
            return
        data = data.drop(row)

        data.reset_index(drop=True,inplace=True)

        data.to_csv(CSV_FILE,index=False)

        print("Record deleted successfully!")
    except ValueError:
        print("Please enter valid numeric values.")
    except Exception as e:
        print("Error:", e)

while True:
    print("\n-------Utility Usage Prediction Tool-------")
    print("1. View Data")
    print("2. Add Data")
    print("3. Update Data")
    print("4. Predict Usage")
    print("5. Delete Data")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_data()
    elif choice == "2":
        add_data()
    elif choice == "3":
        update_data()
    elif choice == "4":
        predict_usage()
    elif choice == "5":
        delete_data()
    elif choice == "6":
        print("Thank you for using the System.")
        break
    else:
        print("Invalid Choice")