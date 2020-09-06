
from core.logic import drinkslist 
from core.logic import peoplelist



class Person:
    def __init__(self, firstname, surname, age):
        self.firstname = firstname
        self.surname= surname
        self.age = age
        
    def addpeopletolist(self):
        info = (self.firstname.title(), self.surname.title(), self.age.title())
        peoplelist.append(info) 
        
    def __str__(self):
      return f"Name: {self.firstname.title()}, Surname: {self.surname.title()}, Age: {self.age.title()}"
  
    
class Drinks:
    def __init__(self, drinkname, colour, typedrink):
        self.drinkname = drinkname        
        self.colour = colour
        self.typedrink = typedrink    

    def __repr__(self):
      return f" Drink name: {self.drinkname.title()}, Colour: {self.colour.title()}, Type: {self.typedrink.title()}"
  
class Preferences:
    def __init__(self, name, drink):
        self.name = name
        self.drink = drink

    def __repr__(self):
        return f"Name: {self.name.title()}, Preference: {self.drink.title()}"
    
class Order:
    def __init__(self, personname, drink):
        self.personname = personname
        self.drink = drink
    def __repr__(self):
        return f" Name: {self.personname.title()}, Order: {self.drink.title()}"
    


