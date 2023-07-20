
from player import Player
from cards import Card
from deck import Deck
from hand import Hand 
from game import Game


players_list=list()  
num_players=5

for o in range(num_players):
    players_list.append(Player())
    
print("this is player list", players_list)    


game=Game(players_list)
game.other_rounds()
