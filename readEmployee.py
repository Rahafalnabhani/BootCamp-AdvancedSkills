# Exercise:
import pandas as pd

class Employee:
    def __init__(self,name,emp_id,salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
    def read_employee(filename):
        employee = []
        try:
             for index, row in df.iterrows():
                 name = row['Name']
                 emp_id = row['ID']
                 salary = row['Salary']
                 employee = Employee(Name=Name , ID=ID , Salary=Salary)
                 employee.append(employee)
        except Excetion as Employee:
            print (f"Error While reading : {Employee}")
        return employee
        
    def binary_search_employees(employees, target_id):
        left, right = 0, len(employees) - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_emp_id = employees[mid].idd
            if mid_emp_id == target_id:
                return employees[mid]
            elif mid_emp_id < target_id:
                left = mid + 1
            else:
                right = mid - 1
        return None


    if __name__ == "__main__":
        excel_file = "Employee.xlsx"

        employees = read_employees_from_excel(excel_file)
        employees.sort(key=lambda x: x.idd)

        target_id = 12  
        result = binary_search_employees(employees, target_id)
        if result:
            print(f"Employee found: Name: {result.Name}, ID: {result.ID}, Salary: {result.Salary}")
        else:
            print("Employee not found.")