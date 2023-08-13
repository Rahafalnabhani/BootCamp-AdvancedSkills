class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):   # Add to the end
        self.items.append(item)

    def dequeue(self):   #delete from the front 
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty, cannot dequeue an item.")

    def peek(self):  # see what is the first element
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty, cannot peek an item.")

    def size(self):
        return len(self.items)