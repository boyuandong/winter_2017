import random
import os.path
def main():
    cards_num=52
    # prompt the player to enter the filename and make sure the file exists
    filename=input('Please enter the filename:')
    assert os.path.exists(filename), 'Input file not found'
    # determine if the cards are complete valid and not repeated
    valid_cards=determine_cards(cards_num,filename)
    # distribute cards to two players
    player1,player2=distribute_cards(valid_cards,cards_num)
    # ask the player to enter the number of war face-down cards from 1,2,3
    war_num=int(input('Please enter the number of war cards face-down:'))
    while war_num not in [1,2,3]:
        war_num=int(input('Please enter the number of war cards face-down from 1,2,3:'))
    # end_game<-False
    end_game=False
    # create the OnTable object
    cards_on_table=OnTable()
    # when the game is not end
    while not end_game:
        # either player put a face up card on the table
        face_up1=player1.dequeue()
        cards_on_table.place(1,face_up1,False)
        face_up2=player2.dequeue()
        cards_on_table.place(2,face_up2,False)
        # show the cards on the table and the number of the left cards of each player
        print(str(cards_on_table))
        print('Player1: %d cards'%player1.size())
        print('Player2: %d cards'%player2.size())
        input('Press return key to continue.')
        # compare two face up cards
        compare_result=compare_cards(face_up1,face_up2)
        if compare_result==1:
            # if faceUp1>faceUp2
            get_cards=cards_on_table.clearnTable()
            for item in get_cards:
                player1.enqueue(item)
        elif compare_result==-1:
            # if faceUp1<faceUp2
            get_cards=cards_on_table.clearnTable()
            for item in get_cards:
                player2.enqueue(item)  
        else:
            # if faceUp1=faceUp2
            if player1.size()<=war_num:
                # if the player1 do not have enough cards
                # player2 get all the cards on the table
                get_cards=cards_on_table.clearnTable()
                for item in get_cards:
                    player2.enqueue(item)
                while not player1.is_empty():
                    # player2 get all the cards of player1
                    player2.enqueue(player1.dequeue())
                end_game=True                
               
            else:
                # player1 have enough cards
                i=0
                while i<war_num:
                    # get war_num face_down cards from player1
                    face_down1=player1.dequeue()
                    # place face_down cards on the table
                    cards_on_table.place(1,face_down1,True)
                    i+=1
                if player2.size()<=war_num:
                    # if the player2 do not have enough cards
                    # player1 get all the cards on the table
                    get_cards=cards_on_table.clearnTable()
                    for item in get_cards:
                        player1.enqueue(item)
                    while not player2.is_empty():
                        # player1 get all the cards of player2
                        player1.enqueue(player2.dequeue())
                    end_game=True     
                else:
                    # player1 have enough cards
                    j=0
                    while j<war_num:
                        # get war_num face_down cards from player2
                        face_down2=player2.dequeue()
                        # place face_down cards on the table
                        cards_on_table.place(2,face_down2,True)
                        j+=1                       
                    
                                  
        if player1.size()==0:
            print('Player1: %d cards'%player1.size())
            print('Player2: %d cards'%player2.size())             
            print('Congratulations! player2 win!')
            end_game=True
        elif player2.size()==0:
            print('Player1: %d cards'%player1.size())
            print('Player2: %d cards'%player2.size())             
            print('Congratulations! player1 win!')
            end_game=True
         
    print('Game end.')
        
    
