def main():
    import time
    # Create two queues, one bounded queue and one circular queue, with n capacity
    n=10000
    bounded=BoundedQueue(n)
    circular=CircularQueue(n)
    # insert n items into each queue.
    for i in range(n):
        bounded.enqueue(i)
        circular.enqueue(i)
    # dequeue the bounded queue n times and calculate the running time
    start_bounded=time.time()
    while not bounded.is_empty():
        bounded.dequeue()
    end_bounded=time.time()
    time_intervals_bounded=end_bounded-start_bounded
    print('Bounded Queue requires %10.7f seconds to dequeue %d times'%(time_intervals_bounded,bounded.capacity()))
    start_circular=time.time()
    # dequeue the circular queue n times and calculate the running time
    while not circular.is_empty():
        circular.dequeue()
    end_circular=time.time()
    time_intervals_circular=end_circular-start_circular   
    # Print the dequeue running time for each queue and the runtime difference on screen.
    print('Circular Queue requires %10.7f seconds to dequeue %d times'%(time_intervals_circular,circular.capacity()))
    differences=abs(time_intervals_bounded-time_intervals_circular)
    print('the differences between the two type Queues is %10.7f'%differences)
    
class BoundedQueue:
    # -Bounded Queue
    def __init__(self,capacity):
        assert isinstance(capacity, int), ('Error: Type error: %s' % (type(capacity))) 
        assert capacity >= 0, ('Error: Illegal capacity: %d' % (capacity))
        self.__items = [] 
        self.__capacity = capacity        
    def enqueue(self,item):
        # -add an item
        # raise an exception when queue is full
        if len(self.__items)>=self.__capacity:
            raise Exception('Error Queue is full')
        self.__items.append(item)
    def dequeue(self):
        # -pop the first item
        # raise an exception when queue is empty
        if len(self.__items)<=0:
            raise Exception('Error Queue is empty')
        return self.__items.pop(0)
    def peek(self):
        # -peek the first item
        # raise an exception when queue is empty
        if len(self.__items)<=0:
            raise Exception('Error Queue is empty')
        return self.__items[0]
    def is_empty(self):
        # -check if the queue is empty
        return len(self.__items)==0
    def is_full(self):
        # -check if the queue is full
        return len(self.__items)==self.__capacity
    def size(self):
        # -return the number of items
        return len(self.__items)
    def capacity(self):
        # -return the capacity
        return self.__capacity
    def clear(self):
        # -reset the queue
        self.__items=[]
    def __str__(self):
        # str the queue
        str_exp=''
        for item in self.__items:
            str_exp+=str(item)+' '
        return str_exp
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
    
main()