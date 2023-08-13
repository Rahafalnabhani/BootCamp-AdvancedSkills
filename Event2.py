from Event import Event
def main():
    event_stack = Stack()

guest = int(input("Enter: "))

if guest == 1:
    Name = input("Enter your Name : ")
    Age = input("Enter your Age : ")
    Phone = input ("Enter Your Phone Number : ")
    person = Person(Name, Age,Phone)
    guest_stack.push(person)
    print (f"Mr {Name} you have been added to the guest list..")

elif guest == 2:
    if not guest_stack.is_empty():
        removed_person = guest_stack.pop()
        print (f"Removed {removed_person.Name} from the guest list.")
    else:
        print("Guest list is empty.")

elif choice == 3:
    print (f"Total number of guests: {guest_stack.size()}")

main()