
import pytest
from core.classes import Drinks


expecteddrinkname = 'Fanta'
expectedcolour = 'Orange'
expectedtype = 'Fizzy'

class TestRunDrinksTest():
     def test_drinks(self):
        assert expecteddrinkname == drink.drinkname
        assert expectedcolour == drink.colour
        assert expectedtype == drink.typedrink

drink = Drinks('Fanta', 'Orange', 'Fizzy')



from core.classes import Person

expectedfirstname = 'John'
expectedsurname = 'Blah'
expectedage = '23'     

class TestRunPersonsTest():
    def test_person(self):
        assert person.firstname == expectedfirstname
        assert person.surname == expectedsurname
        assert person.age == expectedage
person = Person('John', 'Blah', '23')     

    
    
from core.classes import Order

expectedpersonname = 'Sasha'
expdrink = 'Orange'   

class TestRunOrdersTest():
    def test_order(self):
        assert order.personname == expectedpersonname
        assert order.drink == expdrink
         
order = Order('Sasha', 'Orange')


from core.classes import Preferences

expname = 'Sarah'
expecteddrinkpref = 'Lemonade'   

class TestRunPrefsTest():
    def test_pref(self):
        assert pref.name == expname
        assert pref.drink == expecteddrinkpref

pref = Preferences('Sarah', 'Lemonade')

