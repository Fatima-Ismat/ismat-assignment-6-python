class Person:
     def __init__(self, name):
          self.name = name
          print(f"person created with the name: {self.name}")

class Teacher(Person):
     def __init__(self, name, subject):
          super().__init__(name)
          self.subject = subject
          print(f"Teacher teaches: {self.subject}")

t = Teacher("Sir Hamza Syed", "GIAIC Python Course")


