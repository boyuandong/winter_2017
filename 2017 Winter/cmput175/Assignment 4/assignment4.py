def main():
    # ask the player to enter the start number
    start_num=input('Choose your initial size of the pile. Should be more than 2: ')
    while not start_num.isdigit() or int(start_num)<=2:
        start_num=input('Choose your initial size of the pile. Should be more than 2: ')
    start_state=[int(start_num)]
    # create the root
    root=Minimax(start_state,'MAX')
    # build the tree
    root.build()
    # print the tree
    root.print_tree(' ',True)
    
def split_num(num):
    # -split the single number
    i=1
    j=num-1
    num_lst=[]
    # find all the possiblities to split the number
    # and then append the valid pairs into the num_lst
    while i<j:
        num_lst.append([i,j])
        i+=1
        j-=1        
    return num_lst
def split(alist):
    # -split a list of numbers
    total_lst=[]
    for num in alist:
        # for each number that greater than 2 in the list
        if num>2:
            # find the possible lists of numbers to divide the pile
            possible_lst=split_num(num)
            for i,j in possible_lst:
                # for each pair of two numbers which divide the pile
                # copy a new list the same with the original list
                # replace one to the original number and append the other one into the new list
                new_lst=alist[:]
                new_lst[alist.index(num)]=i
                new_lst.append(j)
                new_lst.sort()
                total_lst.append(new_lst)
    return total_lst

class Minimax:
    def __init__(self, nimState, minMaxLevel):
        self.state=nimState
        self.level=minMaxLevel
        self.child=[]
    def add_child(self,newstate):
        # -add the new child node
        # if the self is Max then the child is Min
        # if the self is Min then the child is Max
        if self.level=='MAX':
            new_level='MIN'
        elif self.level=='MIN':
            new_level='MAX'
        # create the new child node and add it to the child node list
        new_child=Minimax(newstate,new_level)
        self.child.append(new_child)
        
    def build(self):
        # -build the tree
        # find the ways to divide piles by calling the split function
        newstate_lst=split(self.state)
        # for each way to divide the piles create a new child node and add it into the child parent node
        for newstate in newstate_lst:
            self.add_child(newstate)
        # let each child node in the parent node build its own tree
        for child in self.child:
            child.build()
            
    def print_tree(self,indentation, last):
        # -print the tree
        print(indentation,end='')
        string=''
        # if the node is the last one in the list
        if last:
            string+='\-'
            indentation += "  "
        else:
            # if the node is not the last one in the list
            string+='+ '
            indentation += "| "
        # add the state to the string to print it out
        string+=str(self.state)
        # if is the last node also add and print its level
        if last: string+=' '+str(self.level)
        print(string)
        i=0
        for child in self.child:
            # for each child in the child nodes
            last=False
            i+=1
            # if the child is the last one last=True
            if i==len(self.child): last = True
            # let the child node call the print tree to print the tree
            child.print_tree(indentation, last)           

main()
