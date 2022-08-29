from player import Player

class Game(Player):
    max_player = 4
    min_player = 2
    def __init__(self, num_player: int, index, deck):
        #num_player should be consider between 2 and 4
        assert num_player <= self.max_player and num_player >= self.min_player, f"Number of players: {num_player} is not between 2 and 4"
        
        self.num_player = num_player
        self.deck = deck
           
        if self.num_player == 2:
            self.player1 = Player("Player1", index, self.deck)
            self.player2 = Player("Player2", index, self.deck)
            
        elif self.num_player == 2:
            self.player1 = Player("Player1", index, self.deck)
            self.player2 = Player("Player2", index, self.deck)
            self.player3 = Player("Player3", index, self.deck)
            
        else:
            self.player1 = Player("Player1", index, self.deck)
            self.player2 = Player("Player2", index, self.deck)
            self.player3 = Player("Player3", index, self.deck)
            self.player4 = Player("Player4", index, self.deck)
            
    def GameDetails(self):
        if self.num_player == 2:
            return self.player1.show_hand(), self.player2.show_hand()
        elif self.num_player == 3:
            return self.player1.show_hand(), self.player2.show_hand(), self.player3.show_hand()
        else:
            return self.player1.show_hand(), self.player2.show_hand(), self.player3.show_hand(), self.player4.show_hand()