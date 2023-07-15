class Utility():
    def __init__(self):
        self.idk=0
   
    def pairs_method(self,cards,val,need_high_card,x=False):
        '''The pairs_method of the Hand class identifies if either a pair, three of a kind or a four of kind is present depending on the input
        paramteres:
            1.The first parameter is the list of cards
            2.The second parameter is what kind of pair needs to be identified, either 2,3 or 4
            3. The third parameter determins if a high cards should also be returned with the function
            4. the fourth parameter is an optional parameter that determins how many cards should be returned
        returns:
            1. It returns either True or False depending if the item is present
            2. It returns the list of cards that form the hand'''
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
        '''The multiple_pairs_method of the Hand class identifies if either a two pair or a full house present depending on the input
        paramteres:
            1.The first parameter is the list of cards
            2.The second parameter is what kind of pairs needs to be identified, either 2(for two pair) or 3(for full house)
        
        returns:
            1. It returns either True or False depending if the item is present
            2. It returns the list of cards that form the hand'''
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
        '''The calculate_decimal_points method of the hand class turns the player's hand into a decimal number
        parameters:
            1.The parameter is the list of cards
        returns:
            1.It returns the decimal value for the player's hand'''
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


