
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

if __name__ == "__main__":
	main()

