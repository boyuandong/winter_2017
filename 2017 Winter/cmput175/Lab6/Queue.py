class Queue:
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
        self.__head=(self.__head-1)%self.__capacity
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