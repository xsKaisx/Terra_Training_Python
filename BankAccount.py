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
    def withdraw(self,amount_with):
        if amount_with > self.balance : 
            raise TypeError("Withdraw amount must be less than balance !")
        self.amount_with = amount_with
        def bankFee(nice):
            self.bankfee = nice*0.05
            return self.bankfee
        self.balance = self.balance - (self.amount_with+ bankFee(self.amount_with))
        print("Withdraw fee is  : {0:,} VND".format(self.bankfee))
    def display(self):
        print("Bank balance is : {0:,} VND".format(self.balance))