class Card():
    def __init__(self,suit,number):
        '''The init method of the Card class, creates a card object with attributes of the suit and number.
            It takes the suit as parameter one
            It takes the number as parameter two'''
        self.suit=suit
        self.number=number
        if self.number=="Jack":
            self.number_value=11
        elif self.number=="Queen":
            self.number_value=12
        elif self.number=="King":
            self.number_value=13
        elif self.number=="Ace":
            self.number_value=14  
        else:
            self.number_value=int(self.number)
