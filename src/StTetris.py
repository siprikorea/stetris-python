from StPlay import StPlay
from StScore import StScore
from PyQt5.QtCore import QBasicTimer, QRect, Qt
from PyQt5.QtGui import QBrush, QColor, QFont, QPainter
from PyQt5.QtWidgets import QWidget


class StTetris(QWidget):

    ST_WINDOW_WIDTH = 800
    ST_WINDOW_HEIGHT = 600
    ST_BLOCK_WIDTH = 30
    ST_BLOCK_HEIGHT = 30
    ST_BOARD_POS_X = 200
    ST_BOARD_POS_Y = 0
    ST_NEXT_BLOCK_POS_X = 650
    ST_NEXT_BLOCK_POS_Y = 150
    ST_SCORE_POS_X = 550
    ST_SCORE_POS_Y = 30
    ST_HIGHSCORE_POS_X = 650
    ST_HIGHSCORE_POS_Y = 30
    ST_BLOCK_COLOR = ["#000000", "#C71585", "#FFA500", "#FFD700", "#228B22", "#1E90FF", "#483D8B", "#9932CC"]
    ST_BACKGROUND_COLOR = "#FFFFFF"
    ST_DOWN_INTERVAL = 500

    # Constructor
    def __init__(self):
        super().__init__()

        # Show widget
        super().resize(self.ST_WINDOW_WIDTH, self.ST_WINDOW_HEIGHT)
        super().setWindowTitle("STetris")
        super().show()

        # Painter
        self.painter = QPainter()

        # Play
        self.play = StPlay(self)
        # Score
        self.score = StScore()
        # High Score
        self.highScore = StScore()
        # Load high score
        # highScore = sessionStorage.getItem("highscore")
        # if (highScore):
        #   Set high score
        #   self.highScore.setScore(highScore)
        # Play interval
        self.playInterval = 500
        # Play timer
        self.playTimer = QBasicTimer()

    # Start
    def start(self):
        # Set interval
        self.playTimer.start(self.ST_DOWN_INTERVAL, self)

    # Stop
    def stop(self):
        self.playTimer.stop()

    def timerEvent(self, e):
        self.play.moveDown()

    def keyPressEvent(self, e):
        key = e.key()

        if key == Qt.Key_Left:
            self.play.moveLeft()
        elif key == Qt.Key_Right:
            self.play.moveRight()
        elif key == Qt.Key_Down:
            self.play.moveDown()
        elif key == Qt.Key_Up:
            self.play.rotate()
        elif key == Qt.Key_Space:
            self.play.drop()

    # Notify
    def notify(self, message, param=None):
        if (message == StPlay.ST_NOTIFY_DOWN):
            self.score.setScore(self.score.getScore() + 100)
        elif (message == StPlay.ST_NOTIFY_DROP):
            self.score.setScore(self.score.getScore() + 100)
        elif (message == StPlay.ST_NOTIFY_CLEAR):
            self.score.setScore(self.score.getScore()
                                + param.cleared_lines * 1000)
        elif (message == StPlay.ST_NOTIFY_TETRISOVER):
            self.stop()

        # Update high score
        #if self.highScore.getScore() < self.score.getScore():
        #    self.highScore.setScore(self.score.getScore())
        #    sessionStorage.setItem("highscore", self.highScore.getScore())

        self.update()

    def paintEvent(self, e):
        self.painter.begin(self)
        self.drawTetris(self.painter)
        self.painter.end()

    # Draw tetris
    def drawTetris(self, painter):

        # Draw background
        rect = {
            "x" : 0,
            "y" : 0,
            "width" : self.ST_WINDOW_WIDTH,
            "height" : self.ST_WINDOW_HEIGHT
        }
        self.drawBackground(painter, rect)

        # Draw board
        boardRect = {
            "x" : self.ST_BOARD_POS_X,
            "y" : self.ST_BOARD_POS_Y,
            "width" : self.ST_BLOCK_WIDTH * self.play.getBoard().getXSize(),
            "height" : self.ST_BLOCK_HEIGHT * self.play.getBoard().getYSize()
        }
        self.drawBoard(painter, boardRect, self.play.getBoard())

        # Draw current block
        self.drawBlock(painter, boardRect, self.play.getCurrentBlock())

        # Draw next block
        nextBlockRect = {
            "x" : self.ST_NEXT_BLOCK_POS_X,
            "y" : self.ST_NEXT_BLOCK_POS_Y,
            "width" : self.ST_BLOCK_WIDTH * 4,
            "height" : self.ST_BLOCK_HEIGHT * 4,
        }
        self.drawBlock(painter, nextBlockRect, self.play.getNextBlock())

        # Draw score
        scoreRect = {
            "x" : self.ST_SCORE_POS_X,
            "y" : self.ST_SCORE_POS_Y,
            "width" : self.ST_BLOCK_WIDTH * 7,
            "height" : self.ST_BLOCK_HEIGHT * 2
        }
        self.drawScore(painter, scoreRect, "SCORE", self.score)

        # Draw high score
        highScoreRect = {
            "x" : self.ST_HIGHSCORE_POS_X,
            "y" : self.ST_HIGHSCORE_POS_Y,
            "width" : self.ST_BLOCK_WIDTH * 7,
            "height" : self.ST_BLOCK_HEIGHT * 2
        }
        self.drawScore(painter, highScoreRect, "HIGH SCORE", self.highScore)

    # Draw background
    def drawBackground(self, painter, rect):
        painter.fillRect(QRect(rect["x"], rect["y"], rect["width"], rect["height"]), QColor(self.ST_BACKGROUND_COLOR))

    # Draw board
    def drawBoard(self, painter, rect, board):

        # Draw board
        for boardY in range(board.getYSize()):
            for boardX in range(board.getXSize()):
                rectBlock = {
                    "x" : rect["x"] + boardX * StTetris.ST_BLOCK_WIDTH,
                    "y" : rect["y"] + boardY * StTetris.ST_BLOCK_HEIGHT,
                    "width" : StTetris.ST_BLOCK_WIDTH,
                    "height" : StTetris.ST_BLOCK_HEIGHT
                }
                fillColor = StTetris.ST_BLOCK_COLOR[self.play.getBoard().getBlock(boardX, boardY)]
                painter.fillRect(QRect(rectBlock["x"], rectBlock["y"], rectBlock["width"], rectBlock["height"]), QColor(fillColor))

    # Draw block
    def drawBlock(self, painter, rect, block):

        # Draw block
        for blockY in range(block.getYSize()):
            for blockX in range(block.getXSize()):
                if block.getBlock(blockX, blockY):
                    rectBlock = {
                        "x" : rect["x"] + (block.getXPos() + blockX) * StTetris.ST_BLOCK_WIDTH,
                        "y" : rect["y"] + (block.getYPos() + blockY) * StTetris.ST_BLOCK_HEIGHT,
                        "width" : StTetris.ST_BLOCK_WIDTH,
                        "height" : StTetris.ST_BLOCK_HEIGHT
                    }
                    fillColor = StTetris.ST_BLOCK_COLOR[block.getBlock(blockX, blockY)]
                    painter.fillRect(QRect(rectBlock["x"], rectBlock["y"], rectBlock["width"], rectBlock["height"]), QColor(fillColor))

    # Draw score
    def drawScore(self, painter, rect, title, score):
        # Draw title
        painter.textAligh = "right"
        painter.fillStyle = "red"
        painter.drawText(rect["x"], rect["y"], title)

        # Draw score
        painter.drawText(rect["x"], rect["y"] + rect["height"] // 2, str(score.getScore()))