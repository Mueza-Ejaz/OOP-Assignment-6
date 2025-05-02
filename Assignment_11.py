# Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.


class Book:
    total_books = 0

    @classmethod
    def increment_books_count(cls):
        cls.total_books += 1  # increase count by 1

    @classmethod
    def sum(cls):
        print(f"Total books: {cls.total_books}")

Book.increment_books_count() # 1st book
Book.increment_books_count() # 2nd book
Book.increment_books_count() # 3rd book
Book.increment_books_count() # 4th book

# Total books
Book.sum() 

# output: 
# Total books: 4




