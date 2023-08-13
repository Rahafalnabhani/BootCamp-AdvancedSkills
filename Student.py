#inhertances by usig supper class to call the (name , age)
#From the person file i can take the name , age
# Only the aca
from Person import Person
class Student (Person):
    
    # Constructor
    def __init__(self,sname,sage,year):
        super().__init__(sname,sage)
        self.academic_year =year
        
    #def say_hi(self):
        #return f"Hello {self.name} as Student"