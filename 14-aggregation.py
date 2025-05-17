# Employee class
class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Employee Name: {self.name}")

# Department class (Aggregation)
class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee  # Aggregation: reference to existing employee

    def show_details(self):
        print(f"Department: {self.department_name}")
        self.employee.show()


# Creating an Employee object
emp = Employee("Fatima")

# Creating a Department object with aggregation
dept = Department("IT", emp)

# Displaying details
dept.show_details()
