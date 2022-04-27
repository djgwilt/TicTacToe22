
class Game:

    EMPTY = " "
    P1 = "o"
    P2 = "x"

    def __init__(self):
        self.__board = [[Game.EMPTY for _ in range(3)] for _ in range(3)]
        self.__player = Game.P1

    def __repr__(self):
        return str(self.__board)

    def play(self,row,col):
        row -= 1 # change to zero-based
        col -= 1
        self.__board[row][col] = self.__player
        self.__player = Game.P2 if self.__player == Game.P1 else Game.P1
    
    @property
    def winner(self):
        return None

# changed comment here
if __name__ == "__main__":
    pass
