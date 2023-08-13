#Create Class
class Person():
    #Costractor to create object
    #Initialize instance variables
    # All are same
    # To pass the age 
    def __init__(self, name, age,salary):
        self.name = name
        self.age= age
        self.salary=salary
    def bounce(self):
        b= self.salary*0.005
        return b
    def say_hi(self):
        return f"Hello {self.name} as Student"
    #Use term of encapsualtion
    def get_name(self):
            return self.name
    def get_age(self):
            return self.age
       
    # Setter / Mutotur Method
    def set_name(self,newName):
            self.name = newName
    def set_age(self,newAge):
            self.age = newAge
    def run(self):
            print(self.name, "is running")
       
        #For the information
    def descrip(self):
            return f"Person name {self.name} is {self.age} years old"
        
    def laugh(self):
            print(self.name, "hahahahahaha")

