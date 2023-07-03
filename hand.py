import random
from cards import Card
from operator import itemgetter
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
            players_list[z].round_status=input(f"Do you want to Fold {self.decision1} {self.decision2} {self.decision3} {self.decision4} {self.decision5} :")
         
    def call(self,players_list,z):
        '''
        The call method of the Hand class reacts to when the player wants to call and sets their attributes accordingly.
        parameters:
        1.The first parameter is the players list 
        2. The second parameter is the iternary variable 
        returns:
        1.It returns the itenary variable.
        '''
        
        if int(self.previous_bet-players_list[z].player_bet_hand) >= players_list[z].money:
            players_list[z].round_status="All_In"
            self.hand_pot=self.hand_pot+players_list[z].money
            self.round_pot=self.round_pot+players_list[z].money
            players_list[z].players_bet=players_list[z].player_bet+players_list[z].money
            players_list[z].players_bet_hand=players_list[z].player_bet_hand+players_list[z].money
            players_list[z].money=0
        
        else:
            players_list[z].money=players_list[z].money-(self.previous_bet-players_list[z].player_bet_hand)
            self.hand_pot=self.hand_pot+(self.previous_bet-players_list[z].player_bet_hand)
            self.round_pot=self.round_pot+(self.previous_bet-players_list[z].player_bet_hand)
            players_list[z].player_bet=players_list[z].player_bet+(self.previous_bet-players_list[z].player_bet_hand)
            players_list[z].player_bet_hand=players_list[z].player_bet_hand+(self.previous_bet-players_list[z].player_bet_hand)
        
           
        print("This is player bet hand",players_list[z].player_bet_hand)
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

        if plaeyrs_list[z].money==0:
            players_list[z].round_status="All_In"

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

            if plaeyrs_list[z].money==0:
                players_list[z].round_status="All_In"

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
                print(jaz)
                if jaz==len(players_list)-1:
                    for g in players_list:
                        if g.round_status!="Fold":
                            g.round_status="Won_hand"
                            g.money=g.money+self.round_pot
                            print(g.name,"wins")
                            print(g.name,"has amount",g.money)
                            stab="NO" 
                            break  
                                        
        for v in players_list:
            if stab=="NO":
                check="NO"
                cont="WON"
                return cont
            elif v.round_status==None:
                check="NO"
                break  
            elif v.round_status=="All-In":
                continue
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
                #print("This is fold z",z)
                z=(z+1)%len(players_list)
                continue
            elif players_list[z].round_status=="All_In":
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
            print(cont)
            if cont=="YES":
                continue
            elif cont=="NO":
                break
            elif cont=="WON":
                return "NO_NEW_ROUND"
#--------------------------------------------------------------------------------------------------------------   
    def check_straight_method(self,f,x,g):
        #print("This is x",x)
        #print("This is f list",f)
        while x<g:
            if f[x]==f[x+1]-1:
                print("Checking this ",f[x],"and this",f[x+1])
                straight=True
            else:
                straight=False
                return straight,None        
            x=x+1
        return straight,f

    def pairs_method(self,cards,val,need_high_card,x=False):
        print("Thi si sinput cards",cards)
        item_present=False
        count=dict()
        for c in cards:
            if c not in count:
                count[c]=[1,[c]]
                #print("This is number",count[c][1],"This is count",count[c][0])
            else:
                count[c][0]=count[c][0]+1
                count[c][1].append(c)
                #print("This is number",count[c],"This is count", count[c][0])
            print("this is count",count)
            if count[c][0]==val:
                high_cards=list()
                item_present=True
                if need_high_card:
                    for k in cards:
                        print("This is first count[c][1]",count[c][1])
                        print("This is k",k)
                        if count[c][1][0] !=k:
                            high_cards.append(k)
                            print("This is high cards",high_cards)
                    high_cards.sort(reverse=True)
                    print("THis is high cards limited",high_cards[0:5-val])
                    for j in high_cards[0:5-val]:
                        print(count[c][1])
                        count[c][1].append(j)
                    print("This is count[c][1]",count[c][1])
                    if x:
                        return item_present,count[c][1][0:5-val]
                    else:
                        return item_present,count[c][1][0:5]
                return item_present,count[c][1]    
        return item_present,None   
   
    def multiple_pairs_method(self,cards,val):
        if val==3:
            need_high_card=False
        else:
            need_high_card=True
        print("THis is need high card",need_high_card)
        ret=self.pairs_method(cards,val,False)
        print("THIS IS RET1",ret[1])
        if ret[0]==False:
            return ret
        elif ret[0]==True:
            new_cards=cards.copy()
            old_cards=list()
            for x in ret[1]:
                old_cards.append(x)
                new_cards.remove(x)
            ret2=self.pairs_method(new_cards,2,need_high_card,True)
            print("THIS IS RET2",ret2[1])
            #print("This is ret2",ret2)
            if ret2[0]==False:
                return ret2
            elif ret2[0]==True:
                for x in ret2[1]:
                    old_cards.append(x)
                print("This is old cards",old_cards)
                return ret2[0],old_cards
       
    def calculate_decimal_points(self,cards):
        new_cards=cards.copy()
        print("This is new_cards",new_cards)
        final_number=""
        for jhy in new_cards:
            print("This is jhy ",jhy)
            if jhy<10:
                final_number=final_number+"0"+str(jhy)
                print("This is final_number",final_number)
            else:
                final_number=final_number+str(jhy)
                print("This is final_number",final_number)
        #14 10 14 09 06
        #1,000,000,000
        final_number_return_value=int(final_number)
        print("This is final_number_return_value",final_number_return_value)
        actual_final_number_return_value=final_number_return_value/10000000000
        print("This is actual final number return value",actual_final_number_return_value)
        return actual_final_number_return_value       
