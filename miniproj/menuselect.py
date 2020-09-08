import csv
import os


from core.logic import clear_screen, readdrink_csv, readppl_csv, writefiles_csv, menu
from core.logic import drinkslist, peoplelist, orders, preflist
from core.classes import Person, Drinks, Order, Preferences

from core.sqll import readperson, readdrink, writeperson, writedrink


while True:
    clear_screen()
    menu()
    ans = input("Enter a number:")
    
    if ans == '1':
        # person_id = input('ID')
        # firstname = input("Add person name:")
        # surname = input("Add surname:")
        # age = input("Add person age:")
        # personinput = Person(firstname, surname, age)
        writeperson()
        # personinput.addpeopletolist()
        # writefiles_csv("people.csv", personinput)
        input("Hit enter to go back to the menu")
        
    elif ans == '2':
        # readppl_csv("people.csv")
        # for ppl in peoplelist:
        #     print(ppl)
        readperson()
        input("Hit enter to go back to the menu")

    elif ans == '3':
        # drinkname = input("What drink do you want to add?")
        # colour = input('What colour is the drink?')
        # typedrink = input('What type of drink is it?')
        # drinkinputtotal = Drinks(drinkname, colour, typedrink)
        # writefiles_csv("drinks.csv", drinkinputtotal)
        writedrink()
        input("Hit enter to go back to the menu")
        
    elif ans == '4':
    #     # readdrink_csv("drinks.csv")
    #     # for drink in csv.reader(drinkslist, delimiter=','):
    #     #     print(drink[0])
    #     #  input("Hit enter to go back to the menu") 
        readdrink()
        input("Hit enter to go back to the menu") 
        
    elif ans == '5':
        readdrink_csv("drinks.csv")
        readppl_csv("people.csv")
        for ppl in csv.reader(peoplelist, delimiter=','):
            print(ppl[0])
            print(drinkslist)
            drinkorder = input("What drink you would like to order:")
            personsdrinkchoice = Order(ppl, drinkorder)
        orders.append(personsdrinkchoice)
        input("Hit Enter to return to main menu.")
        
    elif ans == '6':
        print(orders)
        input("Hit Enter to return to main menu.")
        
    elif ans == '7':
        readppl_csv("people.csv")
        for person in peoplelist:
            print(person)
            drinkpref = input("Choose a drink for this person:")
            personpref = Preferences(person, drinkpref)
            preflist.append(personpref)
        print(preflist)
        input("Hit Enter to return to main menu.")
        
    elif ans == '8':
        exit()
        
    else:
        print('Input not recognised')



# /#      [1] Add a person
#         [2] Display a list of ALL PEOPLE
#         [3] Add drinks
#         [4] Get a list of ALL DRINKS
#         [5] Activate a ROUND of drinks
#         [6] Print ROUND results
#         [7] Enter drink PREFERENCES
#         [8] EXIT