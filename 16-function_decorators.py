# Decorator function
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()  # Original function call
    return wrapper

# Using the decorator
@log_function_call
def say_hello():
    print("Hello!")

# Calling the decorated function
say_hello()
