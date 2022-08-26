#from typing import literal
class CashRegister():
    def __init__(self) :
        self.retail_list = []
    def purchase_item(self,obj):
        self.retail_list.append(obj)
    def get_total(self):
        item_list_price = []
        for element in self.retail_list:
            item_list_price.append(element.item_price)
        print("Total price of all items is : {0:,} VND".format(sum(item_list_price)))
    def show_items(self):
        for element in self.retail_list:
            print(element.__dict__)
    def clear(self):
        self.retail_list = []
    def sell_item(self) -> tuple :
        self.sale_status = "SUCCESS"
        self.change = 5000
        self.amount = 20000
        return print(tuple((self.sale_status,self.change,self.amount)))