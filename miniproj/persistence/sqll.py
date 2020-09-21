import pymysql
from core.logic import drinkslist, peoplenamelist


def writeperson():
    firstname = input("Add person name:")
    surname = input("Add surname:")
    age = input("Add person age:")
    #peoplenamelist.append(firstname)
    connection = pymysql.connect(
		host='localhost',
		port = 3306,
		user ='root',
		password='12345',
		db = "databasetest",
		charset='utf8mb4')
    cursor = connection.cursor()
    query= ("INSERT INTO person (first_name, last_name, age) VALUES(%s, %s, %s)")
    args = (firstname, surname, age)
    cursor.execute(query,args)
    connection.commit()
    
    
def writedrink():
    drinkname = input("Add drink name:")
    drinkcolour = input("Add drink colour:")
    drinktype = input("Add drink type (fizzy, hot, cold, etc.):")
    #drinkslist.append(drinkname)
    connection = pymysql.connect(
		host='localhost',
		port = 3306,
		user ='root',
		password='12345',
		db = "databasetest",
		charset='utf8mb4')
    cursor = connection.cursor()
    query= ("INSERT INTO drink (drink_name, drink_colour, drink_type) VALUES(%s, %s, %s)")
    args = (drinkname, drinkcolour, drinktype)
    cursor.execute(query,args)
    connection.commit()


def readperson():
	connection = pymysql.connect(
		host =	"localhost",
		port = 3306,
		user = "root",
		password = "12345",
		db = "databasetest",
		charset='utf8mb4'
		)
	cursor = connection.cursor()
	cursor.execute("SELECT person_id, first_name, last_name, age FROM person;")
	rows = cursor.fetchall()
	#print (rows)
	for row in rows:
		peoplenamelist.append(str(row[1]))
		#print("First name: " + row[1], "\n  Surname: " + row[2], "\n  Age: " + str(row[3]))
	cursor.close()
	connection.close()
 
def readdrink():
	connection = pymysql.connect(
		host =	"localhost",
		port = 3306,
		user = "root",
		password = "12345",
		db = "databasetest",
		charset='utf8mb4',)

	cursor = connection.cursor()
	cursor.execute("SELECT drink_id, drink_name, drink_colour, drink_type FROM drink")
	rows = cursor.fetchall()
	for row in rows:
		drinkslist.append(str(row[1]))
	#	print("Drink name: ", row[1], "\n   Colour: " + row[2], "\n   Type: " + row[3])
	cursor.close()
	connection.close()
