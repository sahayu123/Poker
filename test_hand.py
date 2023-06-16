import pytest
from hand import Hand
from player import Player
from deck import Deck

def test_input_function():
    hand_pot_values=[8,0,10,5]
    hand_previous_bet_values=[2,0,2,3]
    hand_decision_1_values=["Call","","","Call"]
    hand_decision_2_values=["Raise","","Raise","Raise"]
    hand_decision_3_values=["","Check","Check",""]
    hand_decision_4_values=["","Bet","",""]
    z_values=[4,1,0,2]
    j=0
    while j<len(hand_pot_values):
        num_players=5
        players_list=list()
        
        player=Player()
        player.player_bet_hand=[2,0,2,2][j]
        player.round_status=["Call","Fold",None,"Bet"][j]
        players_list.append(player) 

        player=Player()
        player.player_bet_hand=[2,0,2,3][j]
        player.round_status=["Call",None,"Call","Raise"][j]
        players_list.append(player) 

        player=Player()
        player.player_bet_hand=[2,0,2,0][j]
        player.round_status=["Call",None,"Call",None][j]
        players_list.append(player) 

        player=Player()
        player.player_bet_hand=[2,0,2,0][j]
        player.round_status=["Call",None,"Call",None][j]
        players_list.append(player) 

        player=Player()
        player.player_bet_hand=[0,0,2,0][j]
        player.round_status=[None,None,"Call",None][j]
        players_list.append(player) 

        
        deck=Deck()
        deck.shuffle()
        deck1=deck.deal(num_players,players_list)
        hand=Hand(deck1,players_list)
        hand.hand_pot=hand_pot_values[j]
        hand.previous_bet=hand_previous_bet_values[j]
        z=z_values[j]
        hand.imput_options(players_list,z,"YES")
        assert hand.decision1==hand_decision_1_values[j] and hand.decision2==hand_decision_2_values[j] and hand.decision3==hand_decision_3_values[j] and hand.decision4==hand_decision_4_values[j]
        j=j+1

def test_check_function():
    j=0
    cont_values=["NO","NO","YES","NO","YES"]
    while j<len(cont_values):
        players_list=list()
        num_players=5
        player=Player()
        player.player_bet_hand=[2,0,1,0,0,3][j]
        player.round_status=["Bet","Fold","Bet","Check","Check","Raise"][j]
        players_list.append(player) 

        player=Player()
        player.player_bet_hand=[2,2,2,0,0,2][j]
        player.round_status=["Call","Bet",None,"Check","Check","Call"][j]
        players_list.append(player) 

        player=Player()
        player.player_bet_hand=[2,0,2,0,0,2][j]
        player.round_status=["Call","Fold","Call","Check","Check","Call"][j]
        players_list.append(player) 

        player=Player()
        player.player_bet_hand=[2,0,2,0,0,2][j]
        player.round_status=["Call","Fold","Call","Check","Check","Call"][j]
        players_list.append(player) 

        player=Player()
        player.player_bet_hand=[2,0,2,0,2,2][j]
        player.round_status=["Call","Fold","Call","Check","Bet","Call"][j]
        players_list.append(player) 

        deck=Deck()
        deck.shuffle()
        deck1=deck.deal(num_players,players_list)
        hand=Hand(deck1,players_list)

        cont_value=hand.round_check(players_list)
        assert cont_value==cont_values[j]
        j=j+1
       