#-------------------------------------------------------------------------------------------------------------------
    def check_flush(self,p):       
        suit_count=dict()
        suit_count["Diamonds"]=[0,[]] 
        suit_count["Clubs"]=[0,[]]    
        suit_count["Spades"]=[0,[]]    
        suit_count["Hearts"]=[0,[]]    
        print("------------------------flush---------------------------------------------------------")   
        for x in self.community_cards:
            #print("This is x number",x.number)
            print("This is x suit",x.suit,"This is x number",x.number)
            suit_count[x.suit][0]=suit_count[x.suit][0]+1
            suit_count[x.suit][1].append(x.number_value)

        suit_count[p.card_one.suit][0]=suit_count[p.card_one.suit][0]+1
        suit_count[p.card_one.suit][1].append(p.card_one.number_value)   
        print("This is card 1 suit",p.card_one.suit,"This is card 1 number",p.card_one.number)
        suit_count[p.card_two.suit][0]=suit_count[p.card_two.suit][0]+1
        suit_count[p.card_two.suit][1].append(p.card_two.number_value) 
        print("This is card 2 suit",p.card_one.suit,"This is card 2 number",p.card_one.number)
        print("--------flush-----------------------------flush--------------------------------------")
        if suit_count["Clubs"][0]>=5:
            #print("This is suit_count lenght",len(suit_count["Clubs"][1]))
            suit_count["Clubs"][1].sort(reverse=True)
            dec_val=self.calculate_decimal_points(suit_count["Clubs"][1][0:5])
            return True,suit_count["Clubs"][1][0:5],dec_val,suit_count["Clubs"][1]

        elif suit_count["Hearts"][0]>=5:
            suit_count["Hearts"][1].sort(reverse=True)
            dec_val=self.calculate_decimal_points(suit_count["Hearts"][1][0:5])
            return True,suit_count["Hearts"][1][0:5],dec_val,suit_count["Hearts"][1]
                 
        elif suit_count["Diamonds"][0]>=5:
            suit_count["Diamonds"][1].sort(reverse=True)
            dec_val=self.calculate_decimal_points(suit_count["Diamonds"][1][0:5])
            return True,suit_count["Diamonds"][1][0:5],dec_val,suit_count["Diamonds"][1]
            
        elif suit_count["Spades"][0]>=5:
            suit_count["Spades"][1].sort(reverse=True)
            dec_val=self.calculate_decimal_points(suit_count["Spades"][1][0:5])
            return True,suit_count["Spades"][1][0:5],dec_val,suit_count["Spades"][1]
        else:
            return False,None,None,None
    
    def check_straight(self,p,cards):
        f=list()
        for item in cards:
            #print(cards)
            if item==14:
                New_ace=1
                f.append(New_ace)

            f.append(item)
        f.sort(reverse=True)
        x=0
        count=1
        lst=list()
        lst.append(f[0])
        while x<len(f)-1:
            if f[x]==f[x+1]+1:
                count=count+1
                if f[x] not in lst:
                    lst.append(f[x])
                    count=count+1
                lst.append(f[x+1])
                print("THIS IS LST",lst)
                print("THIS IS X",x)
                print("THIS IS COUNT",count)
            else:
                count=0
                lst=list()
            if count==5:
                dec_points=self.calculate_decimal_points(lst)
                #j=False
                return True,dec_points
            else:
                x=x+1
                print("THIS IS X",x)
       
        return False,None

         
        #print("This is f lenght",len(f))
        #print("This is f",f)
       
    def check_straight_flush(self,p):  
        val=self.check_flush(p)
        if val[0]==False:
            return False,None
        elif val[0]==True:
            print("---------------straight--------------------------------straight---------")
            print("This is card object list",val[3])
            k=list()
            bol=self.check_straight(p,val[3])
            print("THIS IS BOL",bol[1])
            print("-------------------straight-----------------straight-------------------")
        return bol


                #return "STRAIGHT_FLUSH"
    
    def four_of_a_kind(self,p,cards):
       ret=self.pairs_method(cards,4,True)
       print("tHIS IS RET[1]",ret[1])
       if ret[1]==None:
            return False,None
       soup=self.calculate_decimal_points(ret[1])
       return ret[0],soup

    def three_of_a_kind(self,p,cards):
        ret=self.pairs_method(cards,3,True)
        if ret[1]==None:
            return False,None
        soup=self.calculate_decimal_points(ret[1])
        return ret[0],soup
    
    def pair(self,p,cards):
        ret=self.pairs_method(cards,2,True)
        if ret[1]==None:
            return False,None
        soup=self.calculate_decimal_points(ret[1])
        return ret[0],soup

    def two_pair(self,p,cards):
        ret=self.multiple_pairs_method(cards,2)
        if ret[1]==None:
            return False,None
        soup=self.calculate_decimal_points(ret[1])
        return ret[0],soup
    
    def full_house(self,p,cards):
        ret=self.multiple_pairs_method(cards,3)
        if ret[1]==None:
            return False,None
        soup=self.calculate_decimal_points(ret[1])
        return ret[0],soup
    
    def high_card(self,p,cards):
        the_cards=list()
        for x in cards:
            the_cards.append(x)
        the_cards.sort(reverse=True)
        new_cards=the_cards[0:5]
        final_number=""
        for jhy in new_cards:
            print("This is jhy ",jhy)
            if jhy<10:
                final_number=final_number+"0"+str(jhy)
                print("This is final_number",final_number)
            else:
                final_number=final_number+str(jhy)
                print("This is final_number",final_number)
        #14 10 14 09 06
        #1,000,000,000
        final_number_return_value=int(final_number)
        print("This is final_number_return_value",final_number_return_value)
        actual_final_number_return_value=final_number_return_value/1000000000
        print("This is actual final number return value",actual_final_number_return_value)
        return actual_final_number_return_value
