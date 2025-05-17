class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

# Object create karo with factor 5
mult = Multiplier(5)

# Check kren object callable hai ya nahi
print(callable(mult))  # True ayega

# Object ko function ki tarah call kiya
result = mult(10)  # 10 ko 5 se multiply karega
print(result) 
