from hand import Hand
import random 
from deck import Deck
from player import Player
import tkinter
class Game():
    def __init__ (self,player_list):
        self.player_list=player_list
               
    def remove_player_out_of_game(self,player_list):
        for p in player_list:
            if p.money<=0:
                player_list.remove(p)
                print("Player",p.name,"has been removed from the game due to a lack of funds")
                
        return player_list
        
    def cash_out(self,player_list,root,show_players):
        if self.clicked:
            pass
        if self.clicked2:
            pass
        else:
            self.clicked=True
            def remove_player(player_remove,teller_label,player_remove_button,show_players):
                player_to_remove=player_remove.get()
                set_value=False
                for p in player_list:
                    if p.name==player_to_remove:
                        set_value=True
                        player_list.remove(p)
                        player_removed=p
                        break 
                if set_value==False:
                    teller_label["text"]="Please enter a valid name to cash out"
                    player_remove.delete(0,"end")
                elif set_value==True:
                    player_remove.destroy()
                    teller_label.destroy()
                    player_remove_button.destroy()
                    print(self.player_list)
                    self.clicked=False
                    show_players.config(state=("normal"))
                    show_players.delete(1.0,"end")
                    show_players.config(state=("disabled"))
                    for x in player_list:
                        add_thing="Player "+x.name+" has amount "+str(x.money)+"\n"
                        show_players.config(state=("normal"))
                        show_players.insert(tkinter.END,add_thing)
                        show_players.config(state=("disabled"))
        
            teller_label=tkinter.Label(root,text="Please enter player name to cash out")
            teller_label.place(relx=0.7,rely=0.7,anchor="center")
            
            player_remove=tkinter.Entry(root)
            player_remove.place(relx=0.7,rely=0.8,anchor="center")

            player_remove_button=tkinter.Button(root,text="cash out player",command=lambda:remove_player(player_remove,teller_label,player_remove_button,show_players))
            player_remove_button.place(relx=0.7,rely=0.9,anchor="center")
            self.clicked=True

    def cash_in(self,player_list,root,show_players):
        if self.clicked:
            pass
        elif self.clicked2:
            pass
        else:
            self.clicked2=True
            def add_player(player_add,informer_label,player_add_button,show_players):
                new_name=player_add.get().strip()
                if len(new_name)<1:
                    informer_label["text"]="Please enter a valid name to add"
                    player_add.delete(0,"end")
                else:
                    if new_name in [player.name for player in player_list]:
                        informer_label["text"]="Please enter a unique name to add"
                        player_add.delete(0,"end")
                    else:
                        if len(new_name)>12:
                            informer_label["text"]="Please enter a name below 12 charachters"
                            player_add.delete(0,"end")
                        else:
                            new_player=Player()
                            player_list.append(new_player)
                            new_player.name=player_add.get()
                            #print('This is imput',len(imput.get()))
                            player_add.destroy()
                            informer_label.destroy()
                            player_add_button.destroy()
                            self.clicked2=False
                            print(player_list)
                            show_players.config(state=("normal"))
                            show_players.delete(1.0,"end")
                            show_players.config(state=("disabled"))
                            for x in self.player_list:
                                add_thing="Player "+x.name+" has amount "+str(x.money)+"\n"
                                show_players.config(state=("normal"))
                                show_players.insert(tkinter.END,add_thing)
                                show_players.config(state=("disabled"))

            informer_label=tkinter.Label(root,text="Please enter player name to cash in")
            informer_label.place(relx=0.3,rely=0.7,anchor="center")
            
            player_add=tkinter.Entry(root)
            player_add.place(relx=0.3,rely=0.8,anchor="center")

            player_add_button=tkinter.Button(root,text="cash in player",command=lambda:add_player(player_add,informer_label,player_add_button,show_players))
            player_add_button.place(relx=0.3,rely=0.9,anchor="center")

    def other_rounds(self,root):
        self.small_blind_index=random.randint(0,len(self.player_list)-1)
        self.player_list.insert(0,self.player_list.pop(self.small_blind_index))
        deck=Deck()
        deck.shuffle()
        self.deck=deck.deal(len(self.player_list),self.player_list)

        hand=Hand(self.player_list,self.deck,self.small_blind_index)
        
        hand.preflop(root)
        hand.flop(root)
        hand.turn(root)
        hand.river(root)
        self.cont=tkinter.IntVar()
        def cont():
            self.cont.set(1)

        next_button=tkinter.Button(root,text="next",command=cont)
        next_button.place(relx=0.5,rely=0.8,anchor="center")
       
        
        root.wait_variable(self.cont)
        for widgets in root.winfo_children():
            widgets.destroy()
        self.clicked=False
        self.clicked2=False
        print(self.clicked2)
        show_label=tkinter.Label(root,text="Player Cash-In,Cash-Out",font=("Times 15"))
        show_label.place(relx=0.5,rely=0.1,anchor="center")


        show_players=tkinter.Text(root,height=5,width=40,yscrollcommand=True,xscrollcommand=True)
        show_players.place(relx=0.5,rely=0.3,anchor="center")
        show_players.config(state=("disabled"))


        for x in self.player_list:
            
            add_thing="Player "+x.name+" has amount "+str(x.money)+"\n"
            show_players.config(state=("normal"))
            show_players.insert(tkinter.END,add_thing)
            show_players.config(state=("disabled"))

        cash_out_button=tkinter.Button(root,text="Cash Out",command= lambda :self.cash_out(self.player_list,root,show_players))
        cash_out_button.place(relx=0.7,rely=0.5,anchor="center")

        cash_in_button=tkinter.Button(root,text="Cash In",command= lambda :self.cash_in(self.player_list,root,show_players))
        cash_in_button.place(relx=0.3,rely=0.5,anchor="center")
        
        self.cont2=tkinter.IntVar()
        def cont2():
            if self.clicked:
                pass
            elif self.clicked2:
                pass
            else:
                self.cont2.set(1)

        next_button2=tkinter.Button(root,text="next",command=cont2)
        next_button2.place(relx=0.5,rely=0.8,anchor="center")

        root.wait_variable(self.cont2)
        for x in self.player_list:
            x.player_bet=0
            x.player_bet_hand=0
            x.round_status=None
            x.card_one=None
            x.card_two=None
        
        for widgets in root.winfo_children():
            widgets.destroy()
        self.player_list=self.remove_player_out_of_game(self.player_list)

        print(len(self.player_list))
        number=1
        while len(self.player_list)>1:
            number=number+1
            print("In Round number",number)
            for p in self.player_list:
                p.player_bet=0
            self.player_list=self.remove_player_out_of_game(self.player_list)
             
            self.small_blind_index=(self.small_blind_index+1)%len(self.player_list)
            print("small blind index",self.small_blind_index)
            self.player_list.insert(0,self.player_list.pop(self.small_blind_index))
            
            deck=Deck()
            deck.shuffle()
            

            self.deck=deck.deal(len(self.player_list),self.player_list)

            hand=Hand(self.player_list,self.deck,self.small_blind_index)

            hand.preflop(root)
            hand.flop(root)
            hand.turn(root)
            hand.river(root)
            self.cont=tkinter.IntVar()
            def cont():
                self.cont.set(1)

            next_button=tkinter.Button(root,text="next",command=cont)
            next_button.place(relx=0.5,rely=0.8,anchor="center")
        
            
            root.wait_variable(self.cont)
            for widgets in root.winfo_children():
                widgets.destroy()
            
            self.clicked=False
            self.clicked2=False
            print(self.clicked2)

            show_label=tkinter.Label(root,text="Player Cash-In,Cash-Out",font=("Times 15"))
            show_label.place(relx=0.5,rely=0.1,anchor="center")


            show_players=tkinter.Text(root,height=5,width=40,yscrollcommand=True,xscrollcommand=True)
            show_players.place(relx=0.5,rely=0.3,anchor="center")
            show_players.config(state=("disabled"))


            for x in self.player_list:
                
                add_thing="Player "+x.name+" has amount "+str(x.money)+"\n"
                show_players.config(state=("normal"))
                show_players.insert(tkinter.END,add_thing)
                show_players.config(state=("disabled"))

            cash_out_button=tkinter.Button(root,text="Cash Out",command= lambda :self.cash_out(self.player_list,root,show_players))
            cash_out_button.place(relx=0.7,rely=0.5,anchor="center")

            cash_in_button=tkinter.Button(root,text="Cash In",command= lambda :self.cash_in(self.player_list,root,show_players))
            cash_in_button.place(relx=0.3,rely=0.5,anchor="center")
            
            for x in self.player_list:
                x.player_bet=0
                x.player_bet_hand=0
                x.round_status=None
                x.card_one=None
                x.card_two=None
            if len(self.player_list)==1:
                break
        
        print("Game Over")
        print("Player",player_list[0].name,"is the winner")
    
    



        

