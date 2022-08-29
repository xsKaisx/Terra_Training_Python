from cards import Card
import random

class Deck:
    def __init__(self):
      self.cards = []
      self.build()
      
    def build(self):
        for val in range(1, 14):
            for type in ["♠", "♣", "♦", "♥"]:
                if val == 1:
                    val = "A"
                elif val == 11:
                    val = "J"
                elif val == 12:
                    val = "Q"
                elif val == 13:
                    val = "K"
                self.cards.append(Card(str(val)+type))
                
    def show(self):
        for c in self.cards:
            c.show()
            
    def shuffle(self):
        return random.shuffle(self.cards)
    
    def draw(self):
        return self.cards.pop(0)
        
# deck = Deck()
# deck.show()
# deck.shuffle()
# print("------shuffle------")
# card = deck.draw()
# card.show()