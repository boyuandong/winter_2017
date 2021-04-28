# A Stack implementation
def main():
    stack_forward=Stack()
    stack_back=Stack()
    home_page='[www.cs.ualberta.ca]'
    stack_back.push(home_page)
    print(stack_back.peek())
    last_browse=None
    while True:
        # ask the user to enter 
        browse=input()
        # if a user enters '=' to ask to browse a new page
        if browse=='=':
            # add the new page and show it
            new_page=input()
            new_page='['+str(new_page)+']'
            stack_back.push(new_page)
            print(stack_back.peek())
        # if a user enters '<' to ask to browse the previous page
        if browse=='<':
            # if there are no browsing history in stock_back
            if stack_back.size()==1:
                print('%s is an invalid action'%browse)
                stack_back.push(stack_forward.pop())
                print(stack_back.peek()) 
            # if there are browsing history in stock_back, show the previous page
            else:
                # pop the current page from stack_back and push it in stack_forward
                stack_forward.push(stack_back.pop())                
                print(stack_back.peek()) 
        # if a user enters '>' to ask to browse the forward page
        if browse=='>':
            # if the stack_forward is not empty means there are forward pages
            if not stack_forward.is_empty():
                stack_back.push(stack_forward.pop())
            # if the forward pages in stack_forwad is empty
            elif stack_forward.is_empty():
                print('%s is an invalid action'%browse) 
            print(stack_back.peek())
        # if a user enters "<" and then a new web address
        if last_browse=='<' and browse=='=':
            # erase the user's previous browsing history in the ">" direction
            while not stack_forward.is_empty():
                stack_forward.pop()
        # assign the browse to the last_browse and then begin a new loop
        last_browse=browse
class Stack:
    
    def __init__(self):
        self.__items = []
        
    def push(self, item):
        self.__items.append(item)
        
    def pop(self):
        return self.__items.pop()
    
    def peek(self):
        return self.__items[len(self.__items)-1]
    
    def is_empty(self):
        return len(self.__items) == 0
    
    def size(self):
        return len(self.__items)
main()