from deck import Deck

class Player():
    def __init__(self, name, index, deck):
        self.name = name
        self.index = index
        self.deck = deck
        self.deck.shuffle()
        self.hand = []
        self.draw()
        
    def draw(self):
        # if not self.hand:
        #     for _ in range(2):
        #         self.hand.append(self.deck.draw())
        # else:
        #     self.hand.append(self.deck.draw())
        for _ in range(13):
            self.hand.append(self.deck.draw())
    
    def show_hand(self):
        print(f"{self.name}, game index: {self.index}")
        for i in range(len(self.hand)):
            self.hand[i].show()
            if i == len(self.hand) - 1:
                print()
            
    # def cal_score(self):
    #     score = 0
    #     for i in range (len(self.hand)):
    #         s_value = 0           
    #         if self.hand[i].card[0] == "J" or self.hand[i].card[0] == "Q" or self.hand[i].card[0] == "K" or self.hand[i].card[0] == "1":
    #             s_value = 10
    #         elif self.hand[i].card[0] == "A":
    #             s_value = 1
    #         else:
    #             s_value = int(self.hand[i].card[0])
    #         score = score + s_value
    #     return score
            
# deck = Deck()
# player = Player("Dennis", 1, deck)
# player.show_hand()
# print(f"score: {player.cal_score()}")
# player.draw()
# player.show_hand()
# print(f"score: {player.cal_score()}")