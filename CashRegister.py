class CashRegister():
    def __init__(self) :
        self.retail_list = []
    def purchase_item(self,obj):
        self.retail_list.append(obj)
    def get_total(self):
        item_list_price = []
        for element in self.retail_list:
            item_list_price.append(element.item_price)
        self.total_price = sum(item_list_price)
        print("Total price of all items is : {0:,} VND".format(self.total_price))
        return self.total_price
    def show_items(self):
        print(repr(self.retail_list))
    def clear(self):
        self.retail_list.clear()
    def sell_item(self,obj_bank,amount) -> tuple :
        self.amount = amount
        if self.amount > self.total_price and obj_bank.balance > self.amount :
            self.sale_status = "SUCCESS"
        else : 
            self.sale_status = "FAILED"
        self.change = self.amount - self.total_price
        obj_bank.withdraw(self.total_price)
        return tuple((self.sale_status,self.change,self.amount))

    