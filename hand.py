import random

class Hand():
    def __init__(self,player_list,deck):
        '''The init method of the hand class intitializes the attrbitutes of the hand.
        parameters:
        1. The list of players is the first parameter.
        2. The deck of cards is the second parameter. '''
        self.players_list=player_list
        self.deck=deck
        self.previous_bet=0
        self.dealer=self.players_list[len(self.players_list)-1]
        self.small_blind=self.players_list[0]
        self.big_blind=self.players_list[1]
        self.community_cards=list()
        self.players_in_game=self.players_list
        self.round_pot=0
        self.hand_pot=0
        
    def community_cards_deal(self,amount_cards,players_list):
        '''The community_cards_deal method of the hand class deals cards to the community cards attribute.
            parameters:
            1. The amount of cards needed to be dealt is the first parameter.
            2.The list of players if the second parameter. '''
        iter=0      
        while iter<amount_cards:
            jfk=random.randint(0,len(self.deck)-1)
            self.community_cards.append(self.deck[jfk])
            self.deck.remove(self.deck[jfk])
            iter=iter+1
        print(self.community_cards)

    def blinds_check(self,blinds):
        '''
        The blinds_check method of the Hand class, sets the blind attributes and intiazlizes the start of the game.
        parameters:
        1. This paramters takes an input of YES or NO, if YES is entered blind values are intialized, if NO is entered,there will be no blind values.
        returns:
        1. returns the internery number, for who should start the round, if YES is entered iternary variable will be 2, if no is entered iternary variable will be 0.
        '''
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

    def imput_options(self,players_list,z,test="NO"):
        '''
        The imput_options method of the Hand class, calculates what decision the player is able to make depending on certain criteria.
        parameters:
        1.The first parameter is the list of players.
        2.The second parameter is the iternary variable. 
        '''
        print("Player",z+1,"it is your turn")
        if self.hand_pot>0 and players_list[z].player_bet_hand!=self.previous_bet:
            self.decision1="Call"
                
        else: 
            self.decision1=""
        if self.hand_pot >0:
            self.decision2="Raise"
        else:
            self.decision2=""
        self.decision3=""
        if self.hand_pot==0:
            self.decision3="Check"
            self.decision4="Bet"
        else:
            self.decision3=""
            self.decision4=""
        if players_list[z].player_bet_hand==self.previous_bet and players_list[z].round_status==None:
            self.decision3="Check"
        if test=="NO":
            players_list[z].round_status=input(f"Do you want to Fold {self.decision1} {self.decision2} {self.decision3} {self.decision4} :")
         
    def call(self,players_list,z):
        '''
        The call method of the Hand class reacts to when the player wants to call and sets their attributes accordingly.
        parameters:
        1.The first parameter is the players list 
        2. The second parameter is the iternary variable 
        returns:
        1.It returns the itenary variable.
        '''
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

    def Raise(self, players_list, z):
      
        '''
        The Raise method of the Hand class reacts to when the player wants to Raise and sets their attributes accordingly.
        parameters:
        1. The first parameter is the players list 
        2. The second parameter is the itinerary variable 
        returns:
        1. It returns the itinerary variable.
        '''
        while True:
            raise_amount = input("Please enter raise amount: ")
            try:
                players_list[z].player_bet = players_list[z].player_bet + (self.previous_bet - players_list[z].player_bet_hand) + int(raise_amount)
            except:
                print("Please enter a valid bet amount")
                continue
            if int(players_list[z].player_bet) > players_list[z].money:
                print("Insufficient funds")
                print("Player", z+1, "only has amount", players_list[z].money)
                players_list[z].player_bet = players_list[z].player_bet - (self.previous_bet - players_list[z].player_bet_hand) - int(raise_amount)
                print(players_list[z].player_bet)
                continue
            elif int(raise_amount) <= 0:
                print("Cannot bet 0 or less than zero")
                players_list[z].player_bet = players_list[z].player_bet - (self.previous_bet - players_list[z].player_bet_hand) - int(raise_amount)
                print(players_list[z].player_bet)
                continue
            break
        self.hand_pot = self.hand_pot + (self.previous_bet - players_list[z].player_bet_hand) + int(raise_amount)
        self.round_pot = self.round_pot + self.previous_bet
        players_list[z].money = players_list[z].money - self.previous_bet
        players_list[z].player_bet_hand = players_list[z].player_bet_hand + self.previous_bet
        self.previous_bet = self.previous_bet +int(raise_amount)


        print("Player", z+1, "has raised and has amount", players_list[z].money)
        print("Current pot is", self.round_pot)
        z = (z + 1) % len(players_list)  
        return z
   
    def bet(self,players_list,z,):
        '''
        The bet method of the Hand class reacts to when the player wants to bet and sets their attributes accordingly.
        parameters:
        1.The first parameter is the players list 
        2. The second parameter is the iternary variable 
        returns:
        1.It returns the itenary variable.
        '''
        while True:
            bet_amount=input("Please enter bet amount :")
            try:
                players_list[z].player_bet=players_list[z].player_bet+int(bet_amount)
            except:
                print("please enter valid bet amount")
                continue
            if int(bet_amount) > players_list[z].money:
                print("Insuffiecient funds")
                print("player",z+1,"only has amount",players_list[z].money)
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
        '''The round_check of the Hand class, checks if the round is over or not and it checks if there is a winner through folding.
        parameters:
        1.The frst parameter is the list of players
        returns:
        1.It returns YES or NO, it returns YES, when the round should continue and NO when the round should end. '''
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
                            g.round_status="Won_hand"
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
            #print(v)
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
        '''The round_betting class of the Hand class, implements the betting system for the Poker game.
        parameters:
            1. The first parameter is the amout of community cards needed to be dealt in the round
            2. The second parameter is the list of players
            3. The third parameter  takes an input of YES or NO, if YES is entered blind values are intialized, if NO is entered,there will be no blind values. '''
        players_list=player_list.copy()
        self.community_cards_deal(amount_cards,players_list)
        z=self.blinds_check(blinds)
        while z < len(players_list):
            if players_list[z].round_status=="Fold":
                print("This is fold z",z)
                z=(z+1)%len(players_list)
                continue
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
        '''The preflop method of the Hand class implemets betting for the preflop round'''
        self.round_betting(0,self.players_list,"YES")    
    
    def flop(self):
        '''The flop method of the Hand class implements betting for the flop round'''
        self.round_betting(3,self.players_in_game,"NO")
    
    def turn(self):
        '''The turn method of the Hand class implements betting for the turn round'''

        self.round_betting(1,self.players_in_game,"NO")   
    
    def river(self):
        '''The river method of the Hand class implements betting for the river round'''

        self.round_betting(1,self.players_in_game,"NO")   