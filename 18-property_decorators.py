class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    # Getter method using @property
    @property
    def price(self):
        return self._price

    # Setter method using @price.setter
    @price.setter
    def price(self, new_price):
        if new_price >= 0:
            self._price = new_price
        else:
            print("Price can't be negative!")

    # Deleter method using @price.deleter
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price


# Testing
p = Product(100)
print("Initial price:", p.price)

p.price = 150  # Using setter to update
print("Updated price:", p.price)

del p.price   # Using deleter
# print(p.price)  # Agar yeh uncomment karo to error aayega kyun ke price delete ho chuka hai
