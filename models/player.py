class Player:
    def __init__(self,name:str,index:int,current_cards:list = []):
        self.name = name
        self.index = index
        self.current_cards = current_cards

    def __str__(self):
        return "Player {} has index {} and cards in hands {}".format(self.name,self.index,self.current_cards)