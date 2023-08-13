# Example of Sort:

#You are given a list of students, each represented as a
#dictionary with the following attributes: name, age, and gpa.
#Your task is to sort the list of students based on their GPA
#in descending order using the Insertion Sort algorithm.

def inserting_sort(arr):
     for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        #
        while j >= 0 and key ['gpa']>arr[j]['gpa']:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
def main():
    
    student = [
        {"name": "Alice", "age": 20, "gpa": 3.9},
        {"name": "Bob", "age": 22, "gpa": 3.7},
        {"name": "Charlie", "age": 21, "gpa": 4.0},
        {"name": "David", "age": 19, "gpa": 3.5},
              ]
    
    print("Original student:",student) 
    inserting_sort(student)
    print("------------")
    print("Sorted Student :")
        
    for arr in student:
        print(arr)
         
main()