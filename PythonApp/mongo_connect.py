# Karolina Szafran-Belzowska, G00376368, 04/08/2020
# project Applied Databases, Higher Diploma in Science in Data Analytics

import pymongo

myclient = None

def connect():  
    
    global myclient   
    myclient = pymongo.MongoClient()
    myclient.admin.command('ismaster')   # to check if mongo succesfully connected        

# Find Students by Address
# The user is asked to enter aan address.
# All details of students in the docs collection in the proj20DB database with that address asre shown.
# NOTE: if a student does not have a qualifications attribute, nothing should be shown. But if he/she 
# has a qualifications attribute this must be shown.

def find_students(Address):
    if (not myclient):            
        connect()
    mydb = myclient["proj20DB"]    # DATABASE and COLLECTION
    docs = mydb["docs"]  
   
    query = [{"$match":{"details.address":{"$eq": Address}}}, {"$project": {"details.name":1, "details.age":1, "qualifications":{"$ifNull":["$qualifications", " "]}}}]
    people = docs.aggregate(query)  
    return people

# Add New Course
# The user is asked to enter an _id, Name and Level for a new course, 
# which is then added to the “docs” collection in the “proj20DB” database.

def AddNewCourse(ID, Name, Level):
    if (not myclient): 
             connect() 
    mydb = myclient["proj20DB"]  
    docs = mydb["docs"]    
    newCor = {"_id" : ID, "name" : Name, "level" : Level}  # Document which will be inserted is called newCor
    try:
        docs.insert_one(newCor) # try to insert a newCor into MongoDB 
    except pymongo.errors.DuplicateKeyError as e:  
        print("*** ERROR ***: _id DATA already exists, please try again.") 
    except Exception as e: 
        print("Error:", e)

def main():
    if (not myclient): 
        try:
            connect() 
        except Exception as e:
            print("Problem connecting to database", e)

if __name__ == "__main__":
	main()




