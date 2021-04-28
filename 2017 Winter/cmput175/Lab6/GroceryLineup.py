def main():
    # create two bounded queue, one is normal line, the other one is VIP line. each with 3 capacity
    Normal=Queue(3)
    VIP=Queue(3)
    # ask the user to choose, keep running the program when the user does not exit
    enter=input('Add, Serve, or Exit:')
    while enter!='exit':
        # if the user enter add
        if enter=='add':
            # ask the user to input the item and if is VIP
            item=input('Enter the name of the person to add: ')
            is_VIP=input('Is the customer VIP? ')
            # if the customer is VIP
            if is_VIP=='True':
                # if the VIP line is full, show an Error, else insert the customer to the VIP line
                if VIP.is_full():
                    print('Error: VIP customer queue is full')
                else:
                    VIP.enqueue(item)
                    print('add %s to VIP line.'%item)
            # else if the customer is not VIP
            elif is_VIP=='False':
                # if the Normal line is full, show an Error, else insert the customer to the Normal line
                if Normal.is_full():
                    print('Error: Normal customer queue is full')
                else:
                    Normal.enqueue(item)
                    print('add %s to the line.'%item)
        # else if the user enter serve
        elif enter=='serve':
            # if the VIP line is not empty, serve the VIP customer first
            if not VIP.is_empty():
                serve=VIP.dequeue()
                print('%s has been served'%serve)
            # if VIP line is empty and Normal line is not empty, then serve the Normal customer
            elif not Normal.is_empty():
                serve=Normal.dequeue()
                print('%s has been served'%serve)
            # else if both lines are empty, show an Error
            else:
                print('Error: Queues are empty')
        # show the customers in each line
        print('people in the line: %s'% str(Normal) )
        print('VIP customers queue: %s'% str(VIP))
        # ask the user to choose again
        enter=input('Add, Serve, or Exit:')
    
    print('Quitting')
    
class Queue:
    def __init__(self,capacity):
        assert isinstance(capacity, int), ('Error: Type error: %s' % (type(capacity))) 
        assert capacity >= 0, ('Error: Illegal capacity: %d' % (capacity))
        self.__items = [] 
        self.__capacity = capacity        
    def enqueue(self,item):
        if len(self.__items)>=self.__capacity:
            raise Exception('Error Queue is full')
        self.__items.append(item)
    def dequeue(self):
        if len(self.__items)<=0:
            raise Exception('Error Queue is empty')
        return self.__items.pop(0)
    def peek(self):
        if len(self.__items)<=0:
            raise Exception('Error Queue is empty')
        return self.__items[0]
    def is_empty(self):
        return len(self.__items)==0
    def is_full(self):
        return len(self.__items)==self.__capacity
    def size(self):
        return len(self.__items)
    def capacity(self):
        return self.__capacity
    def clear(self):
        self.__items=[]
    def __str__(self):
        str_exp=']'
        for item in self.__items:
            if item!=self.__items[-1]:
                str_exp+=str(item)+','
            else:
                str_exp+=str(item)
        return str_exp+']'
main()