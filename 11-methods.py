class Book:
    # Class variable to store total number of books
    total_books = 0

    def __init__(self, title):
        self.title = title
        # Jab bhi new book banegi, count barh jayega
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1


# Testing the class
book1 = Book("Python Basics")
book2 = Book("Advanced Python")

print("Total books added:", Book.total_books)