#----------------------------------------------------------------------------------------------------------------
    def player_grade(self,info,test=False):
        new_list=sorted(info,key=itemgetter(0),reverse=True)
        count=dict()
        for j in new_list:
            if j[0] not in count:
                count[j[0]]=[1,[j[1]]]
            else:
                count[j[0]][0]=count[j[0]][0]+1
                count[j[0]][1].append(j[1])
        
        max_score_list=info.copy()
        for p in new_list:
            if p[1].round_status=="All-In":
                player_all_in=True
            else:
                player_all_in=False
            print("This is count[p][0]",count[p[0]][0])
            if count[p[0]][0]>1:
                player_tied=True
            else:
                player_tied=False
            print("This is player_all_in",player_all_in)
            if player_all_in==False and player_tied==False:
                print("this is pre self.hand_pot",self.hand_pot)
                p[1].money=p[1].money+self.hand_pot
                print("This is self.hand_pot",self.hand_pot)
                self.hand_pot=0

                return p[1].money
                break
            elif player_all_in==True and player_tied==False:
                
                print("This is pre hand.pot",self.hand_pot)
                val=self.hand_pot-(p[1].player_bet*len(max_score_list))
                if val<0:
                    p[1].money=p[1].money+self.hand_pot
                    self.hand_pot=0
                else:
                    self.hand_pot=val
                    p[1].money=p[1].money+(p[1].player_bet*len(max_score_list))
                    print("This is p money",p[1].money)
                    print("This is hand.pot",self.hand_pot)
                max_score_list.remove(p)

                if self.hand_pot==0:
                    for x in max_score_list:
                        if x[1].player_bet>p[1].player_bet:
                            x[1].money=x[1].money+(x[1].player_bet-p[1].player_bet)
                    return p[1].money
                    break
                else:
                    
                    continue
                    
            elif player_all_in==False and player_tied==True:
                rt_vals=list()
                print("This is len(ties)",count[p[0]][0])
                for j in count[p[0]][1]:
                    print("this is pre j[1] money",j.money)
                    j.money=j.money+self.hand_pot/count[p[0]][0]
                    print("This is hand pot",self.hand_pot)
                    print("This is j[1].money",j.money)
                    rt_vals.append(j.money)
                self.hand_pot=0
                print("thIS IS RT_VALS",rt_vals)
                return rt_vals
                break
            elif player_all_in==True and player_tied==True:
                print("this is formula",p[1].player_bet*len(max_score_list)/count[p[0]][0])
                print("this is p[1].money pre",p[1].money)
                p[1].money=p[1].money+(p[1].player_bet*len(max_score_list))/count[p[0]][0]
                print("this is p[1].money",p[1].money)
                self.hand_pot=self.hand_pot-(p[1].player_bet*len(max_score_list))/count[p[0]][0]
                count[p[0]][0]=count[p[0]][0]-1
                count[p[0]][1]=count[p[0]][1].remove(p[1])
                max_score_list.remove(p)
                print("this is max_score_list",max_score_list)
                continue
        return new_list[0][1].money





               
            

    def check_winner(self,players_list):
        points_list=list()
        for p in players_list:
            list_cards=list()
            cards=self.community_cards
            cards.append(p.card_one)
            cards.append(p.card_two)
            for c in cards:
                list_cards.append(c.number_value)
            list_cards.sort(reverse=True)

            val=self.check_straight_flush(p)
            if val[0]==True:
                point_value=9+val[1]
                points_list.append([point_value,p])
                continue
                
               #return "STRAIGHT_FLUSH"
            elif val[0]==False:
                val=self.four_of_a_kind(p,list_cards)
            
            if val[0]==True:
                point_value=8+val[1]
                points_list.append([point_value,p])
                continue
                #return "FOUR_OF_A_KIND"
            elif val[0]==False:
                val=self.full_house(p,list_cards)

            if val[0]==True:
                point_value=7+val[1]
                points_list.append([point_value,p])
                continue
                #return "FULL_HOUSE"
            elif val[0]==False:
                val=self.check_flush(p)
            
            if val[0]==True:
                point_value=6+val[2]
                points_list.append([point_value,p])
                continue
                #return "FLUSH"
            elif val[0]==False:
                val=self.check_straight(p,list_cards)
           
            if val[0]==True:
                point_value=5+val[1]
                points_list.append([point_value,p])
                continue
                #return "STRAIGHT"
            elif val[0]==False:
                val=self.three_of_a_kind(p,list_cards)

            if val[0]==True:
                point_value=4+val[1]
                points_list.append([point_value,p])
                continue
                #return "THREE_OF_A_KIND"
            elif val[0]==False:
                val=self.two_pair(p,list_cards)

            if val[0]==True:
                point_value=3+val[1]
                points_list.append([point_value,p])
                continue
                #return "TWO_PAIR"
            elif val[0]==False:
                val=self.pair(p,list_cards)
            
            if val[0]==True:
                point_value=2+val[1]
                points_list.append([point_value,p])
                continue
                #return "PAIR"
            elif val[0]==False:
                high_card_value=self.high_card(p,cards)
                points_list.append([high_card_value,p])
                #return "HIGH_CARD"
        self.player_grade(points_list)
            
    def preflop(self):
        '''The preflop method of the Hand class implemets betting for the preflop round'''
        self.new_round=self.round_betting(0,self.players_list,"YES")    
    
    def flop(self):
        '''The flop method of the Hand class implements betting for the flop round'''
        if self.new_round != "NO_NEW_ROUND":
            self.new_round=self.round_betting(3,self.players_in_game,"NO")
    
    def turn(self):
        '''The turn method of the Hand class implements betting for the turn round'''
        if self.new_round != "NO_NEW_ROUND":
           self.new_round= self.round_betting(1,self.players_in_game,"NO")   
    
    def river(self):
        '''The river method of the Hand class implements betting for the river round'''
        if self.new_round != "NO_NEW_ROUND":
            self.new_round=self.round_betting(1,self.players_in_game,"NO")   
            if self.new_round !="NOw_NEW_ROUND":
                self.check_winner(self.players_in_game)
