class Card():
    def __init__(self, card: str):
        self.card = card
        
    def show(self):
        print(f"{self.card}", end=" ")