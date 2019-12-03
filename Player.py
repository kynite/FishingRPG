import maptiles


class X:
    def __init__(self):
        self.x = maptiles.starting_position[4]
        self.y = maptiles.starting_position[6]

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def north(self):
        self.move(dx=0, dy=-1)

    def south(self):
        self.move(dx=0, dy=1)

    def east(self):
        self.move(dx=1, dy=0)

    def west(self):
        self.move(dx=-1, dy=0)
