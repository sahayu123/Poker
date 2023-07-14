from hand import Hand
import random 
from deck import Deck
from player import Player
class Game():
    def __init__ (self,player_list,deck):
        self.player_list=player_list
        self.deck=deck
        self.small_blind_index=random.randint(0,len(self.player_list)-1)
        hand=Hand(self.player_list,deck,self.small_blind_index)
        hand.preflop()
        hand.flop()
        hand.turn()
        hand.river()
    def remove_player_out_of_game(self,player_list):
        for p in player_list:
            if p.money<=0:
                player_list.remove(p)
                print("Player",p.name,"has been removed from the game due to a lack of funds")
        return player_list
        


    def cash_out(self,player_list):
        while True:
            option=input("Does anybody want to cash out: Yes or No : ")
            if option=="Yes":
                player_to_remove=input("Enter Player name to remove")
                set_value=False
                for p in player_list:
                    if p.name==player_to_remove:
                        set_value=True
                        player_list.remove(p)
                        player_removed=p
                        break
                
                if set_value==False:
                    print("Valid name not entered")
                    continue
                elif set_value==True:
                    print(player_removed.name,"Has been succesfully removed from the game. Player had amount",player_removed.money)
                    print("Anybody else can still cash out")
                    continue

            elif option=="No":
                return player_list
            else:
                print("Enter either Yes or No. Invalid input")
                continue
    
    def cash_in(self,player_list):
        while True:
            option=input("Does anybody want to cash in: Yes or No ")
            if option=="Yes":
                new_player=Player()
                player_list.append(new_player)
                print("Player",new_player.name,"has been succesfully added to the game")
                print("You may cash in more players as well")
                continue
            elif option=="No":
                return player_list
            else:
                print("Please enter valid input")
                continue



    def other_rounds(self):
        small_blind=self.first_small_blind
        while len(self.player_list)>0:
            
            self.player_list=self.remove_player_out_of_game(self.player_list)
             
            self.player_list=self.cash_out(self.player_list)
            self.player_list=self.cash_in(self.player_list)

            self.small_blind_index=(self.small_blind_index+1)%len(self.player_list)

            deck=Deck()
            deck.shuffle()

            self.deck=deck.deal(len(self.player_list),self.player_list)

            hand=Hand(self.player_list,self.deck,self.small_blind_index)
            hand.preflop()
            hand.flop()
            hand.turn()
            hand.river()
        
        print("Game Over")
        print("Player",player_list[0].name,"is the winner")




        

