import random

class Hand():
    def __init__(self,playe_list,deck):
        self.players_list=playe_list
        self.deck=deck
        self.previous_bet=0
        self.dealer=self.players_list[len(self.players_list)-1]
        self.small_blind=self.players_list[0]
        self.big_blind=self.players_list[1]
        self.community_cards=list()
        self.players_in_game=self.players_list
        self.round_pot=0

    def community_cards_deal(self,amount_cards,players_list):
        iter=0      
        while iter<amount_cards:
            jfk=random.randint(0,len(self.deck)-1)
            self.community_cards.append(self.deck[jfk])
            self.deck.remove(self.deck[jfk])
            iter=iter+1
        print(self.community_cards)

    def blinds_check(self,blinds):
        if blinds=="YES":
            self.small_blind.money=self.small_blind.money-1
            self.small_blind.round_status="BET"
            self.small_blind.player_bet=self.small_blind.player_bet+1
            self.small_blind.player_bet_hand=self.small_blind.player_bet_hand+1
            #print(self.small_blind.money)

            self.big_blind.money=self.big_blind.money-2
            self.big_blind.round_status=None
            self.big_blind.player_bet=self.big_blind.player_bet+2
            self.big_blind.player_bet_hand=self.big_blind.player_bet_hand+2
            #print(self.big_blind.money) 
        
            self.previous_bet=2   
            self.hand_pot=3
            self.round_pot=3
            z=2
            print("Small Blind is player 1 and has bet amount 1")
            print("Big Blind is player 2 and has bet amount 2")
            print("")
            return z
            
        
        elif blinds=="NO":
            z=0
            self.previous_bet=0
            self.hand_pot=0
            return z

    def  imput_options(self,players_list,z):
       
        print("Player",z+1,"it is your turn")
        if self.hand_pot>0 and players_list[z].player_bet!=self.hand_pot/len(players_list):
            decision1=" Call"
                
        else: 
            decision1=""
        if self.hand_pot >0:
            decision2=" Raise"
        else:
            decision2=""
        decision3=""
        if self.hand_pot==0:
            decision3=" Check"
            decision4=" Bet"
        else:
            decision3=""
            decision4=""
        if players_list[z].player_bet_hand==self.previous_bet and players_list[z].round_status==None:
            decision3=" Check"

        players_list[z].round_status=input(f"Do you want to Fold {decision1} {decision2} {decision3} {decision4} :")
    
    def call(self,players_list,z):
        players_list[z].money=players_list[z].money-(self.previous_bet-players_list[z].player_bet_hand)
        self.hand_pot=self.hand_pot+(self.previous_bet-players_list[z].player_bet_hand)
        self.round_pot=self.round_pot+(self.previous_bet-players_list[z].player_bet_hand)
        players_list[z].player_bet=players_list[z].player_bet+(self.previous_bet-players_list[z].player_bet_hand)
        players_list[z].player_bet_hand=players_list[z].player_bet_hand+(self.previous_bet-players_list[z].player_bet_hand)
        print(players_list[z].player_bet_hand)
        print("Player",z+1, "has called and has amount",players_list[z].money)
        print("Current pot is",self.round_pot)
        print("this is player bet hand",players_list[z].player_bet_hand)
        z=(z+1)%len(players_list)
        print("This is Z",z)
        print(players_list)
        return z

    def Raise(self,players_list,z):
        while True:
            raise_amount=input("Please enter raise amount :")
            try:
                players_list[z].player_bet=players_list[z].player_bet+(self.previous_bet-players_list[z].player_bet_hand)+int(raise_amount)
            except:
                print("please enter valid bet amount")
                continue
            if int(players_list[z].player_bet) > players_list[z].money:
                print("Insuffiecient funds")
                print("player",z,"only has amount",players_list[z].money)
                players_list[z].player_bet=players_list[z].player_bet-(self.previous_bet-players_list[z].player_bet_hand)-int(raise_amount)
                continue
            elif int(players_list[z].player_bet)<=0:
                print("Cannot Bet 0 or less than zero")
                players_list[z].player_bet-int(bet_amount)
                continue

            self.previous_bet=self.previous_bet+int(raise_amount)
            players_list[z].player_bet_hand=players_list[z].player_bet_hand+self.previous_bet
            self.hand_pot=self.hand_pot+self.previous_bet
            self.round_pot=self.round_pot+self.previous_bet
            players_list[z].money=players_list[z].money-self.previous_bet

            print("Player",z+1,"has Raised and has amount",players_list[z].money)
            print("Current pot is",self.round_pot)
            z=(z+1)%len(players_list)
            break
        return z

    def bet(self,players_list,z):
        while True:
            bet_amount=input("Please enter bet amount :")
            try:
                players_list[z].player_bet=players_list[z].player_bet+int(bet_amount)
            except:
                print("please enter valid bet amount")
                continue
            if int(bet_amount) > players_list[z].money:
                print("Insuffiecient funds")
                print("player",z,"only has amount",players_list[z].money)
                players_list[z].player_bet-int(bet_amount)
                continue
            elif int(bet_amount)<=0:
                print("Cannot Bet 0 or less than zero")
                players_list[z].player_bet-int(bet_amount)
                continue

            players_list[z].player_bet_hand=players_list[z].player_bet_hand+int(bet_amount)
            self.previous_bet=int(bet_amount)
            self.hand_pot=int(bet_amount)
            self.round_pot=self.round_pot+int(bet_amount)

            players_list[z].money=players_list[z].money-int(bet_amount)
            print("Player",z+1,"has bet amount",bet_amount)
            print("Current pot is",self.round_pot)
            z=(z+1)%len(players_list)
            break
        return z
    
    def round_check(self,players_list):
        check="YES"
        check2="YES"    
        jst=list()
        mk=list()
        jaz=0
        stab="YES"
        cont="k"
        for v in players_list:
            #print(v.round_status)
            if v.round_status=="Fold":
                jaz=jaz+1
                #print(jaz)
                if jaz==len(players_list)-1:
                    for g in players_list:
                        if g.round_status!="Fold":
                            print(g.name,"wins")
                            stab="NO" 
                            break  
                                        
                continue
            if stab=="NO":
                check="NO"
                cont="NO"
                return cont
            elif v.round_status==None:
                check="NO"
                break  
                
                #elif v.round_status=="BIG":
                    #check="NO"
                    #break
                #print(v.player_bet)
            print(v)
            jst.append(v.player_bet_hand)
            mk.append(v)

        if check=="YES":
            s1=jst[0]
            for c in jst:
                print(c)
                if c!=s1:
                    check2="NO"
        else:
            cont="YES"
            return cont
        if check2=="YES":
            print("Round Over")
            for pollos in mk:
                pollos.player_bet_hand=0
                pollos.round_status=None
            cont="NO"
            return cont
        else:
            cont="YES"
            return cont

    def round_betting(self,amount_cards,player_list,blinds):
        players_list=player_list.copy()
        self.community_cards_deal(amount_cards,players_list)
        z=self.blinds_check(blinds)
        while z < len(players_list):
            self.imput_options(players_list,z)
            if  players_list[z].round_status=="Call":
                z=self.call(players_list,z)
            elif players_list[z].round_status=="Raise":
                z=self.Raise(players_list,z)
            elif players_list[z].round_status=="Bet":
                z=self.bet(players_list,z)
            elif players_list[z].round_status=="Fold":
                z=(z+1)%len(players_list)
                self.players_in_game.remove(players_list[z])   
            elif players_list[z].round_status=="Check":
                z=(z+1)%len(players_list)

            cont=self.round_check(players_list)
            if cont=="YES":
                continue
            elif cont=="NO":
                break
            
    def preflop(self):
        self.round_betting(0,self.players_list,"YES")    
    
    def flop(self):
        self.round_betting(3,self.players_in_game,"NO")
    
    def turn(self):
        self.round_betting(1,self.players_in_game,"NO")   
    
    def river(self):
        self.round_betting(1,self.players_in_game,"NO")   