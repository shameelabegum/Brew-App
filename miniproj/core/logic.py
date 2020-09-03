import os
import csv

drinkslist = []
peoplelist = []
orders = []
preflist = []

def clear_screen():
    os.system("cls")
    
def readppl_csv(file_name):
    with open(file_name) as file:
        read_file = csv.reader(file, delimiter=',')
        inlines = file.readlines()
    for linep in inlines:
        peoplelist.append(linep)
        
def readdrink_csv(file_name):
    with open(file_name) as file:
        read_file = csv.reader(file, delimiter=',')
        inlines = file.readlines()
    for linep in inlines:
        drinkslist.append(linep)   
            
def writefiles_csv(file_name, inputt):
    with open(file_name, "a") as file:
        write_file = csv.writer
        file.write(f"\n{inputt}") 
def menu():
    clear_screen()
    menu_text = """
    Please, select an option below by entering a number:
        [1] Add a person
        [2] Display a list of ALL PEOPLE
        [3] Add drinks
        [4] Get a list of ALL DRINKS
        [5] Activate a ROUND of drinks
        [6] Print ROUND results
        [7] Enter drink PREFERENCES
        [8] EXIT
        """
    print(menu_text)        
