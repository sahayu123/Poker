import random
from cards import Card
from operator import itemgetter
from utility import Utility
import tkinter
from PIL import ImageTk, Image
import time 


class Hand():
    def __init__(self,player_list,deck,small_blind=0):
        '''The init method of the hand class intitializes the attrbitutes of the hand.
        parameters:
        1. The list of players is the first parameter.
        2. The deck of cards is the second parameter. '''
        
        self.players_list=player_list
        self.deck=deck
        self.previous_bet=0
        #self.dealer=self.players_list[len(self.players_list)-1]
        self.small_blind=self.players_list[0]
        self.big_blind=self.players_list[1]
        self.community_cards=list()
        self.players_in_game=self.players_list.copy()
        self.round_pot=0
        self.hand_pot=0
        self.stop_next_turn=False
       
      
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
        print("")
        for x in self.community_cards:
            print(x.number,x.suit)
        print("")
        #print(self.community_cards)

    def blinds_check(self,blinds,player_list):
        '''
        The blinds_check method of the Hand class, sets the blind attributes and intiazlizes the start of the game.
        parameters:
        1. This paramters takes an input of YES or NO, if YES is entered blind values are intialized, if NO is entered,there will be no blind values.
        returns:
        1. returns the internery number, for who should start the round, if YES is entered iternary variable will be 2, if no is entered iternary variable will be 0.
        '''
        print("in blinds check")
        if blinds=="YES":
            print("in blinds yes")
            if self.small_blind.money<=1:
                self.small_blind.player_bet=self.small_blind.money
                self.small_blind.player_bet_hand=self.small_blind.money
                self.small_blind.round_status="All-In"
                self.hand_poy=self.hand_pot+self.small_blind.money
                self.round_pot=self.round_pot + self.small_blind.money
                self.small_blind.money=0
            else:
                self.small_blind.money=self.small_blind.money-1
                self.small_blind.round_status="BET"
                self.small_blind.player_bet=1
                self.small_blind.player_bet_hand=1
                self.hand_pot=self.hand_pot+1
                self.round_pot=self.round_pot+1
                #print(self.small_blind.money)
            if self.big_blind.money<=2:
                self.big_blind.player_bet=self.big_blind.money
                self.big_blind.player_bet_hand=self.big_blind.money
                self.big_blind.round_status="All-In"
                self.hand_poy=self.hand_pot+self.big_blind.money
                self.round_pot=self.round_pot+self.big_blind.money
                self.previous_bet=self.big_blind.money
                self.big_blind.money=0


            else:
                self.big_blind.money=self.big_blind.money-2
                self.big_blind.round_status=None
                self.big_blind.player_bet=2
                self.big_blind.player_bet_hand=2
                self.hand_pot=self.hand_pot+2
                self.round_pot=self.round_pot+2
                self.previous_bet=2   
                print("this is previous bet in blinds check",self.previous_bet)
                #print(self.big_blind.money) 
            z=2%len(player_list)
            print("Small Blind is player ",self.small_blind.name," and has bet amount",self.small_blind.player_bet)
            print("Big Blind is player ",self.big_blind.name,"and has bet amount ",self.big_blind.player_bet)
            print("")
            return z
            
        
        elif blinds=="NO":
            print("in blinds no")
            z=0
            self.previous_bet=0
            return z

    def call(self,players_list,z,root):
        '''
        The call method of the Hand class reacts to when the player wants to call and sets their attributes accordingly.
        parameters:
        1.The first parameter is the players list 
        2. The second parameter is the iternary variable 
        returns:
        1.It returns the itenary variable.
        '''
        print("self.previous_bet",self.previous_bet-players_list[z].player_bet_hand)
        if int(self.previous_bet-players_list[z].player_bet_hand) >= players_list[z].money:
            players_list[z].round_status="All_In"
           
            print("All_In detected")
            self.hand_pot=self.hand_pot+players_list[z].money
            self.round_pot=self.round_pot+players_list[z].money
            players_list[z].player_bet=players_list[z].player_bet+players_list[z].money
            players_list[z].player_bet_hand=players_list[z].player_bet_hand+players_list[z].money
            players_list[z].money=0
        
        else:
            print("In normal call")
            players_list[z].money=players_list[z].money-(self.previous_bet-players_list[z].player_bet_hand)
            self.hand_pot=self.hand_pot+(self.previous_bet-players_list[z].player_bet_hand)
            self.round_pot=self.round_pot+(self.previous_bet-players_list[z].player_bet_hand)
            players_list[z].player_bet=players_list[z].player_bet+(self.previous_bet-players_list[z].player_bet_hand)
            players_list[z].player_bet_hand=players_list[z].player_bet_hand+(self.previous_bet-players_list[z].player_bet_hand)
        
        
        print("Players after round status",players_list[z].round_status)
        print("This is player bet hand",players_list[z].player_bet_hand)
        print("Player",players_list[z].name, "has called and has amount",players_list[z].money)
        print("Current pot is",self.hand_pot)
        #print("this is player bet hand",players_list[z].player_bet_hand)
        z=(z+1)%len(players_list)
        #print("This is Z",z)
        print(players_list)
        return z
   
    def Raise(self,players_list,z,root):
      
        '''
        The Raise method of the Hand class reacts to when the player wants to Raise and sets their attributes accordingly.
        parameters:
        1. The first parameter is the players list 
        2. The second parameter is the itinerary variable 
        returns:
        1. It returns the itinerary variable.
        '''
        def cont():
            self.cont.set(1)
        while True:
            self.cont=tkinter.IntVar()
            raise_input_box=tkinter.Entry(root)
            raise_input_box.place(relx=0.7,rely=0.5,anchor="center")
            raise_button=tkinter.Button(root,text="Place Raise Amount",command=cont)
            raise_button.place(relx=0.9,rely=0.5,anchor="center")
            root.wait_variable(self.cont)
            raise_amount=raise_input_box.get()
            
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
        print("THis is player_bet_hand",players_list[z].player_bet_hand)
        self.hand_pot = self.hand_pot + (self.previous_bet - players_list[z].player_bet_hand) + int(raise_amount)
        self.round_pot = self.round_pot + (self.previous_bet-players_list[z].player_bet_hand)+int(raise_amount)
        print("Players_list[z].money before#############################",players_list[z].money)
        print("raise amount:",raise_amount,"self.previous_bet:",self.previous_bet,"players_list[z].player_bet_hand:",players_list[z].player_bet_hand)
        players_list[z].money = players_list[z].money -( (self.previous_bet-players_list[z].player_bet_hand)+int(raise_amount))
        print("This is the amount getting minused from player money",str((self.previous_bet-players_list[z].player_bet_hand)+int(raise_amount)))
        print("Players_list[z].money after",players_list[z].money)
        if players_list[z].money==0:
            print("All_In deteted*********************************************************************")
            players_list[z].round_status="All_In"

        players_list[z].player_bet_hand = players_list[z].player_bet_hand + (self.previous_bet-players_list[z].player_bet_hand)+int(raise_amount)
        self.previous_bet = self.previous_bet +int(raise_amount)

        print("Players after round status",players_list[z].round_status)
        print("Player", players_list[z].name, "has raised and has amount", players_list[z].money)
        print("Current pot is", self.hand_pot)
        z = (z + 1) % len(players_list)  
        return z
   
    def bet(self,players_list,z,root):
        '''
        The bet method of the Hand class reacts to when the player wants to bet and sets their attributes accordingly.
        parameters:
        1.The first parameter is the players list 
        2. The second parameter is the iternary variable 
        returns:
        1.It returns the itenary variable.
        '''
        
        while True:
            def cont():
                self.cont.set(1)
            self.cont=tkinter.IntVar()
            bet_input_box=tkinter.Entry(root)
            bet_input_box.place(relx=0.7,rely=0.5,anchor="center")
            bet_button=tkinter.Button(root,text="Place Bet Amount",command=cont)
            bet_button.place(relx=0.9,rely=0.5,anchor="center")
            root.wait_variable(self.cont)
            bet_amount=bet_input_box.get()
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
            self.round_pot=int(bet_amount)
            print("This is hand pot befre",self.hand_pot)
            self.hand_pot=self.hand_pot+int(bet_amount)

            players_list[z].money=players_list[z].money-int(bet_amount)

            if players_list[z].money==0:
                players_list[z].round_status="All_In"
                print("All_In detected")

            print("Player",players_list[z],"has bet amount",bet_amount)
            print("Current pot is",self.hand_pot)
            print("Players after round status",players_list[z].round_status)
            z=(z+1)%len(players_list)
            break
        return z
    
    def imput_options(self,players_list,z,root,test="NO"):
        '''
        The imput_options method of the Hand class, calculates what decision the player is able to make depending on certain criteria.
        parameters:
        1.The first parameter is the list of players.
        2.The second parameter is the iternary variable. 
        '''
        self.clicked=False
        def set_round_status(round_status,players_list,z):
            if self.clicked:
                pass
            else:
                players_list[z].round_status=round_status
                print("This is player round status",players_list[z].round_status)
                self.button_clicked.set(1)
                print("This is button clicked",self.button_clicked)
                #z=self.call(players_list,z)
                print("Ya arrah")
                self.clicked=True
        fold_button=tkinter.Button(root,text="Fold",command=lambda :set_round_status("Fold",players_list,z))
        fold_button.place(relx=0.5,rely=0.5,anchor="center")    
        #print("Player",players_list[z].name,"it is your turn")
        if self.round_pot>0 and players_list[z].player_bet_hand!=self.previous_bet:
            call_button=tkinter.Button(root,text="Call",command=lambda :set_round_status("Call",players_list,z))
            call_button.place(relx=0.3,rely=0.5,anchor="center")
                        
        print('round pot',self.round_pot)
        if self.round_pot >0:
            raise_button=tkinter.Button(root,text="Raise",command=lambda :set_round_status("Raise",players_list,z))
            raise_button.place(relx=0.4,rely=0.5,anchor="center")
        
        if self.round_pot==0:
            bet_button=tkinter.Button(root,text="Bet",command=lambda :set_round_status("Bet",players_list,z))
            bet_button.place(relx=0.4,rely=0.5,anchor="center")

            check_button=tkinter.Button(root,text="Check",command=lambda :set_round_status("Check",players_list,z))
            check_button.place(relx=0.3,rely=0.5,anchor="center")

        if players_list[z].player_bet_hand==self.previous_bet and players_list[z].round_status==None:
            check_button=tkinter.Button(root,text="Check",command=lambda :set_round_status("Check",players_list,z))
            check_button.place(relx=0.3,rely=0.5,anchor="center")

        if test=="NO":
            print("This is hand pot",self.hand_pot)
        print("Ya arrah 2")
        #players_list[z].round_status=input(f"Do you want to Fold {self.decision1} {self.decision2} {self.decision3} {self.decision4}  :")
        
    def round_check(self,players_list,root):
        '''The round_check of the Hand class, checks if the round is over or not and it checks if there is a winner through folding.
        parameters:
        1.The frst parameter is the list of players
        returns:
        1.It returns YES or NO, it returns YES, when the round should continue and NO when the round should end. '''
        print("In round check")
        self.stop_next_turn=False
        check="YES"
        check2="YES"    
        jst=list()
        mk=list()
        jaz=0
        stab="YES"
        cont="k"
        all_in_var=0
        for v in players_list:
            #print(v.round_status)
            if v.round_status=="Fold":
                jaz=jaz+1
                print(jaz)
                if jaz==len(players_list)-1:
                    for g in players_list:
                        if g.round_status!="Fold":
                            g.round_status="Won_hand"
                            g.money=g.money+self.hand_pot
                            print(g.name,"wins")
                            print(g.name,"has amount",g.money)
                            stab="NO" 
                            break
            

                                        
        for v in players_list:
            if stab=="NO":
                check="NO"
                cont="WON"
                for widgets in root.winfo_children():
                    widgets.destroy()
                return cont
            elif v.round_status==None:
                check="NO"
                break  
            elif v.round_status=="Fold":
                continue
            elif v.round_status=="All_In":
                print("In all in round check")
                continue
            jst.append(v.player_bet_hand)
            mk.append(v)

        if check=="YES":
            try:
                s1=jst[0]
            except:
                return "NO"
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
            print("This is hand pot",self.hand_pot)
            return cont
            
        else:
            cont="YES"
            return cont

    def round_betting(self,amount_cards,player_list,blinds,root):
        '''The round_betting class of the Hand class, implements the betting system for the Poker game.
        parameters:
            1. The first parameter is the amout of community cards needed to be dealt in the round
            2. The second parameter is the list of players
            3. The third parameter  takes an input of YES or NO, if YES is entered blind values are intialized, if NO is entered,there will be no blind values. '''
        print("This is self.hand_pot",self.hand_pot)
        for widgets in root.winfo_children():
            widgets.destroy()
     
        self.round_pot=0
        players_list=player_list.copy()
        self.community_cards_deal(amount_cards,players_list)
        z=self.blinds_check(blinds,players_list)
        stop_next_turn=False
        while z < len(players_list):
            for x in players_list:
                print(x.name,"round status :",x.round_status)
            j=0 
            for x in players_list:
                if x.round_status=="All_In":
                    j=j+1
                elif x.round_status=="Fold":
                    j=j+1
            if j==len(players_list):
                break
            if j==len(players_list)-1:
                stop_next_turn=True
            print("j   ::   ",j)
            
            if players_list[z].round_status=="Fold":
                #print("This is fold z",z)
                
                z=(z+1)%len(players_list)
                continue
            elif players_list[z].round_status=="All_In":
                
                print("All_In continue")
                z=(z+1)%len(players_list)
                continue

            if stop_next_turn:
                break
           
            
           
                
            for widgets in root.winfo_children():
                widgets.destroy()
            self.cont=tkinter.IntVar()
            show_player_stats=tkinter.Text(root,height=3,width=30,yscrollcommand=True,xscrollcommand=True)
            show_player_stats.place(relx=0.905,rely=0.8,anchor="center")
            player_money="Money "+str(players_list[z].money)+"\n"
            show_player_stats.insert(tkinter.END,player_money)
            player_bet_hand="Amount bet this round "+str(players_list[z].player_bet_hand)+"\n"
            show_player_stats.insert(tkinter.END,player_bet_hand)
            player_bet="Amount bet in total "+str(players_list[z].player_bet)+"\n"
            show_player_stats.insert(tkinter.END,player_bet)
            show_player_stats.config(state=("disabled"))
            
                
