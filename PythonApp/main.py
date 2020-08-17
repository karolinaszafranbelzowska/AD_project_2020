# Karolina Szafran-Belzowska, G00376368, 03/08/2020
# project Applied Databases, Higher Diploma in Science in Data Analytics

# Write a python program that displays a main menu 


# import mysql_connect to connect to MySQL database and all MySQL functions 
# to be called.

# import mongo_connect to connect MongoDB and all Mongo functions to be called.


import mysql_connect
import mongo_connect


# the main program
def main():
    display_menu()   # this function will display the menu.
    
    while True:    # while TRUE call the menu.
        choice = input("Choice:") 

# View People
# The user is shown the list of people in the world database, in groups of 2

        if (choice == "1"):
            people = mysql_connect.ViewPeople()
            display_menu()  # Back to the main menu.

# View Countries by Independence Year
# The user is asked to enter a year.

        elif (choice == "2"):
            print("     ")
            print("Countries by Independence Year")
            print("==============================") 
            independence_year = input("Enter Year: ")  # The user is asked to enter a year.
            # call the function from connect file
            year = mysql_connect.ViewCountriesByIndependenceYear(independence_year)   
            for y in year:   # for loop used to print all countries with certain year entered.
                             # If no countries became independent in the year entered nothing is shown.                
                print(y["Name"], "|", y["Continent"], "|", y["IndepYear"]) # print the country
            display_menu()    # Back to the main menu.

# Add New Person
# The user is asked to enter details of a new person as shown, 
# the person is then added to the world database. 
# (NOTE: The user should not be prompted to enter a personID).

        elif (choice == "3"):
            print("     ")
            print("Add New Person")
            print("==============")
            name = input("Name : ") # Enter a new person name.
            age = input("Age : ")  # Enter a new person age.
            mysql_connect.AddNewPerson(name, age)
            display_menu()     # Back to the main menu.

# View Countries by Name
# The user is asked to enter a country name or part thereof.
# Any country that contains those letters should be displayed.

        elif (choice == "4"):
            print("")
            print("Countries by Name")
            print("=================")
            country_name = input("Enter Country Name: ")   # The user is asked to enter the contry name.
            country = mysql_connect.ViewCountriesByName(country_name)  # Get the country data from country table.
            for c in country:   # for loop to print all countries the user asks. 
                print(c["Name"], "|", c["Continent"], "|", c["Population"], "|", c["HeadOfState"])
            display_menu()     # Back to the main menu.

# View Countries by population
# The user is asked to enter <, > or = and a number.
# If > and 800000000 were entered, the country’s code, name, continent and population 
# should be returned for all countries with a population of > 800000000. 
# The same logic would apply for < and =.

        elif (choice == "5"):
            print("   ")
            print("Countries by Pop")
            print("================")
            enter = input("Enter < > or =:")   # The user is asked to enter <, > or =.
            while enter not in ("<", ">", "="):  #  while none of these 3 signs are entered loop will continue to run and ask for valid input
                enter = input("Enter < > or =:")
                if enter in ("<", ">", "="):  # when valid input is entered loop break and move on to take next input.
                    break
            run = int(input("Enter population:")) # The user is asked to enter population as integer.
            populations = mysql_connect.ViewCountriesByPopulation()   # function to retrieve all data from country table 
            for p in populations:  # loop through all rows of table and check whole data as below        
                if enter == "<":   # return countries with population less than user input.                  
                    if int(p["Population"]) < int(run):   # Convert to integers
                        print(p["Code"],"|", p["Name"], "|", p["Continent"], "|", p["Population"])
                elif enter == "=":   # return countries with population equal to user input.                
                    if int(p["Population"]) == int(run):
                            print(p["Code"],"|", p["Name"], "|", p["Continent"], "|", p["Population"])
                elif enter == ">":     # return countries with population greater than user input.                
                    if int(p["Population"]) > int(run):
                            print(p["Code"],"|", p["Name"], "|", p["Continent"], "|", p["Population"])
            display_menu()     # Back to the main menu.

# Find Students by Address
# The user is asked to enter an address.
# All details of students in the docs collection in the proj20DB database with that address asre shown.
# NOTE: if a student does not have a qualifications attribute, nothing should be shown. But if he/she 
# has a qualifications attribute this must be shown.

        elif (choice == "6"):
            print("   ")
            print("Find Students by Addresses")
            print("==========================")
            Address = input("Enter Address: ")   # Enter an address.
            students = mongo_connect.find_students(Address)   # Call the FIND function from mongo_connect file. Pass the address into the function.
            for s in students:    # loop through all rows of table and check whole data.
                print(s["_id"], "|", s["details"] ["name"], "|",  s["details"] ["age"], "|", s["qualifications"])    # Print students details.
            display_menu()    # Back to the main menu.

# Add New Course
# The user is asked to enter an _id, Name and Level for a new course, 
# which is then added to the “docs” collection in the “proj20DB” database.

        elif (choice == "7"):
            print("   ")
            print("Add New Course: ")
            print("==============")
            ID = input("_id:")   # The user is asked to enter details of a new course. This input will be passed to the function below.
            Name = input("Name:")
            Level = input("Level:")
            mongo_connect.AddNewCourse(ID, Name, Level) # Call the function to add new course from mongo_connect file.
            display_menu()    # Back to the main menu.

# x - Exit Application, Anything Else
# The program terminates and anything else the menu is shown again.

        elif (choice == "x"):
            break;        # Exit appication if the user enter "x".

        else:
            display_menu()

# The main menu shown as Python program specyfication 
# Taken from lecture Applied Databases module, Gerard Harrison, GMIT, Higher Diploma in Data Analytics.

def display_menu():
# Menu as in project specyfication.
    print("    ")
    print("MENU")
    print("=====")
    print("1 - View People")
    print("2 - View Countries by Intependence Year")
    print("3 - Add New Person")
    print("4 - View Countries by name")
    print("5 - View Countries by populations")
    print("6 - Find Students by Address")
    print("7 - Add New Courses")
    print("x - Exit application")


if __name__ == "__main__":   # The main function called.
	main()
