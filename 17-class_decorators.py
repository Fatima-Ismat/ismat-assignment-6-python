# Class decorator function
def add_greeting(cls):
    # Decorator ke andar hum class mein naya method add kar rahe hain
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

# Applying the decorator to Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Testing
p = Person("Fatima")
print(p.greet())
