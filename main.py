from BankAccount import BankAccount
from CashRegister import CashRegister 
from Retailitem import Retailitem  
######################################################
muahang1 = Retailitem("io11","bánh bao",20000,0)
muahang2 = Retailitem("io12","bánh giò",15000,0)
muahang3 = Retailitem("io13","bánh tiêu",5000,0)
thungan = CashRegister()
thungan.purchase_item(muahang1)
thungan.purchase_item(muahang2)
thungan.purchase_item(muahang3)
thungan.get_total()
thungan.show_items()
thungan.clear()
ACB_bank = BankAccount("12345","Phát",3000000)
thungan.sell_item()

