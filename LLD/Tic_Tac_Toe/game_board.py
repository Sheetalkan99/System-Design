class board:
    def __init__(self):
        self.grid = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.grid.append(row)
        self.moves_count = 0

    def make_move(self,row,col,symbol):
            if 0 <= row <= 2 and 0<= col <= 2:
                if self.grid[row][col] == "-":
                    self.grid[row][col] = symbol
                    self.moves_count += 1
                else:
                    raise ValueError("Cell Occupied")
            else:
                 raise ValueError("Row or Column Out of Range.")
    def is_full(self):
         if self.moves_count == 9:
              return True
         else:
              return False
         
    def has_winner(self):
        for i in range(3):
              if self.grid[i][0] != "-" and self.grid[i][0] == self.grid[i][1] == self.grid[i][2]:
                   return True
        for j in range(3):
             if self.grid[0][j] != "-" and self.grid[0][j] == self.grid[1][j] == self.grid[2][j]:
                  return True
        if self.grid[0][0] != "-" and self.grid[0][0] == self.grid[1][1] ==self.grid[2][2]:
             return True
        if self.grid[0][2] != "-" and self.grid[0][2] == self.grid[1][1] == self.grid[2][0]:
             return True
        return False
    def print_board(self):
        for row in self.grid:
            print(" | ".join(row))
        print()

    