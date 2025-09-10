from player import player
from game import game

if __name__ == "__main__":
    name1 = input("Enter Player1: ")
    name2 = input("Enter Player2:" )
    player1 = player(name1, 'X')
    player2 = player(name2,'O')

    game = game(player1, player2)
    game.play()


