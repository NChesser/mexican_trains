from dominos import Dominos
from player import Player
from train import Train

def game_setup(num_of_players):
    #Simulate a Mexican Train Game
    #Add Dominos, Players and Player's Trains
    dominos = Dominos()
    starting_tile = dominos.get_double()    
    players = [Player("Player " + str(i), starting_tile) for i in range(num_of_players)]
    trains = [Train(players[i].name, starting_tile) for i in range(num_of_players)]

    #Adding Public Train
    public_train = Train("Public", starting_tile)
    public_train.open = True
    trains.append(public_train)

    #Give Players Dominos
    for i in range(15):
        for player in players:
            player.remainder.append(dominos.pop_domino())

    #Initial Player Setup 
    print(starting_tile)
    for player in players:
        player.get_longest(starting_tile, player.remainder)
    
    #Handle Player turns 
    handle_turns(players, dominos, trains)     

    #Print out Final Results
    for train in trains:
        print(train.owner)
        print(train.tiles)
        print("Train is open = " + str(train.open))
    
    for player in players:
        print(player.name + " Picked up " + str(player.pickups) + " has " + str(len(player.longest) + len(player.remainder)) + " Tiles left " + str(player.played) + " Dominos Played")

    #Remaing dominos in the boneyard
    print ("Remaining Dominos")
    print (dominos.tiles)

def handle_turns(players, dominos, trains):
    """
    Game function

    Each player should play a domino if they can.
    If they cannot they must pick up and open their train.

    Players can only play on their train or someone else's open train

    Game continues until a player has no dominos left or no one can play a tile

    """   
    finished = False
    while not finished:
        played = False
        for player in players:
            if len(player.longest) > 0 or len(player.remainder) > 0:
                for train in trains:
                    if train.owner == player.name:
                        player.get_longest(list(train.last()), list(player.remainder + player.longest))

                played = play_domino(player, trains)       

                if not played:
                    pick_up(player, dominos)
                    for train in trains:
                        if train.owner == player.name:
                            train.open = True
            else:
                finished = True                
                print (player.name + " Wins") 
                return   
        
        if not played and len(dominos.tiles) == 0:
            finished = True
            print ("Draw")

def pick_up(player, dominos):
    if len(dominos.tiles) > 0:
        player.remainder.append(dominos.pop_domino())
        player.pickups += 1

def play_domino(player, trains): 
    """
    If player has domino with same value as last domino on train then places domino
    """
    return player.play_domino(trains)
                     

if __name__ == "__main__":
    game_setup(4)
