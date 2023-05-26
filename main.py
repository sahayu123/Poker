import random
while True:
    people_amount=input("Enter Amount of People Playing: ")
    try:
        people_amount=int(people_amount)
    except:
        print("Please input an integer")
        continue
    if people_amount<2:
        print("Must Be at Least 2 people")
        continue
    break
print(people_amount)
knowledge=["asd","asdas"]
m=list()
h=1
knowledge=list()
while h<=people_amount:
    player_name=input("Enter Player "+str(h)+" name : ")
    player_profile={"name":player_name,"Money":150,"card":[],"player_round_status":"Playing","money_in_pot":0}
    knowledge.append(player_profile)
    h=h+1

#print(knowledge)
cards=list()
for i in [" of Clubs"," of Diamonds", " of Hearts"," of Spades"]:
    for j in["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]:
        cards.append(j+i)
#print(cards)
cc=0
for items in cards:
    cc=cc+1
#print(cc)
count=51
f=1
while f<=people_amount:
    random_number=random.randint(0,count)
    knowledge[f-1]["card"].append(cards[random_number])
    cards.remove(cards[random_number])
    count=count-1
    random_number=random.randint(0,count)
    knowledge[f-1]["card"].append(cards[random_number])
    cards.remove(cards[random_number])
    count=count-1
    f=f+1
print(knowledge)
  

#print(player1_cards)
#print(player2_cards)
#knowledge[0]["Player_cards"]=player1_cards
#knowledge[1]["Player_cards"]=player2_cards
#knowledge[0]["Money"]=150
#knowledge[1]["Money"]=150

print(people_amount)
#print(knowledge)
round_status=" "
s=list()
d=0

while d<people_amount:
    s.append(d)
    d=d+1
print(s)
order=list()
q=0
while True:
    dealer=random.randint(0,people_amount-1)
    if dealer in s:
        s.remove(dealer)
        order.append(dealer)
        q=q+1
    if q==people_amount:
        break
      
        

first_player_decision="Check"

first_player_bet=0
current_pot=0


def fold(player,amount):
    print(" ")   
    amount=knowledge[player]["money_in_pot"]+int(amount)
    knowledge[player]["money_in_pot"]=0
    print(knowledge[player]["name"]+" Has folded and has amount : "+str(knowledge[player]["Money"]))
    print("  ")
    if round_status=="over":
        print("Round Over")
    return amount

def bet(g):
    while True:
        player_bet=input("Please enter bet amount :")
        try:
            knowledge[g]["money_in_pot"]=knowledge[g]["money_in_pot"]+int(player_bet)
        except:
            print("please enter valid bet amount")
            continue
        if int(player_bet) > knowledge[g]["Money"]:
            print("Insuffiecient funds")
            print(knowledge[g]["name"],"only has amount",knowledge[g]["Money"])
            continue
        elif int(player_bet)<=0:
            print("Cannot Bet 0 or less than zero")
            continue
        knowledge[g]["Money"]=knowledge[g]["Money"]-int(player_bet)
        print(knowledge[g]["name"],"has amount",knowledge[g]["Money"])
        print(knowledge)
        break

    

def call(player,amount):
    knowledge[player]["money_in_pot"]=knowledge[player]["money_in_pot"]+int(amount)
    knowledge[player]["Money"]=knowledge[player]["Money"]-int(amount)
    print(knowledge[player]["name"]+" has bet "+ str(knowledge[player]["money_in_pot"]))
    print(knowledge[player]["name"],"has amount",knowledge[player]["Money"])
    

def Raise(player,otherbet):
    while True:
        raise_amount=input("How much do you want to raise by : ")
        try:
            bet_amount=int(otherbet)+int(raise_amount)
            knowledge[player]["money_in_pot"]=knowledge[player]["money_in_pot"]+bet_amount
        except:
            print("please enter valid raise amount")
            continue
        if int(bet_amount) > knowledge[player]["Money"]:
            print("Insuffiecient funds")
            print(knowledge[player]["name"],"only has amount",knowledge[player]["Money"])
            continue
        elif int(bet_amount)<=0:
            print("Cannot Bet 0 or less tha zero")
            continue
        knowledge[player]["Money"]=knowledge[player]["Money"]-bet_amount
        break    
    
    

second_player=0
stupid=0

    


for g in order:
    if stupid==0:
        knowledge[g]["player_round_status"]=input(knowledge[g]["name"]+"Do you want to Fold, Bet or Check : ")
        if knowledge[g]["player_round_status"]=="Fold":
        current_pot=fold(g,current_pot)
        elif knowledge[g]["player_round_status"]=="Bet":
            first_person=g
            bet(g)
            stupid=stupid+1
        elif knoledge[g]["player_round_status"]=="Check":
                continue
    if stupid>=1:
        for f in order:
            if knowledge[f]["player_round_status"]=="Check":
                print(knowledge[f]["name"]+" You have to Call, Raise or Fold ")
                if knowledge[f]["player_round_status"]=="Fold":
                current_pot=fold(g,current_pot)
                elif knowledge[f]["player_round_status"]=="Call":
                    for iji in order:
                        if knowledge[iji]["money_in_pot"]>=0:
                             call(f,knowledge[iji]["money_in_pot"])
                             break                                      
                elif knowledge[f]["player_round_status"]=="Raise":
                    for nub in order:
                        if knowledge[nub]["money_in_pot"]>0:
                            Raise(f,knowledge[nub]["money_in_pot"])
                            break
                    for jib in order:
                        if knowledge[jib]["money_in_pot"]>0:
                            knowledge[jib]["player_round_status"]=input("do you want to fold call or raise: ")
                            if knowledge[jib]["player_round_status"]

          
                if second_player_decision=="Raise":
                    second_player_raise_amount=input("How much do you want to raise by:")
                    current_pot=Raise(second_player,second_player_raise_amount,first_player_raise_amount,current_pot)
                    first_player_decision=input("do you want to fold,call or raise: ")
                    if first_player_decision=="Raise":
                        continue
                    elif first_player_decision=="Fold":
                        round_status="over"
                        fold(dealer,second_player,current_pot)
                        break
                    elif first_player_decision=="Call":
                        round_status="over"
                        current_pot=call(dealer,second_player_raise_amount,current_pot)
                        break
                if second_player_decision=="Fold":
                    round_status="over"
                    fold(second_player,dealer,current_pot)
                    break
                elif second_player_decision=="Call":
                    round_status="over"
                    current_pot=call(second_player,first_player_raise_amount,current_pot)
                    break    


                   
#----------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------

        knowledge[g]["player_round_status"]=input(knowledge[g]["name"]+"Do you want to Fold, Raise or  Call")
        

    
         

       


if first_player_decision=="Check":
    second_player_decision=input("Do you want to check,fold or bet : ")
    if second_player_decision=="Check":
        print("both player have checked")
        print("round over")
        round_status="over"
    elif second_player_decision=="Fold":
        fold(dealer,second_player,current_pot)
    elif second_player_decision=="Bet":
        while True:
            second_player_bet=input("Please enter bet amount :")
            print(" ")
            current_pot=bet(second_player,second_player_bet,current_pot)
            if b==1:
                continue
            break
        print(knowledge[second_player]["name"]+" it is your turn")
        first_player_decision=input("do you want to fold, call or raise: ")
        
        if first_player_decision=="Fold":
            round_status="over"
            fold(dealer,second_player,current_pot)

        elif first_player_decision=="Call":
            first_player_bet=int(second_player_bet)
            round_status="over"
            current_pot=call(second_player,second_player_bet,current_pot)

        elif first_player_decision=="Raise":
             while True:
                first_player_raise_amount=input("How much do you want to raise by : ")
                current_pot=Raise(dealer,first_player_raise_amount,second_player_bet,current_pot)
                second_player_decision=input("do you want to fold, call or raise: ")
                if second_player_decision=="Raise":
                    second_player_raise_amount=input("How much do you want to raise by:")
                    current_pot=Raise(second_player,second_player_raise_amount,first_player_raise_amount,current_pot)
                    first_player_decision=input("do you want to fold,call or raise: ")
                    if first_player_decision=="Raise":
                        continue
                    elif first_player_decision=="Fold":
                        round_status="over"
                        fold(dealer,second_player,current_pot)
                        break
                    elif first_player_decision=="Call":
                        round_status="over"
                        current_pot=call(dealer,second_player_raise_amount,current_pot)
                        break
                if second_player_decision=="Fold":
                    round_status="over"
                    fold(second_player,dealer,current_pot)
                    break
                elif second_player_decision=="Call":
                    round_status="over"
                    current_pot=call(second_player,first_player_raise_amount,current_pot)
                    break    
       
#----------------------------------------------------------------------------------------------
   
        

elif first_player_decision=="Bet":
    x=0
    
    
    print(knowledge[second_player]["name"]+" it is your turn")
    second_player_decision=input("do you want to fold, call or raise: ")
        
    if second_player_decision=="Fold":
        round_status="over"
        fold(second_player,dealer,current_pot)
            

    elif second_player_decision=="Call":
        second_player_bet=int(first_player_bet)
        round_status="over"
        current_pot=call(second_player,second_player_bet,current_pot)
            

    elif second_player_decision=="Raise":
        while True:
            second_player_raise_amount=input("How much do you want to raise by : ")
            current_pot=Raise(second_player,second_player_raise_amount,first_player_bet,current_pot)
            first_player_decision=input("do you want to fold, call or raise: ")

            if first_player_decision=="Raise":
                first_player_raise_amount=input("How much do you want to raise by:")
                current_pot=Raise(dealer,first_player_raise_amount,second_player_raise_amount,current_pot)
                second_player_decision=input("do you want to fold,call or raise: ")

                if second_player_decision=="Raise":
                    continue
                elif second_player_decision=="Fold":
                    round_status="over"
                    fold(second_player,dealer,current_pot)
                    break
                elif second_player_decision=="Call":
                    round_status="over"
                    current_pot=call(second_player,first_player_raise_amount,current_pot)
                    break
            if first_player_decision=="Fold":
                round_status="over"
                fold(dealer,second_player,current_pot)
                break

            elif first_player_decision=="Call":
                round_status="over"
                current_pot=call(dealer,second_player_raise_amount,current_pot)
                break


print("Yay")           
               
   

        
    




