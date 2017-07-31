
class Train:

    def __init__(self, owner, starting_tile):
        self.owner = owner
        self.tiles = []
        self.tiles.append(starting_tile)
        self.open = False

    def last_tile(self):
        return self.tiles[-1][-1] 

    def last(self):
        return self.tiles[-1]