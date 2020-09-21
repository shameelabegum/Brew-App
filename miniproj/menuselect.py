import csv
import os

from core.logic import menu, drinkslist, peoplenamelist, orders, preflist
from core.classes import Person, Drinks, Order, Preferences
from core.utility import clear_screen
from core.sqll import readperson, readdrink, writeperson, writedrink

while True:
    clear_screen()
    menu()
    ans = input("Enter a number:")
    
    if ans == '1':
        writeperson()
        print('Your input has been added to the database. Thanks!')
        input("Hit enter to go back to the menu")
        
    elif ans == '2':
        readperson()
        print(peoplenamelist)
        input("Hit enter to go back to the menu")

    elif ans == '3':
        writedrink()
        print("Your drink has been added to the database. Thanks!")
        input("Hit enter to go back to the menu")
        
    elif ans == '4':
        readdrink()
        print(drinkslist)
        input("Hit enter to go back to the menu") 
        
    elif ans == '5':
        readperson()
        readdrink()
        for person in peoplenamelist:
            print("Hi "+ person)
            print(f"Here is our menu: {drinkslist}!")
            drinkorder = input("What drink you would like to order?")
            personsdrinkchoice = Order(person, drinkorder)
            orders.append(personsdrinkchoice)
        input("Hit Enter to return to main menu.")
        
    elif ans == '6':
        print(orders)
        input("Hit Enter to return to main menu.")
                
    elif ans == '7':
        for person in peoplenamelist:
            print("Hi" +person)
            drinkpref = input(f"Out of the following drinks: {drinkslist}, which is your preference?")
            personpref = Preferences(person, drinkpref)
            preflist.append(personpref)
        input("Hit Enter to return to main menu.")
        
    elif ans == '8':
        exit()
        
    else:
        print('Input not recognised')
