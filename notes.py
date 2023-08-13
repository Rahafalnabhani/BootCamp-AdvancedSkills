#add comments LIFO
#Think how to add/apply is_FULL??
# The End i the Top
class Stack:
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