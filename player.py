import itertools

class Player:

    def __init__(self, name, starting_tile):
        self.name = name
        self.starting_tile = starting_tile
        self.tiles = []
        self.longest = []
        self.remainder = []
        self.pickups = 0
        self.played = 0

    def recur(self, previous, tiles, possible=None, l=None):
        """
        Returns all possible acceptable permutations        
        """
        t = tiles.copy()

        if possible is None:
            possible = []
        
        if l is None:
            l = []
        
        for tile in tiles:          
            if tile[0] == previous[1]:
                l.append(tile)
                t.remove(tile)
                self.recur(tile, t, possible, l)
            elif tile[1] == previous[1]:
                l.append(list(reversed(tile)))
                t.remove(tile)
                self.recur(list(reversed(tile)), t, possible, l)
        else:
            possible.append(l.copy())
            if len(l) > 0:
                del l[-1]

        return possible

    def get_longest(self, starting_tile, tiles):
        """
        Creates a tree of the longest path that can be played on player's own train
        Stores any remainding tiles
        """
        self.remainder = tiles.copy()
        possible = self.recur(starting_tile, tiles)
        longest = []

        for p in possible:
            if len(p) > len(longest):
                longest = p.copy()

        for tile in longest:
            for t in self.remainder:
                if t == tile:
                    self.remainder.remove(tile)                
                elif t == list(reversed(tile)):
                    self.remainder.remove(list(reversed(tile)))
        
        self.longest = longest.copy()

    def play_domino(self, trains):
        """        
        Firsts checks if other trains are open and then if possible plays a remainding tile
        If none are open then plays tile on private train
        """

        
        for train in trains:
            if train.open:
                for i, t in enumerate(self.remainder):
                    if t[0] == train.last_tile():
                        train.tiles.append(t)
                        self.remainder.remove(t)
                        self.played += 1
                        return True
                    elif t[1] == train.last_tile():
                        self.remainder[i].reverse()
                        train.tiles.append(t)
                        self.remainder.remove(t)
                        self.played += 1
                        return True
        
        for train in trains:
            if train.owner == self.name:
                for i, t in enumerate(self.longest):
                    if t[0] == train.last_tile():
                        train.tiles.append(t)
                        self.longest.remove(t)
                        train.open = False
                        self.played += 1
                        return True
                    elif t[1] == train.last_tile():
                        self.longest[i].reverse()
                        train.tiles.append(t)
                        self.longest.remove(t)
                        train.open = False
                        self.played += 1
                        return True

        return False      
    
    def __repr__(self):
        return self.name

