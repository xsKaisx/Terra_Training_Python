from mimetypes import init
class BankAccount():
    def __init__(self, accountNumber : int, name : str,balance : int):
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
        print(self.__dict__)
        print(self.balance)