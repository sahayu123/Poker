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
        
    def cash_out(self,player_list,root):
        def remove_player(player_remove,teller_label,player_remove_button):
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
            elif set_value==True:
                player_remove.destroy()
                teller_label.destroy()
                player_remove_button.destroy()
                print(self.player_list)
        try:
            teller_label.destroy()
            player_remove.destroy()
            player_remove_button.destroy()
        except:
            pass
        teller_label=tkinter.Label(root,text="Please enter player name to cash out")
        teller_label.place(relx=0.6,rely=0.7,anchor="center")
        
        player_remove=tkinter.Entry(root)
        player_remove.place(relx=0.6,rely=0.8,anchor="center")

        player_remove_button=tkinter.Button(root,text="cash out player",command=lambda:remove_player(player_remove,teller_label,player_remove_button))
        player_remove_button.place(relx=0.6,rely=0.9,anchor="center")

       
    def cash_in(self,player_list,root):
       
        new_player=Player()
        def add_player()
        new_name=imput.get().strip()
        if len(new_name)<1:
            informer_label["text"]="Please enter a valid name to add"
            imput.delete(0,"end")
        else:
            if new_name in [player.name for player in players_list]:
                informer_label["text"]="Please enter a unique name to add"
                imput.delete(0,"end")
            else:
                if len(new_name)>12:
                    informer_label["text"]="Please enter a name below 12 charachters"
                    imput.delete(0,"end")
                else:
                    players_list.append(new_player)
                    new_player.name=imput.get()
                    print('This is imput',len(imput.get()))
                    show_players.config(state=("normal"))
                    add_thing="Player "+new_player.name+" has joined the game \n"
                    show_players.insert(tkinter.END,add_thing)
                    show_players.config(state=("disabled"))
                    imput.delete(0,"end")
      
    def other_rounds(self,root):
        self.small_blind_index=random.randint(0,len(self.player_list)-1)
       
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

        cash_out_button=tkinter.Button(root,text="Cash Out",command= lambda :self.cash_out(self.player_list,root))
        cash_out_button.place(relx=0.6,rely=0.5,anchor="center")

        cash_in_button=tkinter.Button(root,text="Cash In",command= lambda :self.cash_in(self.player_list,root))
        cash_in_button.place(relx=0.4,rely=0.5,anchor="center")
        
        self.cont=tkinter.IntVar()
        next_button=tkinter.Button(root,text="next",command=cont)
        next_button.place(relx=0.5,rely=0.8,anchor="center")

        root.wait_variable(self.cont)
        for widgets in root.winfo_children():
            widgets.destroy()

        while len(self.player_list)>1:
            for p in self.player_list:
                p.player_bet=0
            self.player_list=self.remove_player_out_of_game(self.player_list)
             
            self.small_blind_index=(self.small_blind_index+1)%len(self.player_list)
            
            deck=Deck()
            deck.shuffle()
            

            self.deck=deck.deal(len(self.player_list),self.player_list)

            hand=Hand(self.player_list,self.deck,self.small_blind_index)

            hand.preflop(root)
            hand.flop(root)
            hand.turn(root)
            hand.river(root)

        
        print("Game Over")
        print("Player",player_list[0].name,"is the winner")
    
    



        

