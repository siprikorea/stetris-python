class StScore:
    # Constructor
    def __init__(self):
        # Score
        self.score = 0

    # Clear
    def clear(self):
        self.score = 0

    # Add score
    def addScore(self, score):
        self.score += score

    # Set score
    def setScore(self, score):
        self.score = score

    # Get score
    def getScore(self):
        return self.score