import pymysql



def writeperson():
    person_id = input('ID?')
    firstname = input("Add person name:")
    surname = input("Add surname:")
    age = input("Add person age:")
    connection = pymysql.connect(
		host='localhost',
		port = 3306,
		user ='root',
		password='12345',
		db = "databasetest",
		charset='utf8mb4')
    cursor = connection.cursor()
    query= ("INSERT INTO person (person_id, first_name, surname, age) VALUES(%s, %s, %s, %s)")
    args = (person_id, firstname, surname, age)
    cursor.execute(query,args)
    connection.commit()


def writedrink():
    drinkid = input('ID?')
    drinkname = input("Add drink name:")
    drinkcolour = input("Add drink colour:")
    drinktype = input("Add drink type (fizzy, hot, cold, etc.):")
    connection = pymysql.connect(
		host='localhost',
		port = 3306,
		user ='root',
		password='12345',
		db = "databasetest",
		charset='utf8mb4')
    cursor = connection.cursor()
    query= ("INSERT INTO drink (drink_id, drink_name, drink_colour, drink_type) VALUES(%s, %s, %s, %s)")
    args = (drinkid, drinkname, drinkcolour, drinktype)
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
	cursor.execute("SELECT person_id, first_name, age FROM person;")
	rows = cursor.fetchall()
	print (rows)
	for row in rows:
		print("ID: " + str(row[0]) + ", First name: " + row[1], "Surname: " + row[2], "Age: " + row[3])
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
	print (rows)
	for row in rows:
		print("Drink ID: " + str(row[0]) + ", Drink name: " + row[1], "Colour: " + row[2], "Type: " + row[3])
	cursor.close()
	connection.close()
 
