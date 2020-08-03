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

if(choice == "1"):
    people = mysql_connect.ViewPeople()
    display_menu()


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
