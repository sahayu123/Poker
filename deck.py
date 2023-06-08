
import random
class Player:
    def __init__(self):
        self.card_one=None
        self.card_two=None
class Card():
    def __init__(self,suit,number):
        self.suit=suit
        self.number=number
        
class Deck():
    def __init__(self):
        self.deck3=list()
        for i in ["Clubs","Diamonds", "Hearts","Spades"]:
            for j in["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]:
                self.deck3.append({"suit":i,"number":j})
    def shuffle(self):
        z=51
        x=0
        self.deck_shuffled=list()
        while x<52:
            j=random.randint(0,z)
            print(j)
            self.deck_shuffled.append(self.deck3[j])
            self.deck3.remove(self.deck3[j])
            z=z-1
            x=x+1
           
        # print("should be empty",self.deck3)
        # print("shuffled deck",self.deck_shuffled)
        print("")

    def deal(self,num_players):
        self.num_players=num_players
        cards_list=list()# TODO: this needs to be done in shuffle
        
        for k in self.deck_shuffled:
            cards_list.append(Card(k["suit"],k["number"]))
        print(cards_list)
        d=0
        for m in cards_list:
            d=d+1
        print(d)
        l=51
        j=0
        
        print("this is players list inside deal", players_list)
        for nbm in range(num_players):
                b=random.randint(0,l)
                players_list[nbm].card_one=cards_list[b]
                l=l-1
                cards_list.remove(cards_list[b])
                print(players_list[nbm].card_one.suit,"of", players_list[nbm].card_one.number)
                b=random.randint(0,l)
                players_list[nbm].card_two=cards_list[b]
                l=l-1
                print(players_list[nbm].card_two.suit,"of",players_list[nbm].card_two.number)
                cards_list.remove(cards_list[b])
               

            

players_list=list()  
num_players=3
for o in range(num_players):
    players_list.append(Player())
print("this is player list", players_list)    
deck=Deck()
deck.shuffle()
deck.deal(num_players)


 
        




