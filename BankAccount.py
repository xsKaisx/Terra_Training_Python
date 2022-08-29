from mimetypes import init
class BankAccount():
    def __init__(self, accountNumber : str, name : str,balance : int):
        if type(balance) != int : 
            raise TypeError("Datatype of balance must be integer!")
        elif balance <= 0 :
            raise TypeError("Balance must be greater than 0 !")
        elif type(name) != str :
            raise TypeError("Datatype of name must be string!")
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def deposit(self,amount_de):
        self.balance = self.balance + amount_de
    def Withdraw(self,amount_with):
        self.balance = self.balance - amount_with
    def bankFee(self):
        self.balance = self.balance - self.balance*0.05
    def display(self):
        print(("Bank balance is : {0:,} VND".format(self.balance)))