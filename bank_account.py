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

from time import sleep


class BankAccount():
    def __init__(self, account_number: int, name: str, balance: int) -> None:
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self):
        """ Manage deposit action """
        pass

    def withdrawal(self, withdraw_amount):
        """ Manage withdrawal action """
        self.balance -= withdraw_amount
        return """
            Withdraw amout: {}
            Balance remain: {}
        """.format(withdraw_amount, self.balance)
        

    def bank_fee(self):
        """ Manage bank fee action 
            bank fee == 5% balance
        """
        return (self.balance * 5 / 100)

    def display(self):
        """ show account detail """
        return """
            Bank Accout detail:
                - Account number: {}
                - Owner's name: {}
                - Balance: {}
        """.format(self.account_number, self.name, self.balance)

clint_nguyen = BankAccount(78264, "Clint Nguyen", 2000000)
# print(clint_nguyen.withdrawal(500000))
# print(clint_nguyen.display())

class CashRegister():
    cart = []

    def __init__(self) -> None:
        pass

    def purchase_item(self, list_item: list):
        """ add item to cart """
        """ no RetailItem exist, therefore i hardcode for item """
        self.cart = list_item
        return list_item

    def get_total(self):
        """ sum all price """
        """ sample_list_item = [
                ("áo phông", 100000),
                ("quần xì", 120000)
            ]
        """
        only_prices = []
        total_price = 0

        for item in self.cart:
            only_prices.append(item[1])
        
        for price in only_prices:
            total_price += price

        return total_price
        
    def show_items(self):
        """ show item in cart """
        only_prices = []
        total_price = 0
        result = {}

        for item in self.cart:
            only_prices.append(item[1])
            result[item[0]] = item[1]

        for price in only_prices:
            total_price += price

        result['Total'] = total_price

        return result

    def clear(self):
        """ clear cart """
        self.cart = []
        if len(self.cart) == 0:
            return "Cart is empty"
        return self.cart

    def sell_item(self):
        """ time to pay """
        balance = clint_nguyen.balance
        if balance >= self.get_total():
            print("payment in processing...")
            payment = clint_nguyen.withdrawal(self.get_total())
            print("Payment is completed")
            print(payment)
        else:
            print("Your balance is not enough to continue this transaction")


list_item = [
    ("áo phông", 100000),
    ("quần xì", 120000)
]


order_01 = CashRegister()
print(order_01.purchase_item(list_item))
# print(order_01.get_total())
# print(order_01.cart)
# print(order_01.show_items())
# print(order_01.clear())
# print(order_01.cart)
print(order_01.sell_item())
print(clint_nguyen.display())