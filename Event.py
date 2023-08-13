# Exercise: Managing a Guest List with a Stack

class Event():
    def __init__(self,name,age,phone):
        self.name=name
        self.age=age
        self.phone=phone
        
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getPhone(self):
        return self.phone
    
     #We can update or change
    def set_name(self,newName):
            self.name = newName
    def set_age(self,newAge):
            self.age = newAge
    def set_phone(self,newPhone):
            self.phone = newPhone
            
            
    def __init__(self):
        self.items = []      #constructor to make the stack ready

    def is_empty(self): # To check if the stack has no items
        return len(self.items) == 0

    def push(self, item):   # To Add
        self.items.append(item)

    def pop(self):         # To Remove from the end of the list                                                                                                                                                                                                          
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty, cannot pop an item.")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]   #Last item 
        else:
            raise IndexError("Stack is empty, cannot peek an item.")

    def size(self):
        return len(self.items)