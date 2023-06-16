
import random
from cards import Card
from player import Player     
class Deck():
    def __init__(self):
        '''The init methord of the Deck class creates a deck and appends it to a list.'''
        self.deck3=list()
        for i in ["Clubs","Diamonds", "Hearts","Spades"]:
            for j in["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]:
                self.deck3.append({"suit":i,"number":j})
    def shuffle(self):
        '''The shuffle methord of the Deck class shuffles the deck and makes each individual card an object.'''
        z=51
        x=0
        self.deck_shuffled=list()
        while x<52:
            j=random.randint(0,z)
            #print(j)
            self.deck_shuffled.append(Card(self.deck3[j]["suit"],self.deck3[j]["number"]))
            self.deck3.remove(self.deck3[j])
            z=z-1
            x=x+1
           
        # print("should be empty",self.deck3)
        # print("shuffled deck",self.deck_shuffled)
        #print("")


    def deal(self,num_players,players_list):
        '''The deal method of the Deck class deals to cards to each player.
            It takes the number of players as the first parameter.
            It takes the list of players as the second parameter.
            It returns the shuffled deck.'''
        #print("this is players list inside deal", players_list)
        l=51
        for nbm in range(num_players):
                b=random.randint(0,l)
                players_list[nbm].card_one=self.deck_shuffled[b]
                l=l-1
                self.deck_shuffled.remove(self.deck_shuffled[b])
                #print(players_list[nbm].card_one.suit,"of", players_list[nbm].card_one.number)
                b=random.randint(0,l)
                players_list[nbm].card_two=self.deck_shuffled[b]
                l=l-1
                #print(players_list[nbm].card_two.suit,"of",players_list[nbm].card_two.number)
                self.deck_shuffled.remove(self.deck_shuffled[b])
        return self.deck_shuffled        



 
        




