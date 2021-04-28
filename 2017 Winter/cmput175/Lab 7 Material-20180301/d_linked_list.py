from d_linked_node import d_linked_node

class d_linked_list:
    
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0        

            
    def search(self, item):
        current = self.__head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
        return found
        
    def index(self, item):
        current = self.__head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
                index = index + 1
        if not found:
                index = -1
        return index        
         
    def add(self, item):
        # TODO: 
        # create an new node that next references to the head
        temp=d_linked_node(item,self.__head,None)
        if self.__head!=None:
            # when the list is not empty head's previous references the new node
            self.__head.setPrevious(temp)
        else:
            # when the list is empty the tail=new node
            self.__tail=temp
        self.__head=temp
        self.__size+=1
        
    def remove(self, item):
        # TODO:
        current=self.__head
        previous=None
        found=False
        if self.__head==None:
            # when the list is not empty
            raise Exception('Error:The double-linked list is empty')
        while not found:
            if current.getData()==item:
                found=True
            else:
                # when not found the node, move the current and the previous forward
                previous=current
                current=current.getNext()
        if previous==None:
             # if the first node is the node that sould be removed
            self.__head=current.getNext()
        else:
            # previous node's next reference to the current node's next reference
            previous.setNext(current.getNext())
        if current.getNext()!=None:
            # when the current is not the last node, set the current node's previouse reference to the previous node
            current.getNext().setPrevious(previous)
        else:
            # when the current is the last node
            self.__tail=previous
        self.__size-=1
        
    def append(self, item):
        # TODO:
        # create an new node
        temp=d_linked_node(item,None,None)
        if self.__head==None:
            # when the double linked list is empty
            self.__head=temp
        else:
            # when the list is not empty
            self.__tail.setNext(temp)
            temp.setPrevious(self.__tail)
        self.__tail=temp
        self.__size+=1
        
    def insert(self, pos, item):
        # TODO:
        index=0
        current=self.__head
        previous=None
        found=False
        #create an new node
        temp=d_linked_node(item,None,None)
        if pos==0:
            # when pos is 0 item goes to the begining of the list
            self.__head.setPrevious(temp)
            temp.setNext(self.__head)
            self.__head=temp
        else:
            while current!=None and not found:
                if index==pos:
                    # the index equal to the pos
                    found=True
                else:
                    # not found the position
                    previous=current
                    current=current.getNext()
                    index+=1
            if not found:
                # if not found the index equal to pos
                # means the number of the nodes in the list is less than the pos 
                raise Exception('Error: the pos is larger than the size of the list')
            else:
                # found the pos and insert the new item node
                current.setPrevious(temp)
                previous.setNext(temp)
                temp.setNext(current)
                temp.setPrevious(previous)
        self.__size+=1
        
    def pop1(self):
        # TODO:
        if self.__head==None:
            raise Exception('Error: The list is empty')
        last_node=self.__tail.getData()
        if self.__head.getNext()==None:
            # there is only one node in the list
            self.__head=None
            self.__tail=None
        else:
            self.__tail=self.__tail.getPrevious()
            self.__tail.setNext(None)
            
        self.__size-=1
        return last_node
    
    def pop(self, pos):
        # TODO:
        if pos<0:
            raise Exception('Error: the pos can not less than zero')
        index=0
        current=self.__head
        previous=None
        found=False
        if pos==0:
            if current.getNext()!=None:
                # pop the first node
                self.__head=current.getNext()
                current.getNext().setPrevious(None)
            else:
                # pop the only node
                self.__head=None
                self.__tail=None
            self.__size-=1   
            return current.getData()
        
        else:
            # if pos!=0
            while not found and current!=None:
                if index==pos:
                    found=True
                else:
                    previous=current
                    current=current.getNext()
                    index+=1
            if not found:
                # if not found the index equal to pos
                # means the number of the nodes in the list is less than the pos 
                raise Exception('Error: the pos is larger than the size of the list')
            else:
                # found the pos
                if current.getNext()!=None:
                    # if the pos is not the last node
                    current.getNext().setPrevious(previous)
                    previouse.setNext(current.getNext())
                else:
                    # if pop the last node
                    self.__tail=self.__tail.getPrevious()
                    self.__tail.setNext(None)
                self.__size-=1
                return current.getData()  
        
                    
    def search_larger(self, item):
        # TODO:
        current=self.__head
        found=False
        index=0
        while current!=None and not found:
            if current.getData()>item:
                found=True
            else:
                current=current.getNext()
                index+=1
        if not found:
            index=-1
            
        return index
    
    def get_size(self):
        # TODO:    
        return self.__size
    def get_item(self, pos):
        # TODO:   
        found=False
        if pos>=0:
            # if the pos is positive or equal to 0
            index=0
            current=self.__head
            while current!=None and not found:
                if index==pos:
                    found=True
                else:
                    current=current.getNext()
                    index+=1
        elif pos<0:
            # if the pos is negative
            index=-1
            current=self.__tail
            while current!=None and not found:
                if index==pos:
                    found=True
                else:
                    current=current.getPrevious()
                    index-=1
                    
        if not found:
            print('Error: the pos is not valid')
        else:
            return current.getData()
           
    def __str__(self):
        # TODO:   
        string=''
        current=self.__head
        while current.getNext()!=None:
            string+=str(current.getData())+' '
            current=current.getNext()
        string+=str(current.getData())
        
        return string

