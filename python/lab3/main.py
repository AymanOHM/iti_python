from user import *
from projects import *
from utils import *

def main():
    while True:
        print("1. Sign Up")
        print("2. Login")
        print("3. View Projects")
        print("4. New Project")
        print("5. Edit Projects")
        print("6. Delete Projects")
        print("7. Search Projects")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            sign_up()
        elif choice == '2':
            login()
        elif choice == '3':
            view_projects()
        elif choice == '4':
            new_project()
        elif choice == '5':
            edit_projects()
        elif choice == '6':
            edit_projects(True)
        elif choice == '7':
            search_projects()
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()