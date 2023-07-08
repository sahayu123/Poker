class Player:
    def __init__(self):
        '''The init method of the Player class creates a player object
         and sets the players attributes for the game.
        '''
        self.card_one=None
        self.card_two=None
        self.money=100
        self.round_status=None
        self.player_bet=0
        self.player_bet_hand=0
        self.point_val=0
        #self.name=input("please enter name:")
        names=["b","c","d","e","f"]
        self.name=names[0]
        names.remove(self.name)
        



         