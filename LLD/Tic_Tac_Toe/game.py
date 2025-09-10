from game_board import board
class game:
    def __init__(self,player1,player2):
        self.board = board()
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
    def swtich_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1
    def get_valid_input(self,message):
        while True:
            try:
                value = int(input("Enter value in grid: "))
                
                if 0 <= value <= 2:
                    return value
                else:
                    print("Out Of Range")
            except ValueError:
                print("Invlaid Input")
    def play(self):
        print("Game Started:")
        while not self.board.is_full() and not self.board.has_winner():
            print(f"{self.current_player.get_name()}'s turn ({self.current_player.get_symbol()}):")

            row = self.get_valid_input("Enter row: ")
            col = self.get_valid_input("Enter Col :")

            try:
                self.board.make_move(row,col,self.current_player.get_symbol())
                self.board.print_board()
                self.swtich_player()
            except ValueError as e:
                print(f"{str(e)} Try Again")

        if self.board.has_winner():
            self.swtich_player()
            print(f"{self.current_player.get_name()} wins!")
        else:
            print("DRAW!")

    