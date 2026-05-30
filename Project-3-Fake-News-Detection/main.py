import pandas as pd

while True:
    print("\n-------Fake News Detection-------")
    print("1. View Dataset")
    print("2. Train Model")
    print("3. Detect News")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == "1":
        print("View Dataset selected")
    elif choice == "2":
        print("Train Model Selected")
    elif choice == "3":
        print("Detect News Selected")
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice")
        