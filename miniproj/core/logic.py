
drinkslist = []
peoplenamelist = []
orders = []
preflist = []

import os
from core.utility import clear_screen
from persistence.sql import readperson
    
def menu():
    clear_screen()
    menu_text = """
    Please, select an option below by entering a number:
        [1] Add a person
        [2] Display a list of first names of ALL PEOPLE
        [3] Add drinks
        [4] Get a list of names of ALL DRINKS
        [5] Activate a ROUND of drinks
        [6] Print ROUND results
        [7] Enter drink PREFERENCES
        [8] EXIT
        """
    print(menu_text)        
