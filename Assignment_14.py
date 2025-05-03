# Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.



class Employee:
    def __init__(self, name):
        self.name = name

    def show_employee(self):
        return f"Employee Name: {self.name}"    

class Department:
    def __init__(self,department_name, employee):
        self.department_name = department_name
        self.employee = employee

    def show_department(self):
        return f"Department Name: {self.department_name}, {self.employee.show_employee()}"


emp_1 = Employee("Mueza Ejaz") 
department_1 = Department("HR", emp_1)

print(department_1.show_department())  # Output: Department Name: HR, Employee Name: Mueza Ejaz
        




        