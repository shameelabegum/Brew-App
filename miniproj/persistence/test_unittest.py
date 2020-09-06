import unittest

from core.classes import Drinks

expecteddrinkname = 'Fanta'
expectedcolour = 'Orange'
expectedtype = 'Fizzy'

class RunDrinkTest(unittest.TestCase):
     def test_drinks(self):
        self.assertEqual(drink.drinkname, expecteddrinkname)          
        self.assertEqual(drink.colour, expectedcolour)
        self.assertEqual(drink.typedrink, expectedtype)
        
drink = Drinks('Fanta', 'Orange', 'Fizzy')
if __name__ == '__main__':
    unittest.main()
    

    
from core.classes import Person
expectedfirstname = 'John'
expectedsurname = 'Blah'
expectedage = '23'     

class RunPersonTest(unittest.TestCase):
    def test_person(self):
        self.assertEqual(person.firstname, expectedfirstname)
        self.assertEqual(person.surname, expectedsurname)
        self.assertEqual(person.age, expectedage)
person = Person('John', 'Blah', '23')     
if __name__ == '__main__':
    unittest.main()
    
    
    
from core.classes import Order

expectedpersonname = 'Sasha'
expdrink = 'Orange'   

class RunOrderTest(unittest.TestCase):
    def test_order(self):
        self.assertEqual(order.personname, expectedpersonname)
        self.assertEqual(order.drink, expdrink)
         
order = Order('Sasha', 'Orange')

if __name__ == '__main__':
    unittest.main()


from core.classes import Preferences

expname = 'Sarah'
expecteddrinkpref = 'Lemonade'   

class RunPrefTest(unittest.TestCase):
    def test_pref(self):
        self.assertEqual(pref.name, expname)
        self.assertEqual(pref.drink, expecteddrinkpref)

pref = Preferences('Sarah', 'Lemonade')

if __name__ == '__main__':
    unittest.main()
    