#----------------------------------------------------------------------------------------------------
            player_tell_label=tkinter.Label(root,font=("Times 21"))
            player_tell_label.place(relx=0.3,rely=0.1,anchor="center")
            player_tell_label["text"]="Player "+players_list[z].name+" it is your turn"

            player_your_cards_label=tkinter.Label(root,text="Your cards",font=("Times 14"))
            player_your_cards_label.place(relx=0.5,rely=0.6,anchor="center")
            
            card_one_image=tkinter.Button(root,command=lambda :show_card_one(players_list,z,card_one_image,card_two_image))
            k=Image.open("PNG-cards-1.3/b.png")
            image=k.resize((150,250))
            img_to_add=ImageTk.PhotoImage(image)
            card_one_image["image"]=img_to_add
            card_one_image.place(relx=0.4,rely=0.8,anchor="center")
           

            card_two_image=tkinter.Button(root,command=lambda :show_card_one(players_list,z,card_one_image,card_two_image))
            card_two_image.place(relx=0.6,rely=0.8,anchor="center")
            k2=Image.open("PNG-cards-1.3/b.png")
            image2=k2.resize((150,250))
            img_to_add2=ImageTk.PhotoImage(image2)
            card_two_image["image"]=img_to_add2
            self.card_open=False
            

            def show_card_one(players_list,z,card_one_image,card_two_image):
                if self.card_open:
                    k=Image.open("PNG-cards-1.3/b.png")
                    image=k.resize((150,250))
                    self.img=ImageTk.PhotoImage(image)
                    card_one_image["image"]=self.img
                    self.img2=ImageTk.PhotoImage(image)
                    card_two_image["image"]=self.img2
                    self.card_open=False
                else:
                    card_one_number=players_list[z].card_one.number
                    card_one_suit=players_list[z].card_one.suit

                    new_card_one_number=card_one_number.lower()
                    new_card_one_suit=card_one_suit.lower()

                    image_to_open=f"{new_card_one_number}_of_{new_card_one_suit}.png"
                
                    td=Image.open('PNG-cards-1.3/'+image_to_open)
                    image=td.resize((150,250))
                    self.img=ImageTk.PhotoImage(image)
    
                    card_one_image["image"]=self.img

                    card_two_number=players_list[z].card_two.number
                    card_two_suit=players_list[z].card_two.suit

                    new_card_two_number=card_two_number.lower()
                    new_card_two_suit=card_two_suit.lower()

                    image_to_open2=f"{new_card_two_number}_of_{new_card_two_suit}.png"
                    
                    td2=Image.open('PNG-cards-1.3/'+image_to_open2)
                    image2=td2.resize((150,250))

                    self.img2=ImageTk.PhotoImage(image2)
                    card_two_image["image"]=self.img2
                    self.card_open=True
            
            def show_card_two(players_list,z,card_two_image):
                if self.card_open:
                    k=Image.open("PNG-cards-1.3/b.png")
                    image=k.resize((150,250))
                    self.img2=ImageTk.PhotoImage(image)
                    card_two_image["image"]=self.img2
                    self.card_two_open=False
                else:
                    card_two_number=players_list[z].card_two.number
                    card_two_suit=players_list[z].card_two.suit

                    new_card_two_number=card_two_number.lower()
                    new_card_two_suit=card_two_suit.lower()

                    image_to_open2=f"{new_card_two_number}_of_{new_card_two_suit}.png"
                    
                    td2=Image.open('PNG-cards-1.3/'+image_to_open2)
                    image2=td2.resize((150,250))

                    self.img2=ImageTk.PhotoImage(image2)

                    card_two_image["image"]=self.img2
                    self.card_open=True
