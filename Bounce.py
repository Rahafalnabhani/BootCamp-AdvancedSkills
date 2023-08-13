from Person import Person
from Teacher import Teacher
def main ():
    p1 =Person("Ahmed",24,1500)
    t1 =Teacher("Ali",24,23,1500)
    print(p1.descrip())
    print(p1.bounce())
    
    print(t1.descrip())
    print(t1.bounce())
    
main()