"""
------------------------------------------------------------------------
Bank Account

Make a class that represents a bank account. Create four methods named set_details, display, withdraw and deposit. In the set_details method, create two instance variables : name and balance. The default value for balance should be zero. In the display method, display the values of these two instance variables. Both the methods withdraw and deposit have amount as parameter. Inside withdraw, subtract the amount from balance and inside deposit, add the amount to the balance. Create two instances of this class and call the methods on those instances.

Delete the set_detail() method and create an  __init__ method

Book
Create a class named Book with an __init__ method. Inside the __init__ method, create the instance variables isbn, title, author, publisher, pages, price, copies
Create these four instance objects from this class and write a method display that prints the isbn, title, price and number of copies of the book
Write a method named in_stock that returns True if number of copies is more than zero, otherwise it returns False
Create a list named books that contains the 4 Book instance objects that you have created in 2.a. Iterate over this list using a for loop and call display() for each object in the list
Write a list comprehension to create another list that contains title of books written by specific author.
Create a property named price such that the price of a book cannot be less than 50 or more than 1000
"""

class BankAccount():
    def __init__(self, name: str, balance: int = 0) -> None:
        self.name = name
        self.balance = balance

    def display(self):
        """ display the values of two instance variables """
        return self.name, self.balance

    def withdraw(self, amount: int):
        self.balance -= amount
        return self.balance

    def deposit(self, amount: int):
        self.balance += amount
        return self.balance

clint = BankAccount("Clint", 2000000)
# print(clint.display())

class Book():
    count = 0
    def __init__(self, isbn: bool, title: str, author: str, publisher: str, pages: int, price: int, copies: int) -> None:
        self.isbn = isbn 
        self.title = title 
        self.author = author 
        self.publisher = publisher 
        self.pages = pages 
        self.price = price 
        self.copies = copies
        Book.count += 1

    def display(self):
        return """
            isbn: {}
            title: {}
            price: {}
            number of copies: {}
            count: {}
        """.format(self.isbn, self.title, self.price, self.copies, self.count)
    
    def in_stock(self):
        if self.copies > 0:
            return True
        else: 
            return False

book_1 = Book(True, "Làm đĩ", "Vũ Trọng Phụng", "Nhà xuất bản Trần Duy Hưng", 120, 100000, 1000)
book_2 = Book(True, "Làm gái", "Đồ Sơn", "Nhà xuất bản Đồ Sơn", 120, 100000, 1000)
book_3 = Book(True, "Làm ngành", "Quất Lâm", "Nhà xuất bản Quất Lâm", 120, 100000, 1000)
book_4 = Book(True, "Lấy lỗ làm lãi", "Cầu Thị Nghè", "Nhà xuất bản Cầu Thị Nghè", 120, 100000, 1000)
# print(book_1.display())

# book_list = [book_1, book_2, book_3, book_4]

# for book in book_list:
#     print(book.display())

# author_book = [book for book in book_list if book.author == "Đồ Sơn"]

# for book in author_book:
#     print(book.display())