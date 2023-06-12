import random
class Hand():
    def __init__(self,players_list,deck):
        self.hand_pot=0
        self.players_list=players_list
        self.deck=deck
        self.previous_bet=0
        self.dealer=self.players_list[len(self.players_list)-1]
        self.small_blind=self.players_list[0]
        self.big_blind=self.players_list[1]
        self.community_cards=list()
    
    def hand(amount_cards):
        iter=0
        while iter<amount_cards:
            jfk=random.randint(0,len(self.deck)-1)
            self.community_cards=self.deck[jfk]
            self.deck.remove(self.deck[jfk])
            iter=iter+1
            print(self.community_cards)




    def preflop(self):
        self.hand()
        self.small_blind.money=self.small_blind.money-1
        self.small_blind.round_status="BET"
        self.small_blind.player_bet=self.small_blind.player_bet+1
        #print(self.small_blind.money)

        self.big_blind.money=self.big_blind.money-2
        self.big_blind.round_status=None
        self.big_blind.player_bet=self.big_blind.player_bet+2
        #print(self.big_blind.money) 
        
        self.previous_bet=2   
        self.hand_pot=3
        z=2
        print("Small Blind is player 1 and has bet amount 1")
        print("Big Blind is player 2 and has bet amount 2")
        print("")
        while z < len(self.players_list):
            print("Player",z+1,"it is your turn")
            if self.hand_pot>0 and self.players_list[z].player_bet!=self.previous_bet:
                decision1=" Call"
                
            else: 
                decision1=""
            if self.hand_pot >0:
                decision2=" Raise"
            else:
                decision2=""
            if self.hand_pot==0:
                decision4=" Bet"
                decision3=" Check"
            else:
                decision3=""
                decision4=""
            if self.players_list[z].player_bet==self.previous_bet:
                decision3=" Check"
            else:
                decision3=""
            self.players_list[z].round_status=input(f"Do you want to Fold {decision1} {decision2} {decision3} {decision4} :")
            if  self.players_list[z].round_status=="Call":
                self.players_list[z].money=self.players_list[z].money-(self.previous_bet-self.players_list[z].player_bet)
                self.hand_pot=self.hand_pot+(self.previous_bet-self.players_list[z].player_bet)
                self.players_list[z].player_bet=self.players_list[z].player_bet+(self.previous_bet-self.players_list[z].player_bet)
                print("Player",z+1, "has called and has amount",self.players_list[z].money)
                print("Current pot is",self.hand_pot)
                z=(z+1)%len(self.players_list)
               
            elif self.players_list[z].round_status=="Raise":
                
                raise_amount=input("please enter raise amount: ")
                self.players_list[z].player_bet=self.players_list[z].player_bet+(self.previous_bet-self.players_list[z].player_bet)+int(raise_amount)
                self.previous_bet=self.previous_bet+int(raise_amount)
                self.hand_pot=self.hand_pot+self.previous_bet
                self.players_list[z].money=self.players_list[z].money-self.previous_bet
                print("Player",z+1,"has Raised and has amount",self.players_list[z].money)
                print("Current pot is",self.hand_pot)
                z=(z+1)%len(self.players_list)

            
            elif self.players_list[z].round_status=="Fold":
                z=(z+1)%len(self.players_list)

                
            elif self.players_list[z].round_status=="Check":
                z=(z+1)%len(self.players_list)

            check="YES"
            check2="YES"    
            jst=list()
            jaz=0
            stab="YES"
            #make it so that big blind also has a turn
            #Make a system to see if everybody folded

            for v in self.players_list:
                #print(v.round_status)
                if v.round_status=="Fold":
                    jaz=jaz+1
                    #print(jaz)
                    if jaz==len(self.players_list)-1:
                        for g in self.players_list:
                            if g.round_status!="Fold":
                                print(g.name,"wins")
                                stab="NO" 
                                break  
                                        
                    continue
                    if stab=="NO":
                        break
                elif v.round_status==None:
                    check="NO"
                    break  
                #elif v.round_status=="BIG":
                    #check="NO"
                    #break
                #print(v.player_bet)
                jst.append(v.player_bet)
                
            if check=="YES":
                s1=jst[0]
                for c in jst:
                    if c!=s1:
                        check2="NO"
            else:
                continue
            if check2=="YES":
                print("Round Over")
                break
            else:
                continue

        