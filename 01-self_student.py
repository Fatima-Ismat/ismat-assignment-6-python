class Student:
     def __init__(self, name, marks):
          self.name = name
          self.marks = marks

     def display(self):
          print(f"Student Name: {self.name} \nMarks: {self.marks}")
          
Student1 = Student("Ismat", 85)
Student1.display()
          
