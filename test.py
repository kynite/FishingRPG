from tabulate import tabulate

class Movement:

    def __init__(self):
        self.x = 4
        self.y = 6

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def movenorth(self):
        self.move(dx=0, dy=-1)

    def movesouth(self):
        self.move(dx=0, dy=1)

    def moveeast(self):
        self.move(dx=1, dy=0)

    def movewest(self):
        self.move(dx=-1, dy=0)

    def playerpostion(self):
        self.playerpositionx = map[self.x]
        self.playerpositiony = map[self.y]





userinp = input('chose direcion: ')


def changedirection():
    if userinp == 'north':
        Movement.movenorth()
        print(tabulate(map))



map = [[" . ", " . ", " E ", " . ", " . "],
       [" . ", " . ", " . ", " . ", " . "],
       [" J ", " . ", " . ", " . ", " K "],
       [" . ", " . ", " . ", " . ", " . "],
       [" . ", " W ", " . ", " H ", " . "],
       [" . ", " . ", " R ", " . ", " . "],
       [" . ", " . ", " . ", " . ", " X "]]

changedirection()
