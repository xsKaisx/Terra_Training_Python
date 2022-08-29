from game import Game
from deck import Deck

if __name__ == "__main__":
    while True:
        num_game = input("Please input number of game: ")
        try:
            val = int(num_game)
            if val < 0:
                raise ValueError
            break #out loop if successful get num_game
        except ValueError:
            print('Invalid number. Please input a positive integer. -_-')
            
    for i in range(val):
        num_player = input("Please input number of players(2-4): ")
        deck = Deck()
        game = Game(int(num_player), i+1, deck)
        print("Your {} game details: ---------------------------".format(i+1))
        game.GameDetails() 