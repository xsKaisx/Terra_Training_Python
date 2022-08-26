from deck import Deck
from datetime import datetime
class Game:
    manager = {}
    def __init__(self,name:str,deck:Deck,max_players:int = 4):
        self.name = name
        self.created_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.deck = deck
        self.max_players = max_players
    
    def __str__(self):
        return "Game {} created on {} with {} players".format(self.name,self.created_at,self.max_players)

    def distribute_card(self):
        list_players = {}
        for j in range(13):
            for i in range(1,self.max_players+1):
                if ('p'+str(i)) in list_players.keys():
                    list_players['p'+str(i)].append(self.deck.release_card())
                else:
                    list_players['p'+str(i)] = []
                    list_players['p'+str(i)].append(self.deck.release_card())
        return list_players
    