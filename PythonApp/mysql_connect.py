# Karolina Szafran-Belzowska, G00376368, 03/08/2020
# project Applied Databases, Higher Diploma in Science in Data Analytics

# This file is to connect to the "world" database in MySQL
# All the functions are called from the main python application file.


import pymysql

conn = None

def connect():  # Function to connect to world db
    global conn  # To connect to my SQL I have to enter my own credentials (username and password)
    conn = pymysql.connect(host = "localhost", user = "root", password = "25Szarfa", db = "world", cursorclass = pymysql.cursors.DictCursor)


# View People
# The user is shown the list of People in the world database, in groups of 2.

def ViewPeople(): 
    if(not conn):  # check if the function is connected, if not call the connect() function
        connect()

    query = "SELECT * from person"  # Select everything from person table.

    with conn:
        cursor = conn.cursor()   # activate the cursor
        cursor.execute(query)    # Execute the sql command
        while True:
            people = cursor.fetchmany(size = 2)   # Fetchmany is used to return two rows and store in people variable

            for p in people:   # loop through each row of data and print out the results
                print(p["personID"], "|", p["personname"], "|", p["age"])
            quit = input("-- Quit (q) --")
            if quit == "q":  # If the user enter "q" it will break out of loop.
                print("Done!, Back to the Main Menu.")
                break 

# View Countries by Independence Year
# The user is asked to enter a year.

def ViewCountriesByIndependenceYear(independence_year):
    if (not conn):
        connect() 
    query = "SELECT Name, Continent, IndepYear FROM country WHERE IndepYear = %s"  # "%s" is a placeholder for the number that will be passed in as input 
    with conn:                                                                     # It will print not everything from country table.
        try:
            cursor = conn.cursor() 
            cursor.execute(query, (independence_year))  # the input will be passed to sql command.  
            x = cursor.fetchall()  # returns all the rows that are equal to the user's input 
            return x 
                
        except pymysql.err.IntegrityError as e:   # Exception added to print an error.
            print(e)   
        except pymysql.err.InternalError as e:    # Other errors will ba printed here.
            print(e)

# Add New Person
# The user is asked to enter details of a new person as shown, 
# the person is then added to the world database. 
# (NOTE: The user should not be prompted to enter a personID).

def AddNewPerson(name, age):
    if (not conn):
        connect()
    query = "INSERT into person (personname, age) VALUES (%s, %s)"   # "%s" placeholder for user inputs
    with conn:                                                       # Just person name and age will be added.
        try:
            cursor = conn.cursor()
            cursor.execute(query, (name, age)) 
            conn.commit()   # Commit insertion to database
        except pymysql.err.IntegrityError as e: # Exception added to print out an error with the message
            print("*** ERROR ***:", name, "already exists. Back to the Main Menu.")   # Integrity error occurs when user will try to enter name already in db
        except pymysql.err.InternalError as e:   # Other errors will ba printed here.
            print(e)    
      
# View Countries by Name
# The user is asked to enter a country name or part thereof.
# Any country that contains those letters should be displayed.

def ViewCountriesByName(country_name):
    if (not conn):
        connect()
    query = "SELECT Name, Continent, Population, HeadOfState from country where Name like %s"               
    with conn:
        try:
            cursor = conn.cursor()
            cursor.execute(query, ("%"+country_name+"%"))  # Concatenate "%"" before and after user input to return any countries with partial matches
            return cursor.fetchall()
        except pymysql.err.IntegrityError as e: # Exception added here to print errors.
            print(e)   
        except pymysql.err.InternalError as e:    
            print(e)

# View Countries by population
# The user is asked to enter <, > or = and a number.
# If > and 800000000 were entered, the country’s code, name, continent and population 
# should be returned for all countries with a population of > 800000000. 
# The same logic would apply for < and =.

def ViewCountriesByPopulation():    
    if (not conn):
        connect()
    query = "SELECT * from country"
    with conn:     
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            x = cursor.fetchall()
            return x
        except pymysql.err.IntegrityError as e:  # Exception added here to print errors.
            print(e)   
        except pymysql.err.InternalError as e: 
            print(e)


def main():
    if (not conn): 
        try:
            connect() 
        except Exception as e:
            print("Problem connecting to database", e)


if __name__ == "__main__":   # The main function called.
	main()

