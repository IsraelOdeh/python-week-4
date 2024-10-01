# Create a Python class named Person.
class Person:
    
    # Define the contructor function
    def __init__(self,name,age,gender): 
        self.name = name
        self.age = age
        self. gender = gender
        return(None)
    
    # Define introduce function
    def introduce(self):
        print("Hello there, I am " + self.name+ " i'm a " + str(self.age) + " year old " + self.gender)

# Retrieve user inputs
name = str(input("Enter Your Name: "))
age = int(input("Enter Your Age: "))
gender = str(input("Enter Your Gender: "))

# Create Object from class
Citizen = Person(name,age,gender)

# Call Object's method
Citizen.introduce()