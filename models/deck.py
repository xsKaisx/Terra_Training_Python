from random import shuffle
from itertools import product
from card import Card

class Deck:
    def __init__(self):
        self.cards = []
        for c in product(Card.card_suits,Card.card_values):
            self.cards.append(c)
        shuffle(self.cards)
    def release_card(self):
        return self.cards.pop()
    
    def card_shuffle(self):
        return shuffle(self.cards)

    def __str__(self):
        return len(self.cards)
