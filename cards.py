
import random
amount=0
deck=list()
for i in ["Clubs","Diamonds", "Hearts","Spades"]:
            for j in["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]:
                deck.append({"suit":i,"number":j})
                amount=amount+1
print(amount)
m=["hi",51]         
class Card:
    def __init__(self):
        r=random.randint(0,m[1])
        #print(deck[r])
        self.suit=deck[r]["suit"]
        self.number=deck[r]["number"]
        deck.remove(deck[r])
        samoa=0
        for items in deck:
          samoa =samoa+1
        #print(samoa)
        m[1]=m[1]-1
        #print("This is Gi", m[1])
count=0
lst=list()
while count<51:
  obj=Card()
  lst.append(obj)
  count=count+1
k=0
for juble in lst:
  k=k+1
#print(k)
#------------------------------------------------------------------------------------------------------------------------------
gi=["hi",51]
player_cards=list()
class Deck:
    def __init__(self):
            b=random.randint(0,gi[1])
            self.card_one=lst[b]
            lst.remove(lst[b])
            gi[1]=gi[1]-1
            b=random.randint(0,gi[1])
            self.card_two=lst[b]
            lst.remove(lst[b])
            gi[1]=gi[1]-1

amount_of_players=3
x=0
player_cards_list=list()
while x<amount_of_players:
    hj=Deck()
    player_cards_list.append(hj)
    x=x+1

for smth in player_cards_list:
  print("card one suit  : ",smth.card_one.suit,"!!!  card one number : ",smth.card_one.number,"!!!  card two suit : ",smth.card_two.suit,"!!! card two number :",smth.card_two.number)

class Player:
    def __init__(self):
        self.player_card_one_suit=player_cards_list[0].card_one.suit
        self.player_card_one_number=player_cards_list[0].card_one.number
        self.player_card_two_suit=player_cards_list[0].card_two.suit
        self.player_card_two_number=player_cards_list[0].card_two.number
        player_cards_list.remove(player_cards_list[0])

x=0
while x<amount_of_players:
    player=Player()
    
    
        





 
        