#--------------------------------------------------------------------------------------------------
            
            
            show_players_bet=tkinter.Text(root,height=3,width=40,yscrollcommand=True,xscrollcommand=True)
            show_players_bet.config(state=("disabled"))
            show_players_bet.place(relx=0.7,rely=0.1,anchor="center")
            print(self.previous_bet)
            amount_needed_to_match=tkinter.Label(root,font=("Times 13"))
            amount_needed_to_match["text"]="You need to bet at least amount   "+str(self.previous_bet-players_list[z].player_bet_hand)
            amount_needed_to_match.place(relx=0.15,rely=0.8,anchor="center")

            current_pot_label=tkinter.Label(root,font=("Times 13"))
            current_pot_label["text"]="Current pot is "+str(self.hand_pot)
            current_pot_label.place(relx=0.15,rely=0.7,anchor="center")
            try_next_card=True
            #print(self.community_cards)

            def set_image_to_card(card):
                #print('This is card ',card)
                community_card_number=self.community_cards[card].number
                #print("This is community_card_number",community_card_number)

                community_card_suit=self.community_cards[card].suit
                #print("This is community_card_suit",community_card_suit)
                #print("check")
                new_community_card_number=community_card_number.lower()
                new_community_card_suit=community_card_suit.lower()
                #print("check2")

                image_to_open=f"{new_community_card_number}_of_{new_community_card_suit}.png"
                #print("This is image to open",image_to_open)
                return image_to_open
            
            try:
                rt=set_image_to_card(0)
                community_card_one_image=tkinter.Label(root)
                community_card_one_image.place(relx=0.1,rely=0.3,anchor="center")
                td3=Image.open('PNG-cards-1.3/'+rt)
                image3=td3.resize((150,250))
                img3=ImageTk.PhotoImage(image3)
                community_card_one_image["image"]=img3
            except IndexError:
                print("There is an error")
                try_next_card=False

            if try_next_card:
                try:
                    rt2=set_image_to_card(1)
                    community_card_two_image=tkinter.Label(root)
                    community_card_two_image.place(relx=0.3,rely=0.3,anchor="center")
                    print("rt2",rt2)
                    td4=Image.open('PNG-cards-1.3/'+rt2)
                    image4=td4.resize((150,250))
                    img4=ImageTk.PhotoImage(image4)
                    community_card_two_image["image"]=img4
                   
                except IndexError:
                    try_next_card=False

            if try_next_card:
                try:
                    rt3=set_image_to_card(2)
                    community_card_three_image=tkinter.Label(root)
                    community_card_three_image.place(relx=0.5,rely=0.3,anchor="center")
                    td5=Image.open('PNG-cards-1.3/'+rt3)
                    image5=td5.resize((150,250))
                    img5=ImageTk.PhotoImage(image5)
                    community_card_three_image["image"]=img5
                except IndexError:
                    try_next_card=False
                
            if try_next_card:
                try:
                    rt4=set_image_to_card(3)
                    community_card_four_image=tkinter.Label(root)
                    community_card_four_image.place(relx=0.7,rely=0.3,anchor="center")
                    td6=Image.open('PNG-cards-1.3/'+rt4)
                    image6=td6.resize((150,250))
                    img6=ImageTk.PhotoImage(image6)
                    community_card_four_image["image"]=img6
                except IndexError:
                    try_next_card=False
            
            if try_next_card:
                try:
                    rt5=set_image_to_card(4)
                    community_card_five_image=tkinter.Label(root)
                    community_card_five_image.place(relx=0.9,rely=0.3,anchor="center")
                    td7=Image.open('PNG-cards-1.3/'+rt5)
                    image7=td7.resize((150,250))
                    img7=ImageTk.PhotoImage(image7)
                    community_card_five_image["image"]=img7
                except IndexError:
                    try_next_card=False



            print("This is players_list",players_list)
            for x in self.players_list:
                if x.round_status=="Fold":
                    add_thing="Player "+x.name+" has folded \n"
                    show_players_bet.config(state=("normal"))
                    show_players_bet.insert(tkinter.END,add_thing)
                    show_players_bet.config(state=("disabled"))
                else:
                    add_thing="Player "+x.name+" has bet amount "+str(x.player_bet)+"\n"
                    show_players_bet.config(state=("normal"))
                    show_players_bet.insert(tkinter.END,add_thing)
                    show_players_bet.config(state=("disabled"))

            self.button_clicked=tkinter.IntVar()
            self.imput_options(players_list,z,root)
            print("out of imput_options")
            def on_closing():
                print("Root window is closing...")
                self.button_clicked.set(1)
                self.cont.set(1)
                root.destroy()  
                
            root.protocol("WM_DELETE_WINDOW", on_closing)
            root.wait_variable(self.button_clicked)

                
            

            print("This is players round status",players_list[z].round_status)

            if  players_list[z].round_status=="Call":
                print("In Call")
                z=self.call(players_list,z,root)
            elif players_list[z].round_status=="Raise":
                z=self.Raise(players_list,z,root)
            elif players_list[z].round_status=="Bet":
                z=self.bet(players_list,z,root)
            elif players_list[z].round_status=="Fold":
                self.players_in_game.remove(players_list[z])
                z=(z+1)%len(players_list)
            elif players_list[z].round_status=="Check":
                z=(z+1)%len(players_list)
            else:
                break
            for x in players_list:
                print("Name:",x.name,"Card 1",x.card_one.number,x.card_one.suit,"Card 2",x.card_two.number,x.card_two.suit)     
            cont=self.round_check(players_list,root)
            print(cont)
            if cont=="YES":
                continue
            elif cont=="NO":
                break
            elif cont=="WON":
                return "NO_NEW_ROUND"
            
            root.mainloop()

           
