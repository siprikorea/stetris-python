class StTetris():

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
    ST_BLOCK_COLOR = ["#000000", "#C71585", "#FFA500","#FFD700",  "#228B22",  "#1E90FF",  "#483D8B",  "#9932CC"]
    ST_BACKGROUND_COLOR = "#FFFFFF"

    # Constructor
    def __init__(self, canvas):
        # Canvas
        # self.canvas = canvas
        # self.canvas.width = StTetris.ST_WINDOW_WIDTH
        # self.canvas.height = StTetris.ST_WINDOW_HEIGHT

        # Context of canvas
        # self.ctx = self.canvas.getContext("2d")

        # Play
        self.play = StPlay(self)
        # Score
        self.score = StScore()
        # High Score
        self.highScore = StScore()
        # Load high score
        # highScore = sessionStorage.getItem("highscore")
        if (highScore):
            # Set high score
            self.highScore.setScore(highScore)
        # Play interval
        self.playInterval = 500
        # Play interval handle
        self.playIntervalHandle = null

    # Start
    def start(self):
        # Set interval
        # self.playIntervalHandle = setInterval(() => {
        #     self.play.moveDown() },
        #     self.playInterval);

        # Key down event listener
        # self.onKeyDown = (e) => {
        #    switch (e.code):
        #        case "ArrowLeft":
        #            self.play.moveLeft()
        #            break
        #        case "ArrowRight":
        #            self.play.moveRight()
        #            break
        #        case "ArrowDown":
        #            self.play.moveDown()
        #            break
        #        case "ArrowUp":
        #            self.play.rotate()
        #            break
        #        case "Space":
        #            self.play.drop()
        #            break

        # Add event listener
        window.addEventListener('keydown', self.onKeyDown)

    # Stop
    def stop(self):
        # Clear interval
        clearInterval(self.playIntervalHandle)
        # Remove event listener
        window.removeEventListener('keydown', self.onKeyDown)

    # Notify
    def notify(self, message, param):
        switch (message):
            case StPlay.ST_NOTIFY_LEFT:
            case StPlay.ST_NOTIFY_RIGHT:
            case StPlay.ST_NOTIFY_ROTATE:
                break
            case StPlay.ST_NOTIFY_DOWN:
            case StPlay.ST_NOTIFY_DROP:
                self.score.setScore(self.score.getScore() + 100)
                break
            case StPlay.ST_NOTIFY_CLEAR:
                self.score.setScore(self.score.getScore() + param.cleared_lines * 1000)
                break
            case StPlay.ST_NOTIFY_TETRISOVER:
                self.stop()
                return

        # Update high score
        if self.highScore.getScore() < self.score.getScore():
            self.highScore.setScore(self.score.getScore())
            sessionStorage.setItem("highscore", self.highScore.getScore())

        self.drawTetris(self.ctx)

    # Draw tetris
    def drawTetris(self, ctx):

        # Draw background
        rect = {
            x: 0,
            y: 0,
            width: StTetris.ST_WINDOW_WIDTH,
            height: StTetris.ST_WINDOW_HEIGHT }
        self.drawBackground(self.ctx, rect)

        # Draw board
        boardRect = {
            x: StTetris.ST_BOARD_POS_X,
            y: StTetris.ST_BOARD_POS_Y,
            width: StTetris.ST_BLOCK_WIDTH * self.play.getBoard().getXSize(),
            height: StTetris.ST_BLOCK_HEIGHT * self.play.getBoard().getYSize() }
        self.drawBoard(ctx, boardRect, self.play.getBoard())

        # Draw current block
        self.drawBlock(ctx, boardRect, self.play.getCurrentBlock())

        # Draw next block
        nextBlockRect = {
            x: StTetris.ST_NEXT_BLOCK_POS_X,
            y: StTetris.ST_NEXT_BLOCK_POS_Y,
            width: StTetris.ST_BLOCK_WIDTH * StTetris.ST_MAX_BLOCK_X,
            height: StTetris.ST_BLOCK_HEIGHT * StTetris.ST_MAX_BLOCK_Y }
        self.drawBlock(ctx, nextBlockRect, self.play.getNextBlock())

        # Draw score
        scoreRect = {
            x: StTetris.ST_SCORE_POS_X,
            y: StTetris.ST_SCORE_POS_Y,
            width: StTetris.ST_BLOCK_WIDTH * 7,
            height: StTetris.ST_BLOCK_HEIGHT * 2 }
        self.drawScore(ctx, scoreRect, "SCORE", self.score)

        # Draw high score
        highScoreRect = {
            x: StTetris.ST_HIGHSCORE_POS_X,
            y: StTetris.ST_HIGHSCORE_POS_Y,
            width: StTetris.ST_BLOCK_WIDTH * 7,
            height: StTetris.ST_BLOCK_HEIGHT * 2 }
        self.drawScore(ctx, highScoreRect, "HIGH SCORE", self.highScore)

    # Draw background
    def drawBackground(self, ctx, rect):
        ctx.fillStyle = StTetris.ST_BACKGROUND_COLOR
        ctx.fillRect(rect.x, rect.y, rect.width, rect.height)

    # Draw board
    def drawBoard(self, ctx, rect, board):

        # Draw board
        for (let boardY = 0; boardY < board.getYSize(); boardY++):
            for (let boardX = 0; boardX < board.getXSize(); boardX++):
                rectBlock = {
                    x: rect.x + boardX * StTetris.ST_BLOCK_WIDTH,
                    y: rect.y + boardY * StTetris.ST_BLOCK_HEIGHT,
                    width: StTetris.ST_BLOCK_WIDTH,
                    height: StTetris.ST_BLOCK_HEIGHT }
                ctx.fillStyle = StTetris.ST_BLOCK_COLOR[self.play.getBoard().getBlock(boardX, boardY)]
                ctx.fillRect(rectBlock.x, rectBlock.y, rectBlock.width, rectBlock.height)

    # Draw block
    def drawBlock(self, ctx, rect, block):

        # Draw block
        for blockY in range(block.getYSize()):
            for blockX in range(block.getXSize()):
                if block.getBlock(blockX, blockY):
                    rectBlock = {
                        x: rect.x + (block.getXPos() + blockX) * StTetris.ST_BLOCK_WIDTH,
                        y: rect.y + (block.getYPos() + blockY) * StTetris.ST_BLOCK_HEIGHT,
                        width: StTetris.ST_BLOCK_WIDTH,
                        height: StTetris.ST_BLOCK_HEIGHT }
                    ctx.fillStyle = StTetris.ST_BLOCK_COLOR[block.getBlock(blockX, blockY)]
                    ctx.fillRect(rectBlock.x, rectBlock.y, rectBlock.width, rectBlock.height)

    # Draw score
    def drawScore(self, ctx, rect, title, score):
        # Draw title
        ctx.textAligh = "right"
        ctx.fillStyle = "red"
        ctx.fillText(title, rect.x, rect.y)

        # Draw score
        ctx.fillText(score.getScore(), rect.x, rect.y + rect.height // 2)