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
        print("View Dataset")
    elif choice == "2":
        print("Analyze Dataset")
    elif choice == "3":
        print("Handle Missing Values")
    elif choice == "4":
        print("Visualize Data")
    elif choice == "5":
        print("Predict Performance")
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice")
