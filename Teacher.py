from Person import Person 
class Teacher(Person):
    
    def __init__(self,sname,sage,experiance,salary):
        super().__init__(sname,sage,salary)
        self.experiance_year =experiance
        
    def bounce(self):
        teacherB = super().bounce()*2
        return teacherB
        
    def say_hi(self):
        print(super().say_hi())
        return f"Hello {self.name} as Teacher"