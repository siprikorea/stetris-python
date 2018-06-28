import numpy

class StBoard:

    # Constructor
    def __init__(self):
        # Board
        self.board = numpy.zeros(shape=(self.getYSize(), self.getXSize()))

    # Get X size
    def getXSize(self):
        return 10

    # Get Y size
    def getYSize(self):
        return 20

    # Get block
    def getBlock(self, x, y):
        if x < 0 or x >= self.getXSize():
            return 0

        if y < 0 or y >= self.getYSize():
            return 0

        return self.board[y][x]

    # Set block
    def setBlock(self, x, y, block):
        if x < 0 or x >= self.getXSize():
            return

        if y < 0 or y >= self.getYSize():
            return

        self.board[y][x] = block

    # Clear complete lines
    def clearCompleteLines(self):
        complete_lines = 0

        for boardY in range(self.getYSize()):
            block_count = 0

            # Count the number of block
            for boardX in range(self.getXSize()):
                if (self.board[boardY][boardX]):
                    block_count += 1

            # The line of board is full of block
            if block_count == self.board[boardY].length:
                # Delete line of board
                self.board.pop(boardY)
                # Add line to the beginning of the board
                self.board = numpy.zeros(shape=(1, self.getXSize())) + self.board
                complete_lines += 1

        return complete_lines