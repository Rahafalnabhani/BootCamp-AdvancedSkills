from Person import Person
from Student import Student
from Teacher import Teacher
def main():
    Rahaf = Person("Rahaf AL-Nabhani",21)
    person2= Person("Hamed")
    print(Rahaf.say_hi())
    print(person2.say_hi())
    #For Student
    std1 = Student("Meera",18,2012)
    std2 = Student("Maram",21,2021)
    std1.run()
    #For Teacher
    tec1=Teacher("Hamza",50,40)
    tec2=Teacher("Latifa",30,50)
    tec1.laugh()
    
    print(person2.descrip())
    print(Rahaf.get_name())
    #Create new name
    Rahaf.set_name("Rahaf Hamed")
    print(Rahaf.get_name())
    print(Rahaf.descrip())
    Rahaf.run()
    Rahaf.laugh()
    person2.laugh()
    
    print(std1.say_hi())
    #Another way to call the Student names
    print(Student.say_hi(std2))
    
    print(tec1.say_hi())
    print(tec2.say_hi())
main()