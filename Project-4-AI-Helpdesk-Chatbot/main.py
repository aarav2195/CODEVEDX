import pandas as pd

while True:
    print("\n------AI Helpdesk Chatbot-------")
    print("1. View FAQ Dataset")
    print("2. Chat with Bot")
    print("3. Add FAQ")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("View dataset selected")
    elif choice == "2":
        print("Chat feature coming next")
    elif choice == "3":
        print("Add FAQ feature coming next")
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid Choice")