from StBoard import StBoard
from StBlock import StBlock

class StPlay:
    ST_NOTIFY_LEFT = "NOTIFY_LEFT"

    ST_NOTIFY_RIGHT = "NOTIFY_RIGHT"

    ST_NOTIFY_DOWN = "NOTIFY_DOWN"
        
    ST_NOTIFY_DROP = "NOTIFY_DROP"

    ST_NOTIFY_ROTATE = "NOTIFY_ROTATE"

    ST_NOTIFY_CLEAR = "NOTIFY_CLEAR"

    ST_NOTIFY_TETRISOVER = "NOTIFY_TETRISOVER"

    # Constructor
    def __init__(self, notify):
        # Board
        self.board = StBoard()
        # Current block
        self.currentBlock = StBlock()
        self.currentBlock.setXPos((self.board.getXSize() - self.currentBlock.getXSize()) // 2)
        self.currentBlock.setYPos(0 - self.currentBlock.getYSize())
        # Next block
        self.nextBlock = StBlock()
        # Notify
        self.notify = notify

    # Get board
    def getBoard(self):
        return self.board

    # Get current block
    def getCurrentBlock(self):
        return self.currentBlock

    # Get next block
    def getNextBlock(self):
        return self.nextBlock

    # Move left
    def moveLeft(self):
        # Is block movable
        if self.isMovable(self.currentBlock, self.currentBlock.getXPos() - 1, self.currentBlock.getYPos(), self.currentBlock.getRotation()):
            # Set current X position to left
            self.currentBlock.setXPos(self.currentBlock.getXPos() - 1)
            # Notify
            self.notify.notify(StPlay.ST_NOTIFY_LEFT)

    # Move right
    def moveRight(self):
        # Is block movable
        if self.isMovable(self.currentBlock, self.currentBlock.getXPos() + 1, self.currentBlock.getYPos(), self.currentBlock.getRotation()):
            # Set current X position to right
            self.currentBlock.setXPos(self.currentBlock.getXPos() + 1)
            # Notify
            self.notify.notify(StPlay.ST_NOTIFY_RIGHT)

    # Move down
    def moveDown(self):
        # Is block movable
        if self.isMovable(self.currentBlock, self.currentBlock.getXPos(), self.currentBlock.getYPos() + 1, self.currentBlock.getRotation()):
            # Set current Y position to down
            self.currentBlock.setYPos(self.currentBlock.getYPos() + 1)
            # Notify
            self.notify.notify(StPlay.ST_NOTIFY_DOWN)
        # Block is not movable
        else:
            # Set current block to board
            self.setCurrentBlockToBoard()
            # Change current block
            self.changeCurrentBlock()
            # Clear completed line
            cleared_lines = self.board.clearCompleteLines()
            if cleared_lines:
                # Notify
                self.notify.notify(StPlay.ST_NOTIFY_CLEAR, { cleared_lines : cleared_lines })
            # Tetris is over
            if self.isTetrisOver():
                # Notify
                self.notify.notify(StPlay.ST_NOTIFY_TETRISOVER)

    # Drop
    def drop(self):

        while True:
            # Block is movable
            if self.isMovable(self.currentBlock, self.currentBlock.getXPos(), self.currentBlock.getYPos() + 1, self.currentBlock.getRotation()):
                # Set current Y position to down
                self.currentBlock.setYPos(self.currentBlock.getYPos() + 1)
            # Block is not movable
            else:
                # Notify
                self.notify.notify(StPlay.ST_NOTIFY_DROP)
                break

        # Set current block to board
        self.setCurrentBlockToBoard()
        # Change current block
        self.changeCurrentBlock()
        # Clear completed line
        cleared_lines = self.board.clearCompleteLines()
        if cleared_lines:
            # Notify
            self.notify.notify(StPlay.ST_NOTIFY_CLEAR, { cleared_lines : cleared_lines })
        # Tetris is over
        if self.isTetrisOver():
            # Notify
            self.notify.notify(StPlay.ST_NOTIFY_TETRISOVER)

    # Rotate
    def rotate(self):
        # Is block movable
        if self.isMovable(self.currentBlock, self.currentBlock.getXPos(), self.currentBlock.getYPos(), self.currentBlock.getRotation() + 1):
            # Rotate
            self.currentBlock.setRotation(self.currentBlock.getRotation() + 1)
            # Notify
            self.notify.notify(StPlay.ST_NOTIFY_ROTATE)

    # Is movable
    def isMovable(self, block, xPos, yPos, rotation):

        # Create block to check and set value to check
        checkBlock = StBlock(block)
        checkBlock.setXPos(xPos)
        checkBlock.setYPos(yPos)
        checkBlock.setRotation(rotation)

        # Get value of board
        for blockX in range(checkBlock.getXSize()):
            for blockY in range(checkBlock.getYSize()):

                # Check if block to check is empty
                if checkBlock.getBlock(blockX, blockY) == 0:
                    continue

                boardX = checkBlock.getXPos() + blockX
                boardY = checkBlock.getYPos() + blockY

                # Check X position of block to check
                if boardX < 0 or boardX >= self.board.getXSize():
                    return False

                # Check Y position of block to check
                if boardY >= self.board.getYSize():
                    return False

                # Check if block is already exist
                if self.board.getBlock(boardX, boardY) != 0:
                    return False

        return True

    # Set current block to board
    def setCurrentBlockToBoard(self):
        # Set current block to board
        for blockX in range(self.currentBlock.getXSize()):
            for blockY in range(self.currentBlock.getYSize()):
                if self.currentBlock.getBlock(blockX, blockY) != 0:
                    self.board.setBlock(self.currentBlock.getXPos() + blockX, self.currentBlock.getYPos() + blockY, self.currentBlock.getType())

    # Check if tetris is over
    def isTetrisOver(self):
        isTetrisOver = False
        for boardX in range(self.board.getXSize()):
            if self.board.getBlock(boardX, 0) != 0:
                isTetrisOver = True
                break
        return isTetrisOver

    # Change current block
    def changeCurrentBlock(self):
        # Set next block to current block
        self.currentBlock = self.nextBlock
        self.currentBlock.setXPos((self.board.getXSize() - self.currentBlock.getXSize()) // 2)
        self.currentBlock.setYPos(- self.currentBlock.getYSize())
        # Set next block
        self.nextBlock = StBlock()