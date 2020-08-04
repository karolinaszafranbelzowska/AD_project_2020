# Karolina Szafran-Belzowska, G00376368, 03/08/2020
# project Applied Databases, Higher Diploma in Science in Data Analytics
# Write a python program that displays a main menu 


import mysql_connect



def main():
    display_menu()
    
    while True:
        choice = input("Choice:") 

# View People
# The user is shown the list of people in the world database, in groups of 2

        if (choice == "1"):
            people = mysql_connect.ViewPeople()
            display_menu()

# View Countries by Independence Year
# The user is asked to enter a year.

        elif (choice == "2"):
            print("     ")
            print("Countries by Independence Year")
            print("==============================") 
            independence_year = input("Enter Year: ")  
            year = mysql_connect.ViewCountriesByIndependenceYear(independence_year)   
            for y in year:                   
                print(y["Name"], "|", y["Continent"], "|", y["IndepYear"]) 
            display_menu()    

# Add New Person
# The user is asked to enter details of a new person as shown, 
# the person is then added to the world database. 
# (NOTE: The user should not be prompted to enter a personID).

        elif (choice == "3"):
            print("     ")
            print("Add New Person")
            print("==============")
            name = input("Name : ") 
            age = input("Age : ") 
            mysql_connect.AddNewPerson(name, age)
            display_menu()

# View Countries by Name
# The user is asked to enter a country name or part thereof.
# Any country that contains those letters should be displayed.

        elif (choice == "4"):
            print("")
            print("Countries by Name")
            print("=================")
            country_name = input("Enter Country Name: ")  
            country = mysql_connect.ViewCountriesByName(country_name)
            for c in country:    
                print(c["Name"], "|", c["Continent"], "|", c["Population"], "|", c["HeadOfState"])
            display_menu() 

# View Countries by population
# The user is asked to enter <, > or = and a number.
# If > and 800000000 were entered, the country’s code, name, continent and population 
# should be returned for all countries with a population of > 800000000. 
# The same logic would apply for < and =.




def display_menu():
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


if __name__ == "__main__":
	# execute only if run as a script 
	main()
