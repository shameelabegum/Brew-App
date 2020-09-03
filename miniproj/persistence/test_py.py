
import pytest
from classes import Drinks

expecteddrinkname = 'Fanta'
expectedcolour = 'Orange'
expectedtype = 'Fizzy'

class TestRunDrinkTest():
     def test_drinks(self):
        assert expecteddrinkname == drink.drinkname
        assert expectedcolour == drink.colour
        assert expectedtype == drink.typedrink

drink = Drinks('Fanta', 'Orange', 'Fizzy')



from classes import Person

expectedfirstname = 'John'
expectedsurname = 'Blah'
expectedage = '23'     

class TestRunPersonTest():
    def test_person(self):
        assert person.firstname == expectedfirstname
        assert person.surname == expectedsurname
        assert person.age == expectedage
person = Person('John', 'Blah', '23')     

    
    
from classes import Order

expectedpersonname = 'Sasha'
expdrink = 'Orange'   

class TestRunOrderTest():
    def test_order(self):
        assert order.personname == expectedpersonname
        assert order.drink == expdrink
         
order = Order('Sasha', 'Orange')


from classes import Preferences

expname = 'Sarah'
expecteddrinkpref = 'Lemonade'   

class TestRunPrefTest():
    def test_pref(self):
        assert pref.name == expname
        assert pref.drink == expecteddrinkpref

pref = Preferences('Sarah', 'Lemonade')

