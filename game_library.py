#!/usr/bin/python3
#Gentry Cross
#1/27/20

import pickle

'''This is a game library to hold all the Data to your games'''

def add_game():
    print("running add_game()")
    
def edit_game():
    print("running edit_game()")
    
def print_all():
    print("running print_all()")
    
def search_by_title():
    print("running search_by_title")
    
def remove_game():
    print("running remove_game()")
    
def save():
    print("running save()")
    
def quit():
    print("running quit()")
    
keep_going = True
    
while keep_going:
    print("""
    Welcome to your game library
    ---------------------------
        
    MAIN MENU
    1) Add Game
    2) Edit Game
    3) Print All 
    4) Search By Title
    5) Remove a Game
    6) Save Database
        
    Q) Quit
    
    """)

    choice = input("What would you like to do? ")
    if choice == "1":
        add_game()
    elif choice == "2":
        edit_game()
    elif choice == "3":
        print_all()
    elif choice == "4":
        search_by_title()
    elif choice == "5":
        remove_game()
    elif choice == "6":
        save()
    elif choice == "Q" or choice == "q":
        quit()
        keep_going = False
    else:
        print("*** NOT A VALID CHOICE ***\n")
        
print("Goodbye.")