
class MapTile:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def introtext(self):
        raise NotImplementedError()

    def modifyplayer(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
    if world.tile_exists(self.x - 1, self.y):
        moves.append(actions.MoveWest())
    if world.tile_exists(self.x, self.y - 1):
        moves.append(actions.MoveNorth())
    if world.tile_exists(self.x, self.y + 1):
        moves.append(actions.MoveSouth())
    return moves

class Startingroom(MapTile):
    def introtext(self):
        return "yes hello this is the beginning"

    def modifyplayer(self, player):
        pass


starting_position = None
