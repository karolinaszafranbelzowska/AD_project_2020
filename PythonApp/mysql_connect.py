
# Karolina Szafran-Belzowska, G00376368, 03/08/2020
# project Applied Databases, Higher Diploma in Science in Data Analytics

import pymysql

conn = None

def connect():
    global conn
    conn = pymysql.connect(host = "localhost", user = "root", password = "25Szarfa", db = "world", cursorclass = pymysql.cursors.DictCursor)


# View People
# The user is shown the list of People in the world database, in groups of 2.

def ViewPeople(): 
    if(not conn):
        connect()

    query = "SELECT * from person"

    with conn:
        cursor = conn.cursor()
        cursor.execute(query)
        while True:
            people = cursor.fetchmany(size = 2)

            for p in people:
                print(p["personID"], "|", p["personname"], "|", p["age"])
            quit = input("-- Quit (q) --")
            if quit == "q":
                print("Done!, Back to the Main Menu.")
                break 

# View Countries by Independence Year
# The user is asked to enter a year.

def ViewCountriesByIndependenceYear(independence_year):
    if (not conn):
        connect() 
    sql = "SELECT Name, Continent, IndepYear FROM country WHERE IndepYear = %s"   
    with conn:  
        try:
            cursor = conn.cursor() 
            cursor.execute(sql, (independence_year))    
            x = cursor.fetchall()
            return x
                
        except pymysql.err.IntegrityError as e:
            print(e)   
        except pymysql.err.InternalError as e:
            print(e)
      

def main():
    if (not conn): 
        try:
            connect() 
        except Exception as e:
            print("Problem connecting to database", e)


if __name__ == "__main__":
	main()