def test():
                  
    linked_list = d_linked_list()
                    
    is_pass = (linked_list.get_size() == 0)
    assert is_pass == True, "fail the test"
            
    linked_list.add("World")
    linked_list.add("Hello")    
        
    is_pass = (str(linked_list) == "Hello World")
    assert is_pass == True, "fail the test"
              
    is_pass = (linked_list.get_size() == 2)
    assert is_pass == True, "fail the test"
            
    is_pass = (linked_list.get_item(0) == "Hello")
    assert is_pass == True, "fail the test"
        
        
    is_pass = (linked_list.get_item(1) == "World")
    assert is_pass == True, "fail the test"    
            
    is_pass = (linked_list.get_item(0) == "Hello" and linked_list.get_size() == 2)
    assert is_pass == True, "fail the test"
            
    is_pass = (linked_list.pop(1) == "World")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.pop1() == "Hello")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.get_size() == 0)
    assert is_pass == True, "fail the test" 
                    
    int_list2 = d_linked_list()
                    
    for i in range(0, 10):
        int_list2.add(i)      
    int_list2.remove(1)
    int_list2.remove(3)
    int_list2.remove(2)
    int_list2.remove(0)
    is_pass = (str(int_list2) == "9 8 7 6 5 4")
    assert is_pass == True, "fail the test"
                
    for i in range(11, 13):
        int_list2.append(i)
    is_pass = (str(int_list2) == "9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    for i in range(21, 23):
        int_list2.insert(0,i)
    is_pass = (str(int_list2) == "22 21 9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    is_pass = (int_list2.get_size() == 10)
    assert is_pass == True, "fail the test"    
                    
    int_list = d_linked_list()
                    
    is_pass = (int_list.get_size() == 0)
    assert is_pass == True, "fail the test"
                    
        
                    
    for i in range(0, 1000):
        int_list.append(i)      
    correctOrder = True
            
    is_pass = (int_list.get_size() == 1000)
    assert is_pass == True, "fail the test"            
            
        
    for i in range(0, 200):
        if int_list.pop1() != 999 - i:
            correctOrder = False
                            
    is_pass = correctOrder
    assert is_pass == True, "fail the test" 
            
    is_pass = (int_list.search_larger(200) == 201)
    assert is_pass == True, "fail the test" 
            
    int_list.insert(7,801)   
        
    is_pass = (int_list.search_larger(800) == 7)
    assert is_pass == True, "fail the test"
            
            
    is_pass = (int_list.get_item(-1) == 799)
    assert is_pass == True, "fail the test"
            
    is_pass = (int_list.get_item(-4) == 796)
    assert is_pass == True, "fail the test"
                    
    if is_pass == True:
        print ("=========== Congratulations! Your have finished exercise 1! ============")
                
if __name__ == '__main__':
    test()