def compare_cards(card1,card2):
    # -compare two cards
    rank_value=None
    rank_num={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':10,'J':11,'Q':12,'K':13,'A':14}
    if rank_num[card1[0]]==rank_num[card2[0]]:
        # if card1=card2 return 0
        rank_value=0
    elif rank_num[card1[0]]>rank_num[card2[0]]:
        # if card1>card2 return 1
        rank_value=1
    elif rank_num[card1[0]]<rank_num[card2[0]]:
        # if card1<card2 return -1
        rank_value=-1
    return rank_value
def determine_cards(cards_num,filename):
    
    # -determine if the cards are complete all valid and no repeated cards
    # all the numbers and suits of the cards
    num_list=['0','2','3','4','5','6','7','8','9','J','Q','K','A','j','q','k','a']
    suit_list=['D','C','H','S','d','c','h','s']
    infile=open(filename,'r')
    # a new list to store valid cards
    valid_cards=[]
    for card in infile:
        # determine the valid cards
        card=card.strip()
        if (card[0] in num_list) and (card[1] in suit_list):
            valid_cards.append(card)
    assert len(valid_cards)==cards_num,'Error: The cards are not valid.'
    # determine if there are repeated cards
    for card in valid_cards:
        assert valid_cards.count(card)==1,'Error: There are repeated cards'
    infile.close()
    return valid_cards
    
def distribute_cards(valid_cards,cards_num):
    # -distribute cards
    # create two players
    player1=CircularQueue(cards_num)
    player2=CircularQueue(cards_num)
    # add the cards into the queues
    i=0
    while i<cards_num:
        player1.enqueue(valid_cards[i])
        player2.enqueue(valid_cards[i+1])
        i+=2
    players=[player1,player2]
    # start randomly with either player
    random.shuffle(players)
    return players
    
class OnTable:
    # -represent the cards on the table
    def __init__(self):
        self._cards=[]
        self._faceUp=[]
    def place(self,player,card,hidden):
        # -place the card on the table
        if player==1:
            # player1 add at the beging of the list
            self._cards.insert(0,card)
            self._faceUp.insert(0,not hidden)
        elif player==2:
            # player2 add at the end of the list
            self._cards.append(card)
            self._faceUp.append(not hidden)
    def clearnTable(self):
        # -reset the cards and faceUp, return the cards on the table
        cards=self._cards[:]
        self._cards=[]
        self._faceUp=[]
        return cards
    def __str__(self):
        # -show the table cards as a list format string
        if len(self._cards)!=0:
            # if there are cards on the table
            show_list=[]
            i=0
            while i<len(self._cards):
                if self._faceUp[i]:
                    # if the cards is face-up append it to the show list
                    show_list.append(self._cards[i])
                else:
                    # if the cards is face-down append XX to the show list
                    show_list.append('XX')
                i+=1
            # transform the show list into a string as a list format
            show_string='['
            j=0
            while j<len(show_list)-1:
                show_string+=show_list[j]+', '
                j+=1
            show_string+=show_list[j]+']'
        else:
            # if there are no cards on the table
            show_string='[]'
        
        return show_string

    
class CircularQueue:
    # -Circular Queue
    def __init__(self,capacity):
        if type(capacity)!=int or capacity<=0:
            raise Exception('Capacity Error')
        self.__items=[]
        self.__capacity=capacity
        self.__count=0
        self.__head=0
        self.__tail=0
    def enqueue(self,item):
        # -add an item
        # raise an exception when queue is full        
        if self.__count==self.__capacity:
            raise Exception('Error: Queue is full')
        if len(self.__items)<self.__capacity:
            self.__items.append(item)
        else:
            self.__items[self.__tail]=item
        self.__count+=1
        self.__tail=(self.__tail+1)%self.__capacity
    def dequeue(self):
        # -pop the first item
        # raise an exception when queue is empty        
        if self.__count==0:
            raise Exception('Error: Queue is empty')
        item=self.__items[self.__head]
        self.__items[self.__head]=None
        self.__count-=1
        self.__head=(self.__head+1)%self.__capacity
        return item
    def peek(self):
        # -peek the first item
        # raise an exception when queue is empty        
        if self.__count==0:
            raise Exception('Error: Queue is empty')
        return self.__items[self.__head]
    def is_empty(self):
         # -check if the queue is empty
        return self.__count==0
    def is_full(self):
        # -check if the queue is full
        return self.__count==self.__capacity
    def size(self):
        # -return the number of items
        return self.__count
    def capacity(self):
        # -return the capacity
        return self.__capacity
    def clear(self):
        # -reset the queue
        self.__items=[]
        self.__count=0
        self.__head=0
        self.__tail=0
    def __str__(self):
        # -str the queueu
        str_exp=']'
        i=self.__head
        for j in range(self.__count):
            str_exp+=str(self.__items[i])+' '
            i=(i+1)%self.__capacity
        return str_exp+']'
    def __repr__(self):
        # -repr the queue
        exp=str(self.__items)+'H='+str(self.__head)+'T='+str(self.__tail)+'('+str(self.__count)+'/'+str(self.__capacity)+')'
        return exp
    
main()