class Retailitem():
    def __init__(self,item_id : str,item_name : str,item_price : int,discount : int):
        self.item_id = item_id
        self.item_name = item_name
        self.item_price = item_price
        self.discount = discount
    def __repr__(self):
        return f'Retailitem("{self.item_id}","{self.item_name}",{self.item_price},{self.discount})'