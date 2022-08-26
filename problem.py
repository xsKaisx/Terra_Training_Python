"""
Bank account
- Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
- Create a constructor with parameters: accountNumber, name, balance.
- Create a Deposit() method which manages the deposit actions.
- Create a Withdrawal() method  which manages withdrawals actions.
- Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
- Create a display() method to display account details.
- Give the complete code for the  BankAccount class.

Cash machine: Cash machine và Bank account phải làm việc tương tác với nhau hơp lí
This exercise assumes that you have created the RetailItem class for Programming
Exercise 5. Create a CashRegister class that can be used with the RetailItem class. The CashRegister class should be able to internally keep a list of RetailItem objects. The class should have the following methods:
• A method named purchase_item that accepts a RetailItem object as an argument.

Each time the purchase_item method is called, the RetailItem object that is passed as an argument should be added to the list.
• A method named get_total that returns the total price of all the RetailItem objects stored in the CashRegister object’s internal list.
• A method named show_items that displays data about the RetailItem objects stored in the CashRegister object’s internal list.
• A method named clear that should clear the CashRegister object’s internal list.
* A method named sell_item that sells item to the Bank Account above:
        * This method returns a tuple (sale_status, change, amount)
            - sale_status: SUCCESS / FAILED 
            - change: float : tien thoi
            - amount: float : tien nhan
      ****  Khi SUCCESS, Bank Account phai duoc update
	
Demonstrate the CashRegister class in a program that allows the user to select several items for purchase. When the user is ready to check out, the program should display a list of all the items he or she has selected for purchase, as well as the total price.

"""

"""
------------------------------------------------------------------------

Fraction

* Make a class Fraction that contains two instance variables, nr and dr (nr stands for numerator and dr for denominator). Define an __init__ method that provides values for these instance variables. Make the denominator optional by providing a default argument of 1. In the __init__ method, make the denominator positive if it is negative. For example  -2/-3 should be changed to 2/3 and 2/-3 to -2/3. Write a method named show that prints numerator, then '/' and then the denominator


- Define a method named multiply that multiples two Fraction instance objects. For multiplying two fractions, you have to multiply the numerator with numerator and denominator with the denominator.
- Create a new instance object that is the product of the two fractions and return it. Write your method in such a way that it supports multiplication of a Fraction by an integer also
- Define a method named add to add two Fraction instance objects. Sum of two fractions n1/d1 and n2/d2 is (n1*d2 + n2*d1) / (d1*d2). This method should also support addition of a Fraction by an integer
- Create a function to find the highest common factor of two numbers and make it a static method
- Write a private instance method _reduce that reduces a fraction to its lowest terms. To reduce a Fraction to its lowest terms you have to divide the numerator and denominator by the highest common factor. Call this method in __init__and also call it on the resultant fraction in methods multiply and add

"""

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