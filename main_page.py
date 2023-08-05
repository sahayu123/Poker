from game import Game
from player import Player
import tkinter
small_blind=Player()
small_blind.name="p1"
big_blind=Player()
big_blind.name="p2"
dealer=Player()
dealer.name="p3"
player_list=list()
player_list.append(small_blind)
player_list.append(big_blind)
player_list.append(dealer)
game=Game(player_list)
root=tkinter.Tk()
root.title("Poker Game")
root.geometry("800x800")
root.configure(bg="green")
game.other_rounds(root)







    
    

  


