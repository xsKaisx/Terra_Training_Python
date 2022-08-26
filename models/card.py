class Card:
    card_suits = ["spades","hearts","diamond","clubs"]
    card_values = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    def __init__(self,t:str,v:str):
        self.card_suit = t
        self.card_value = v
    
    def __str__(self):
        return "{} {}".format(self.card_suit,self.card_value)