import tkinter
from player import Player
from game import Game


root=tkinter.Tk()
root.title("Poker Game")
root.geometry("800x800")
root.configure(bg="green")
title=tkinter.Label(root,text="Welcome to Poker Game")
title.place(relx=0.5,rely=0.1,anchor="center")
players_list=list()

show_players=tkinter.Text(root,height=5,width=40,yscrollcommand=True,xscrollcommand=True)
show_players.config(state=("disabled"))
show_players.place(relx=0.5,rely=0.25,anchor="center")

informer_label=tkinter.Label(root,text="Please enter player name to add")
informer_label.place(relx=0.5,rely=0.4,anchor="center")

imput=tkinter.Entry(root)
imput.place(relx=0.5,rely=0.5,anchor="center")

def add_player():
    new_player=Player()
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
        

def start_the_game():
    if len(players_list)<2:
        informer_label["text"]="Please add at least two players before starting"
    else:
        informer_label["text"]="Game starting"
        game=Game(players_list)
        game.other_rounds(root)
        
        
add_players_button=tkinter.Button(root,text="Add Player",command=add_player)
add_players_button.place(relx=0.5,rely=0.6,anchor="center")



start_the_game=tkinter.Button(root,text="Start Game",command=start_the_game)
start_the_game.place(relx=0.5,rely=0.7,anchor="center")


root.mainloop()