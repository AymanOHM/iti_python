from utils import *
from validation import *

current_user = {}

def get_current_user():
    return current_user

def sign_up():
    data = {}
    data['name'] = input("Enter your first name: ") + input("Enter your last name: ")
    data['email'] = input("Enter your email: ")
    data['password'] = input("Enter your password: ")
    data['phone'] = input("Enter your phone number: ")

    if all(validate_user(data).values()):
        append_to_file(data)
        print("Sign up successful!\n")

    else:
        print("Invalid input. Please try again.\n")
        sign_up()

def login():
    name = input("Enter your name: ")
    if validate_name(name):
        print('which number is yours: \n')
        results = search_db(name)
        for i, option in enumerate(results):
            print(f'[{i}] - ********{option['phone'][-3:]}')

        try: 
            choice = int(input())
        except:
            print("Invalid choice. Please try again.\n")
            return

        if choice < 0 or choice >= len(results):
            print("Invalid choice. Please try again.\n")
            return
        pswd = input('Enter your password: ')
        
        if results[choice]['password']==pswd:
            global current_user
            current_user = results[choice]
            print(f'Welcome {current_user['name']}\n')
            return
        else:
            print("Invalid password. Please try again.\n")
            return




    