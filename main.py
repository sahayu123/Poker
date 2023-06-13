
from player import Player
from cards import Card
from deck import Deck
from hand import Hand 


players_list=list()  
num_players=5
for o in range(num_players):
    players_list.append(Player())
print("this is player list", players_list)    
deck=Deck()
deck.shuffle()
deck1=deck.deal(num_players,players_list)

hand = Hand(players_list,deck1)
hand.preflop()
hand.flop()
hand.turn()
hand.river()