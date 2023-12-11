import json
import os
from helper import menu

contacts =[]
MY_DATA='output.txt'

def load_data():
    global contacts
    with open(MY_DATA, 'r') as filehandle:
        contacts = json.load(filehandle)

def save_2_file():
    with open(MY_DATA, 'w') as filehandle:
        json.dump(contacts, filehandle)

def do_menu_actions(userSelection):
    if userSelection == 'x': # when closing the applicaion
        save_2_file()
        print("bye bye")
        exit()
    if userSelection == 'p': print(contacts)
    if userSelection == 'a': contacts.append({"name":input("your name?"),"age":input("your age?")})
    if userSelection == 'd': print("not implemented yet - premium version only")

def main():
    load_data()
    while(True):
        menu()
        userSelection = input("please select action")
        os.system('cls' if os.name == 'nt' else 'clear') #clear terminal
        do_menu_actions(userSelection)

if __name__ == "__main__":
    main()
