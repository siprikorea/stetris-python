import random

class StBlock:
    blocks = [ [
                [
                    [ 1, 0, 0 ],
                    [ 1, 1, 1 ],
                    [ 0, 0, 0 ]
                ], [
                    [ 0, 1, 0 ],
                    [ 0, 1, 0 ],
                    [ 1, 1, 0 ]
                ], [
                    [ 0, 0, 0 ],
                    [ 1, 1, 1 ],
                    [ 0, 0, 1 ]
                ], [
                    [ 0, 1, 1 ],
                    [ 0, 1, 0 ],
                    [ 0, 1, 0 ]
                ]
            ], [
                [
                    [ 0, 0, 2 ],
                    [ 2, 2, 2 ],
                    [ 0, 0, 0 ]
                ], [
                    [ 2, 2, 0 ],
                    [ 0, 2, 0 ],
                    [ 0, 2, 0 ]
                ], [
                    [ 0, 0, 0 ],
                    [ 2, 2, 2 ],
                    [ 2, 0, 0 ]
                ], [
                    [ 0, 2, 0 ],
                    [ 0, 2, 0 ],
                    [ 0, 2, 2 ]
                ]
            ], [
                [
                    [ 3, 3 ],
                    [ 3, 3 ]
                ]
            ], [
                [
                    [ 0, 4, 4 ],
                    [ 4, 4, 0 ],
                    [ 0, 0, 0 ]
                ], [
                    [ 0, 4, 0 ],
                    [ 0, 4, 4 ],
                    [ 0, 0, 4 ]
                ]
            ], [
                [
                    [ 0, 0, 0 ],
                    [ 5, 5, 5 ],
                    [ 0, 5, 0 ]
                ], [
                    [ 0, 5, 0 ],
                    [ 0, 5, 5 ],
                    [ 0, 5, 0 ]
                ], [
                    [ 0, 5, 0 ],
                    [ 5, 5, 5 ],
                    [ 0, 0, 0 ]
                ], [
                    [ 0, 5, 0 ],
                    [ 5, 5, 0 ],
                    [ 0, 5, 0 ]
                ]
            ], [
                [
                    [ 6, 6, 0 ],
                    [ 0, 6, 6 ],
                    [ 0, 0, 0 ]
                ], [
                    [ 0, 0, 6 ],
                    [ 0, 6, 6 ],
                    [ 0, 6, 0 ]
                ]
            ], [
                [
                    [ 0, 0, 0, 0 ],
                    [ 0, 0, 0, 0 ],
                    [ 7, 7, 7, 7 ],
                    [ 0, 0, 0, 0 ]
                ], [
                    [ 0, 7, 0, 0 ],
                    [ 0, 7, 0, 0 ],
                    [ 0, 7, 0, 0 ],
                    [ 0, 7, 0, 0 ]
                ]
            ] ]

    def __init__(self, block) {
        if (block != null):
            # Type
            self.type = block.type
            # X Position
            self.xPos = block.xPos
            # Y Position
            self.yPos = block.yPos
            # Rotation
            self.rotation = block.rotation
            # Block
            self.block = block.block
        else:
            # Type
            self.type = random.randint(1, len(StBlock.blocks))
            # X Position
            self.xPos = 0
            # Y Position
            self.yPos = 0
            # Rotation
            self.rotation = 0
            # Block
            self.block = StBlock.blocks[self.type-1]
        }
    }

    # Get type
    def getType(self):
        return self.type

    # Get X size
    def getXSize(self):
        return len(self.block[self.rotation][0])

    # Get Y size
    def getYSize(self):
        return len(self.block[self.rotation])

    # Get X position
    def getXPos(self):
        return self.xPos

    # Get Y position
    def getYPos(self):
        return self.yPos

    # Get rotation
    def getRotation(self):
        return self.rotation

    # Get block
    def getBlock(self, x, y):
        if x < 0 or x >= self.getXSize():
            return 0

        if y < 0 or y >= self.getYSize():
            return 0

        return self.block[self.rotation][y][x]
    }

    # Set X position
    def setXPos(self, xPos):
        self.xPos = xPos

    # Set Y position
    def setYPos(self, yPos):
        self.yPos = yPos
    
    # Set rotation
    def setRotation(self, rotation):
        self.rotation = rotation % self.block.length