#---------------------------------------------------------------------------------------------------------------------------------------        
#---------------------------------------------------------------------------------------------------------------------------------
    def check_flush(self,p):       
        '''The check_flush method of the hand class will check if a flush is present in a Poker hand
        parameters:
            1.The first parameter is the player object 
        returns:
            1. True or False depending if the hand is present 
            2. Either the point value of how strong the hand is or None if the hand isn't there'''
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
        utility=Utility()
        if suit_count["Clubs"][0]>=5:
            #print("This is suit_count lenght",len(suit_count["Clubs"][1]))
            suit_count["Clubs"][1].sort(reverse=True)
            dec_val=utility.calculate_decimal_points(suit_count["Clubs"][1][0:5])
            return True,suit_count["Clubs"][1][0:5],dec_val,suit_count["Clubs"][1]

        elif suit_count["Hearts"][0]>=5:
            suit_count["Hearts"][1].sort(reverse=True)
            dec_val=utility.calculate_decimal_points(suit_count["Hearts"][1][0:5])
            return True,suit_count["Hearts"][1][0:5],dec_val,suit_count["Hearts"][1]
                 
        elif suit_count["Diamonds"][0]>=5:
            suit_count["Diamonds"][1].sort(reverse=True)
            dec_val=utility.calculate_decimal_points(suit_count["Diamonds"][1][0:5])
            return True,suit_count["Diamonds"][1][0:5],dec_val,suit_count["Diamonds"][1]
            
        elif suit_count["Spades"][0]>=5:
            suit_count["Spades"][1].sort(reverse=True)
            dec_val=utility.calculate_decimal_points(suit_count["Spades"][1][0:5])
            return True,suit_count["Spades"][1][0:5],dec_val,suit_count["Spades"][1]
        else:
            return False,None,None,None
    
    def check_straight(self,p,cards):
        '''The check_straight method of the hand class will check if a straight is present in a Poker hand
        parameters:
            1.The first parameter is the player object 
            2. The second parameter is the cards
        returns:
            1. True or False depending if the hand is present 
            2. Either thr point value of how strong the hand is or None if the hand isn't there'''
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
            print("This is f[x]",f[x],"This is f[x+1]",f[x+1])
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
                utility=Utility()
                dec_points=utility.calculate_decimal_points(lst)
                #j=False
                return True,dec_points
            else:
                x=x+1
                print("THIS IS X",x)
       
        return False,None

         
        #print("This is f lenght",len(f))
        #print("This is f",f)
       
    def check_straight_flush(self,p):  
        '''The check_straight_flush method of the hand class will check if a straight flush  is present in a Poker hand
        parameters:
            1.The first parameter is the player object 
        returns:
            1. True or False depending if the hand is present 
            2. Either thr point value of how strong the hand is or None if the hand isn't there'''
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
        '''The four_of_a_kind method of the hand class will check if a four of a kind is present in a Poker hand
        parameters:
            1.The first parameter is the player object 
            2. The second parameter is the cards
        returns:
            1. True or False depending if the hand is present 
            2. Either thr point value of how strong the hand is or None if the hand isn't there'''
        utility=Utility()
        ret=utility.pairs_method(cards,4,True)
        print("tHIS IS RET[1]",ret[1])
        if ret[1]==None:
            return False,None
        soup=utility.calculate_decimal_points(ret[1])
        return ret[0],soup

    def three_of_a_kind(self,p,cards):
        '''The three_of_a_kind method of the hand class will check if a three of a kind is present in a Poker hand
        parameters:
            1.The first parameter is the player object 
            2. The second parameter is the cards
        returns:
            1. True or False depending if the hand is present 
            2. Either thr point value of how strong the hand is or None if the hand isn't there'''
        utility=Utility()
        ret=utility.pairs_method(cards,3,True)
        if ret[1]==None:
            return False,None
        soup=utility.calculate_decimal_points(ret[1])
        return ret[0],soup
    
    def pair(self,p,cards):
        '''pair method of the hand class will check if a pair is present in a Poker hand
        parameters:
            1.The first parameter is the player object 
            2. The second parameter is the cards
        returns:
            1. True or False depending if the hand is present 
            2. Either thr point value of how strong the hand is or None if the hand isn't there'''
        utility=Utility()
        ret=utility.pairs_method(cards,2,True)
        if ret[1]==None:
            return False,None
        soup=utility.calculate_decimal_points(ret[1])
        return ret[0],soup

    def two_pair(self,p,cards):
        '''The two_pair method of the hand class will check if a two pair is present in a Poker hand
        parameters:
            1.The first parameter is the player object 
            2. The second parameter is the cards
        returns:
            1. True or False depending if the hand is present 
            2. Either thr point value of how strong the hand is or None if the hand isn't there'''
        utility=Utility()
        ret=utility.multiple_pairs_method(cards,2)
        if ret[1]==None:
            return False,None
        soup=utility.calculate_decimal_points(ret[1])
        return ret[0],soup
    
    def full_house(self,p,cards):
        '''The full_house method of the hand class will check if a full house is present in a Poker hand
        parameters:
            1.The first parameter is the player object 
            2. The second parameter is the cards
        returns:
            1. True or False depending if the hand is present 
            2. Either thr point value of how strong the hand is or None if the hand isn't there'''
        utility=Utility()
        ret=utility.multiple_pairs_method(cards,3)
        if ret[1]==None:
            return False,None
        soup=utility.calculate_decimal_points(ret[1])
        return ret[0],soup

    def high_card(self,p,cards):
        '''The high_card method of the hand class will calculate a point value for the high card in a Poker hand
        parameters:
            1.The first parameter is the player object 
            2. The second parameter is the cards
        returns:
            1. returns the point value for the high card for a hand'''
        new_cards=cards[0:5]
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
    def player_grade(self,info,root,test=False):
        '''The player_grade function of the hand class identifies the winner/winners of a Poker hand based on the value of their hand and allocate the money to them accordingly
        parameters:
                1. A list of the value of a player's hand and the player object.
                2. This is an optional parameter that should be made True when one is testing the function.  '''
        new_list=sorted(info,key=itemgetter(0),reverse=True)
        sorted_list=list()
        previous_bet=0
        cnt=0
        list1=[new_list[0][1]]
        item = new_list[0]
        list_of_players=list()
        
        list_of_players = [x[1] for x in new_list] 
        # for x in new_list:
        #     list_of_players.append(x[1])
        print("This is list of players",list_of_players)
        player_money_display=tkinter.Text(root,height=8,width=50,yscrollcommand=True,xscrollcommand=True)
        player_money_display.place(relx=0.5,rely=0.3,anchor="center")
        player_money_display.config(state=("disabled"))

        title_label=tkinter.Label(root,text="Winner(s) and Loser(s)",font=("Times 21"))
        title_label.place(relx=0.5,rely=0.1,anchor="center")

        for p in new_list:
            
            print("This is item[0]",item[0],"This is p[0]",p[0])
            if item == p:
                continue
            if item[0]==p[0]:
                print("This is list1 in ties",list1)
                list1.append(p[1])
                #list_of_players.append(p[1])

            else:
                print("tis list 1",list1)
                list1.sort(key=lambda x:x.player_bet)
                #final_list=sorted(list1,key=lambda x:x.player_bet)
                sorted_list.append(list1)
                list1=list()
                list1.append(p[1])
                #list_of_players.append(p[1])
                
        print("list1 after",list1)
        if len(list1)>0:
            list1.sort(key=lambda x:x.player_bet)
            #final_list=sorted(list1,key=lambda x:x.player_bet)
            sorted_list.append(list1)
            list1=list()
            
        print("sorted_list",sorted_list)
        print("This is list of player",list_of_players)

        
        winner_list=list()
        rts_val=list()
        
        for big_list in sorted_list:
            
            player=0
            split_amount=len(big_list)
            print("This is big_list",big_list)
            for ties in big_list:
                amount=self.hand_pot
                for g in list_of_players:
                    val = g.player_bet-ties.player_bet
                    print("This is g.player_bet",g.player_bet,"This is ties.player_bet",ties.player_bet)
                    print("This is val",val)
                    if val < 0:
                        val=0
                    amount = amount - val
                print("Tis amount eligle",amount)
                self.hand_pot=self.hand_pot-(amount/split_amount)
                print('This i s pot',self.hand_pot)
                print("Tis amount won",amount/split_amount)
                big_list[player].money=big_list[player].money+(amount/split_amount)
                rts_val.append(big_list[player].money)
                print("This is rts_val",rts_val)
                print("This is split_amount",split_amount)
                #big_list.remove(ties)
                print("This is big_list",big_list)
                winner_info=ties.name+" has won amount "+str(amount/split_amount) +" and has amount "+str(ties.money)+"\n"
                player_money_display.config(state=("normal"))
                player_money_display.insert(tkinter.END,winner_info)
                player_money_display.config(state=("disabled"))
                winner_list.append(ties)
                split_amount=split_amount-1
                player=player+1
                print("This is player",player)
                
            if self.hand_pot==0:
                if test:
                    return rts_val
                else:
                    player_money_display.config(state=("normal"))
                    player_money_display.insert(tkinter.END,"-------------------------------------------------- \n")
                    player_money_display.config(state=("disabled"))
                    for p in self.players_list:
                        if p in winner_list:
                            continue 
                        else:
                            loser_info=p.name+" has lost and has amount "+str(p.money)+"\n"
                            player_money_display.config(state=("normal"))
                            player_money_display.insert(tkinter.END,loser_info)
                            player_money_display.config(state=("disabled"))
                    break
            else:
                print('In continue')
                continue
                            
    def check_winner(self,players_list,root):
        '''The check_winner function of the hand class looks for the winner/winners of a Poker hand and allocates their money won accordingly
            parameters:
            1. the list of players in the game 
            '''
        for widgets in root.winfo_children():
            widgets.destroy()
        points_list=list()
        print(len(players_list))
        for p in players_list:
            list_cards=list()
            cards=self.community_cards.copy()
            cards.append(p.card_one)
            cards.append(p.card_two)
            for c in cards:
                list_cards.append(c.number_value)
            list_cards.sort(reverse=True)
            
            val=self.check_straight_flush(p)
            if val[0]==True:
                point_value=9+val[1]
                points_list.append([point_value,p])
                p.point_val=point_value
                continue
                
               #return "STRAIGHT_FLUSH"
            elif val[0]==False:
                val=self.four_of_a_kind(p,list_cards)
            
            if val[0]==True:
                point_value=8+val[1]
                points_list.append([point_value,p])
                p.point_val=point_value
                continue
                #return "FOUR_OF_A_KIND"
            elif val[0]==False:
                val=self.full_house(p,list_cards)

            if val[0]==True:
                point_value=7+val[1]
                points_list.append([point_value,p])
                p.point_val=point_value
                continue
                #return "FULL_HOUSE"
            elif val[0]==False:
                val=self.check_flush(p)
            
            if val[0]==True:
                point_value=6+val[2]
                points_list.append([point_value,p])
                p.point_val=point_value
                continue
                #return "FLUSH"
            elif val[0]==False:
                val=self.check_straight(p,list_cards)
           
            if val[0]==True:
                point_value=5+val[1]
                points_list.append([point_value,p])
                p.point_val=point_value
                continue
                #return "STRAIGHT"
            elif val[0]==False:
                val=self.three_of_a_kind(p,list_cards)

            if val[0]==True:
                point_value=4+val[1]
                points_list.append([point_value,p])
                p.point_val=point_value
                continue
                #return "THREE_OF_A_KIND"
            elif val[0]==False:
                val=self.two_pair(p,list_cards)

            if val[0]==True:
                point_value=3+val[1]
                points_list.append([point_value,p])
                p.point_val=point_value
                continue
                #return "TWO_PAIR"
            elif val[0]==False:
                val=self.pair(p,list_cards)
            
            if val[0]==True:
                point_value=2+val[1]
                points_list.append([point_value,p])
                p.point_val=point_value
                continue
                #return "PAIR"
            elif val[0]==False:
                high_card_value=self.high_card(p,list_cards)
                points_list.append([high_card_value,p])
                p.point_val=high_card_value
                #return "HIGH_CARD"
        self.player_grade(points_list,root)
            
    def preflop(self,root):
        '''The preflop method of the Hand class implemets betting for the preflop round'''
        self.new_round=self.round_betting(0,self.players_list,"YES",root)    
    
    def flop(self,root):
        '''The flop method of the Hand class implements betting for the flop round'''
        if self.new_round != "NO_NEW_ROUND":
            self.new_round=self.round_betting(3,self.players_in_game,"NO",root)
    
    def turn(self,root):
        '''The turn method of the Hand class implements betting for the turn round'''
        if self.new_round != "NO_NEW_ROUND":
           self.new_round= self.round_betting(1,self.players_in_game,"NO",root)   
    
    def river(self,root):
        '''The river method of the Hand class implements betting for the river round'''
        if self.new_round != "NO_NEW_ROUND":
            self.new_round=self.round_betting(1,self.players_in_game,"NO",root)   
            if self.new_round !="NOw_NEW_ROUND":
                self.check_winner(self.players_in_game,root=root)
               
    