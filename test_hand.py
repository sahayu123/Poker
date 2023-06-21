import pytest
from hand import Hand
from player import Player
from deck import Deck
from cards import Card

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
    cont_values=["NO","WON","YES","NO","YES","YES"]
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
       
def test_check_straight_flush():

    players_list=list()
    player=Player()
    players_list.append(player)
    player=Player()
    players_list.append(player)
    deck=Deck()
    deck.shuffle()
    deck1=deck.deal(1,players_list)
    hand=Hand(deck1,players_list)
    
    player_one_card=[Card("Clubs","6"),
                     Card("Clubs","9"),
                     Card("Clubs","Jack"),
                     Card("Clubs","2"),
                     Card("Clubs","8"),
                     Card("Clubs","Ace")]

    player_two_card=[Card("Clubs","9"),
                    Card("Clubs","10"),
                    Card("Clubs","10"),
                    Card("Hearts","3"),
                    Card("Clubs","4"),
                    Card("Clubs","King")]
    
    community_cards=[[Card("Clubs","7"),Card("Clubs","2"),Card("Clubs","8"),Card("Clubs","10"),Card("Clubs","5")],
                     [Card("Clubs","7"),Card("Clubs","2"),Card("Clubs","8"),Card("Clubs","Jack"),Card("Clubs","5")],
                    [Card("Hearts","7"),Card("Spades","2"),Card("Clubs","8"),Card("Clubs","Queen"),Card("Clubs","9")],
                    [Card("Hearts","7"),Card("Spades","2"),Card("Clubs","8"),Card("Clubs","Queen"),Card("Clubs","9")],
                    [Card("Hearts","7"),Card("Spades","2"),Card("Clubs","8"),Card("Clubs","Queen"),Card("Clubs","9")],
                    [Card("Hearts","7"),Card("Spades","2"),Card("Clubs","Jack"),Card("Clubs","Queen"),Card("Clubs","10")]
 ]
 
    results=[True,True,True,False,False,True]
    x=0
    while x<len(player_two_card):
        players_list[0].card_one=player_one_card[x]
        players_list[0].card_two=player_two_card[x]
   
        hand=Hand(players_list,deck1)
        hand.community_cards=community_cards[x]
        print("This is community cards",hand.community_cards)
    
        j=hand.check_straight_flush(players_list[0])
        print("this is test",x)
        print("This is J",j)
        assert j[0]==results[x]
        x=x+1

def test_check_four_of_a_kind():
    players_list=list()
    player=Player()
    players_list.append(player)
    player=Player()
    players_list.append(player)
    deck=Deck()
    deck.shuffle()
    deck1=deck.deal(1,players_list)
    hand=Hand(deck1,players_list)
    cards=[[7,5,7,9,10,7,7],[7,6,8,9,7,7,10],[8,8,8,7,7,7,10]]
    reults=[True,False,False]
    x=0
    
    while x<len(cards):
        print("4---------------------------4--------------------------------4--------------------4------")
        cards[x].sort(reverse=True)
        z=hand.four_of_a_kind(players_list[0],cards[x])
        assert reults[x]==z[0]
        x=x+1
        print("4-----------------4-----------------------------4-------------------------4---------")

def test_check_three_of_a_kind():
    players_list=list()
    player=Player()
    players_list.append(player)
    player=Player()
    players_list.append(player)
    deck=Deck()
    deck.shuffle()
    deck1=deck.deal(1,players_list)
    hand=Hand(deck1,players_list)
    cards=[[7,5,10,9,10,7,7],[7,6,6,6,7,7,10],[8,5,8,7,9,7,10]]
    reults=[True,True,False]
    return_expected=[[7,7,7],[7,7,7],None]
    x=0
    
    while x<len(cards):
        print("---------3-----------------------------3-------------------------------3---------------------")
        cards[x].sort(reverse=True)
        z=hand.three_of_a_kind(players_list[0],cards[x])
        assert reults[x]==z[0]
        assert return_expected[x]==z[1]
        x=x+1
        print("-------------3----------------------------3----------------------3----------------------------")

def test_pair():
    players_list=list()
    player=Player()
    players_list.append(player)
    player=Player()
    players_list.append(player)
    deck=Deck()
    deck.shuffle()
    deck1=deck.deal(1,players_list)
    hand=Hand(deck1,players_list)
    cards=[[7,5,10,9,10,9,7],[11,8,6,6,7,7,10],[8,5,14,11,9,7,10]]
    reults=[True,True,False]
    return_expected=[[10,10],[7,7],None]
    x=0
    
    while x<len(cards):
        print("---------2-----------------------------2-------------------------------2---------------------")
        cards[x].sort(reverse=True)
        z=hand.pair(players_list[0],cards[x])
        assert reults[x]==z[0]
        assert return_expected[x]==z[1]
        x=x+1
        print("-------------2----------------------------2----------------------2----------------------------")

def test_two_pair():
    players_list=list()
    player=Player()
    players_list.append(player)
    player=Player()
    players_list.append(player)
    deck=Deck()
    deck.shuffle()
    deck1=deck.deal(1,players_list)
    hand=Hand(deck1,players_list)
    cards=[[7,5,10,9,10,9,7],[11,8,6,6,7,7,10],[8,5,14,11,9,7,10]]
    reults=[True,True,False]
    return_expected=[[10,10,9,9],[7,7,6,6],None]
    x=0
    
    while x<len(cards):
        print("---------2-2----------------------------2-2------------------------------2-2--------------------")
        cards[x].sort(reverse=True)
        z=hand.two_pair(players_list[0],cards[x])
        print("this is z",z)
        assert reults[x]==z[0]
        assert return_expected[x]==z[1]
        x=x+1
        print("-------------2-2---------------------------2-2---------------------2-2---------------------------")

def test_full_house():
    players_list=list()
    player=Player()
    players_list.append(player)
    player=Player()
    players_list.append(player)
    deck=Deck()
    deck.shuffle()
    deck1=deck.deal(1,players_list)
    hand=Hand(deck1,players_list)
    cards=[[7,5,10,10,10,9,7],[11,6,6,6,7,7,7],[8,5,14,11,9,7,10]]
    reults=[True,True,False]
    return_expected=[[10,10,10,7,7],[7,7,7,6,6],None]
    x=0
    
    while x<len(cards):
        print("---------3-2----------------------------3-2------------------------------3-2--------------------")
        cards[x].sort(reverse=True)
        z=hand.full_house(players_list[0],cards[x])
        print("this is z",z)
        assert reults[x]==z[0]
        assert return_expected[x]==z[1]
        x=x+1
        print("------------3-2---------------------------3-2---------------------3-2---------------------------")