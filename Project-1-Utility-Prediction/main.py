import pandas as pd

while True:
    print("\n-------Utility Usage Prediction Tool-------")
    print("1. View Data")
    print("2. Add Data")
    print("3. Update Data")
    print("4. Predict Usage")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        data = pd.read_csv(r"E:\AARAV\CODEVEDX\Project-1-Utility-Prediction\dataset.csv")
        print(data)
    elif choice == "2":
        try:
            members = int(input("Enter family members: "))
            hours = int(input("Enter usage hours: "))
            usage = int(input("Enter utility usage:")) 

            new_row = pd.DataFrame({"members":[members],"hours":[hours],"usage":[usage]})
            new_row.to_csv(r"E:\AARAV\CODEVEDX\Project-1-Utility-Prediction\dataset.csv",mode="a",header=False,index=False)
            print("Data added successfully")
        except ValueError:
            print("Please enter valid numeric values.")
    elif choice == "3":
        print("Update Data selected")
    elif choice == "4":
        print("Predict Usage selected")
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid Choice")
