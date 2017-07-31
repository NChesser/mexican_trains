import itertools
import random

class Dominos:

    def __init__(self):
        self.tiles = self.tiles_setup()
        random.shuffle(self.tiles)

    def tiles_setup(self):
        tiles = []
        for i in range (12):
            for j in range (12, 0+i, -1):
                tiles.append([i+1,j])
                
        return tiles

    def pop_domino(self, index=-1):
        return self.tiles.pop(index)
    
    def get_double(self):
        for i, tile in enumerate(self.tiles):
            if tile[0] == tile[1]:
                return self.tiles.pop(i)