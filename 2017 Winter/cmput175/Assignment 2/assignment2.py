import random as rnd
import os
import sys

class Grid():
    def __init__(self, row=4, col=4, initial=2):
        self.row = row                              # number of rows in grid
        self.col = col                              # number of columns in grid
        self.initial = initial                      # number of initial cells filled
        self.score = 0

        self._grid = self.createGrid(row, col)    # creates the grid specified above

        self.emptiesSet = list(range(row * col))    # list of empty cells

        for _ in range(self.initial):               # assignation to two random cells
            self.assignRandCell(init=True)


    def createGrid(self, row, col):

        """
        Create the grid here using the arguments row and col
        as the number of rows and columns of the grid to be made.

        The function should return the grid to be used in __init__()
        """
        # create a list of row and then append the row to the grid list
        grid_list=[]
        for i in range(row):
            row_list=[]
            for j in range(col):
                row_list.append(0)
            grid_list.append(row_list)
            
        return grid_list        



    def setCell(self, cell, val):

        """
        This function should take two arguments cell and val and assign
        the cell of the grid numbered 'cell' the value in val.

        This function does not need to return anything.

        You should use this function to change values of the grid.
        """
        # get the row number and the column number then the value
        row_num=cell//self.row 
        col_num=cell%self.row 
        self._grid[row_num][col_num]=val        


    def getCell(self, cell):

        """"
        This function should return the value in cell number 'cell'
        of the grid.

        You should use this function to access values of the grid
        """
        # get the row number and the column number then return the value
        row_num=cell//self.row 
        col_num=cell%self.row 
        return self._grid[row_num][col_num]         


    def assignRandCell(self, init=False):

        """
        This function assigns a random empty cell of the grid
        a value of 2 or 4.

        In __init__() it only assigns cells the value of 2.

        The distribution is set so that 75% of the time the random cell is
        assigned a value of 2 and 25% of the time a random cell is assigned
        a value of 4
        """

        if len(self.emptiesSet):
            cell = rnd.sample(self.emptiesSet, 1)[0]
            if init:
                self.setCell(cell, 2)
            else:
                cdf = rnd.random()
                if cdf > 0.75:
                    self.setCell(cell, 4)
                else:
                    self.setCell(cell, 2)
            self.emptiesSet.remove(cell)


    def drawGrid(self):

        """
        This function draws the grid representing the state of the game
        grid
        """

        for i in range(self.row):
            line = '\t|'
            for j in range(self.col):
                if not self.getCell((i * self.row) + j):  
                    line += ' '.center(5) + '|'
                else:
                    line += str(self.getCell((i * self.row) + j)).center(5) + '|'   
            print(line)
        print()
   
    
    def updateEmptiesSet(self):

        """
        This function should update the list of empty cells of the grid.
        """
        
        # reset the emptiesSet if the tile is equal to zero append the index into emptiesSet
        self.emptiesSet=[]
        for num in range(self.row*self.col):
            if self.getCell(num)==0:
                self.emptiesSet.append(num)
        
        return self.emptiesSet
    

    def collapsible(self):

        """
        This function should test if the grid of the game is collapsible
        in any direction (left, right, up or down.)

        It should return True if the grid is collapsible.
        It should return False otherwise.
        """
        """
        # check if the grid is collapsible 
        # the tile is not empty and there's no same value tiles beside the tile is uncollapsible tile
        # if the uncollapsible tiles less than the total tiles than the grid is collapsible
        full_grid=0
        for row in range(self.row):
            for col in range(self.col):
                num=self.row*row+col
                if self.getCell(num)!=0:
                    # top left corner
                    if row==0 and col==0:
                        if self.getCell(num)!=self.getCell(num+self.row) and self.getCell(num+self.row)!=0 and self.getCell(num)!=self.getCell(num+1) and self.getCell(num+1)!=0:
                            full_grid+=1
                    # top right corner
                    elif row==0 and col==self.col-1:
                        if self.getCell(num)!=self.getCell(num+self.row) and self.getCell(num+self.row)!=0 and self.getCell(num)!=self.getCell(num-1) and self.getCell(num-1)!=0:
                            full_grid+=1                    
                    # bottom right corner
                    elif row==self.row-1 and col==self.col-1:
                        if self.getCell(num)!=self.getCell(num-self.row) and self.getCell(num-self.row)!=0 and self.getCell(num)!=self.getCell(num-1) and self.getCell(num-1)!=0:
                            full_grid+=1
                    # bottom left corner
                    elif row==self.row-1 and col==0:
                        if self.getCell(num)!=self.getCell(num-self.row) and self.getCell(num-self.row)!=0 and self.getCell(num)!=self.getCell(num+1) and self.getCell(num+1)!=0:
                            full_grid+=1                    
                    # top side
                    elif row==0 and col>0 and col<self.col-1:
                        if self.getCell(num)!=self.getCell(num+self.row) and self.getCell(num+self.row)!=0 and self.getCell(num)!=self.getCell(num+1) and self.getCell(num+1)!=0 and self.getCell(num)!=self.getCell(num-1) and self.getCell(num-1)!=0:
                            full_grid+=1
                    # bottom side
                    elif row==self.row-1 and col>0 and col<self.col-1:
                        if self.getCell(num)!=self.getCell(num-self.row) and self.getCell(num-self.row)!=0 and self.getCell(num)!=self.getCell(num+1) and self.getCell(num+1)!=0 and self.getCell(num)!=self.getCell(num-1) and self.getCell(num-1)!=0:
                            full_grid+=1
                    # left side
                    elif row>0 and row<self.row-1 and col==0:
                        if self.getCell(num)!=self.getCell(num+self.row) and self.getCell(num+self.row)!=0 and self.getCell(num)!=self.getCell(num-self.row) and self.getCell(num-self.row)!=0 and self.getCell(num)!=self.getCell(num+1) and self.getCell(num+1)!=0:
                            full_grid+=1  
                    # right side
                    elif row>0 and row<self.row-1 and col==self.col-1:
                        if self.getCell(num)!=self.getCell(num+self.row) and self.getCell(num+self.row)!=0 and self.getCell(num)!=self.getCell(num-self.row) and self.getCell(num-self.row)!=0 and self.getCell(num)!=self.getCell(num-1) and self.getCell(num-1)!=0:
                            full_grid+=1  
                    # inside the tile
                    else:
                        if self.getCell(num)!=self.getCell(num+self.row) and self.getCell(num+self.row)!=0 and self.getCell(num)!=self.getCell(num-self.row) and self.getCell(num-self.row)!=0 and self.getCell(num)!=self.getCell(num+1) and self.getCell(num+1)!=0 and self.getCell(num)!=self.getCell(num-1) and self.getCell(num-1)!=0 :
                            full_grid+=1
              
        return full_grid < (self.row*self.col) 
        """
        
        #is_true=False
        for index in range(self.row*self.col):
            if self.getCell(index)==0:
                return True       
        for index in range(self.row*self.col):
            # collapsible to move up
            if index>=self.row:    
                if self.getCell(index)==self.getCell(index-self.row):
                    return True 
            # collapsible to move down
            if index<=self.row*self.col-self.row-1:
                if self.getCell(index)==self.getCell(index+self.row):
                    return True 
            # collapsible to move left
            if index!=0 and index!=self.row and index !=2*self.row  and index!=3*self.row:
                if self.getCell(index)==self.getCell(index-1):
                    return True 
            # collapsible to move right
            if index!=self.row-1 and index!=2*self.row-1 and index!=3*self.row-1 and index!=4*self.row-1:
                if self.getCell(index)==self.getCell(index+1):
                    return True 
        return False    
        
        
    def collapseRow(self, lst):
        """
        This function takes a list lst and collapses it to the LEFT.

        This function should return two values:
        1. the collapsed list and
        2. True if the list is collapsed and False otherwise.
        """
       
        orignial_lst=lst[:]
        #left justify the lst
        zero_num=lst.count(0)
        for i in range(zero_num):
            lst.remove(0)
        for x in range(zero_num):
            lst.append(0)
        # if the number have the same value with the next one 
        # turn the is_ture into True and collapse the row
        for index in range(len(lst)-1):
            if lst[index]==lst[index+1] and lst[index]!=0:
                lst[index]=2*lst[index]
                self.score+=int(lst[index])
                lst.pop(index+1)
                lst.append(0)
        is_true= orignial_lst!=lst
        return (lst,is_true)

    
    def collapseLeft(self):
        """
        This function should use collapseRow() to collapse all the rows
        in the grid to the LEFT.

        This function should return True if any row of the grid is collapsed
        and False otherwise.
        """
        collapse_left=False
        total_lst=[]
        new_lst=[]
        # get a copy of whole gird
        for row_num in range(self.row):
            lst=[]
            for col_num in range(self.col):
                num=row_num*self.row+col_num
                item=self.getCell(num)
                lst.append(item)
            total_lst.append(lst)
        # for each row of the grid call the collapseRow to collapse left each row
        for row in total_lst: 
            # get the new row and the collapsible value
            result_row,value=(lambda x : [x[0], x[1]])(self.collapseRow(row))
            new_lst.append(result_row)
            if value:
                collapse_left=True
                
        for row_num in range(self.row):
            for col_num in range(self.col):
                new_num=row_num*self.row+col_num
                new_item=new_lst[row_num][col_num]
                self.setCell(new_num,new_item)                
          
                
        return collapse_left  

    def collapseRight(self):

        """
        This function should use collapseRow() to collapse all the rows
        in the grid to the RIGHT.

        This function should return True if any row of the grid is collapsed
        and False otherwise.
        """
        
        collapse_right=False
        total_lst=[]
        new_lst=[]
        # get an reversed copy of whole gird
        for row_num in range(self.row):
            lst=[]
            for col_num in range(self.col):
                num=row_num*self.row+col_num
                item=self.getCell(num)
                lst.append(item)
            # reverse each row then append to the total list
            lst.reverse()
            total_lst.append(lst)
        # collapse each row to the right
        # for each reversed row of the grid call the collapseRow to collapse left each row
        for row in total_lst:
            # get the new row and the collapsible value
            result_row,value=(lambda x : [x[0], x[1]])(self.collapseRow(row))
            # reverse each row back
            result_row.reverse()  
            new_lst.append(result_row)
            # if any row is collapsible (any value is true) then the whole grid can be collapsed to the right
            if value:
                collapse_right=True
                
        for row_num in range(self.row):
            for col_num in range(self.col):
                new_num=row_num*self.row+col_num
                new_item=new_lst[row_num][col_num]
                self.setCell(new_num,new_item)           
       
                
        return collapse_right          



    def collapseUp(self):

        """
        This function should use collapseRow() to collapse all the columns
        in the grid to UPWARD.

        This function should return True if any column of the grid is
        collapsed and False otherwise.
        """
       
        collapse_up=False
        # create a list to get all the elements in the grid column by column and sorted each column
        total_lst=[]
        new_lst=[]
        for col_num in range(self.col):
            lst=[]
            for row_num in range(self.row):
                num=row_num*self.row+col_num
                item=self.getCell(num)
                lst.append(item)
            total_lst.append(lst)
        # collapse each column up 
        # for each column of the grid call the collapseRow to collapse left each row        
        for col in total_lst:
            # get the new row and the collapsible value
            result_row,value=(lambda x : [x[0], x[1]])(self.collapseRow(col))
            # set each column-row to the new list
            new_lst.append(result_row)
            # if any column-row is collapsible (any value is true) then the whole grid can be collapsed up
            if value:
                collapse_up=True
                
        for col_num in range(self.col):
            for row_num in range(self.row):
                new_num=row_num*self.row+col_num
                new_item=new_lst[col_num][row_num]
                self.setCell(new_num,new_item)
            
       
        return collapse_up          
    
    
    def collapseDown(self):

        """
        This function should use collapseRow() to collapse all the columns
        in the grid to DOWNWARD.

        This function should return True if any column of the grid is
        collapsed and False otherwise.
        """
       
        collapse_down=False
        # create a list to get all the elements in the grid column by column and sorted each column
        total_lst=[]
        new_lst=[]
        for col_num in range(self.col):
            lst=[]
            for row_num in range(self.row):
                num=row_num*self.row+col_num
                item=self.getCell(num)
                lst.append(item)
            # reverse each column
            lst.reverse()
            total_lst.append(lst)
        # collapse each column down
        # for each column-row of the grid call the collapseRow to collapse left each row                
        for col in total_lst:
            # get the new collapswed list and collapsible value
            result_row,value=(lambda x : [x[0], x[1]])(self.collapseRow(col))
            # reverse each column-back
            result_row.reverse()
            # set each column-row to the new list
            new_lst.append(result_row)
            # if any column-row is collapsible (any value is true) then the whole grid can be collapsed down
            if value:
                collapse_down=True
                
        for col_num in range(self.col):
            for row_num in range(self.row):
                new_num=row_num*self.row+col_num
                new_item=new_lst[col_num][row_num]
                self.setCell(new_num,new_item)        
                
        return collapse_down     
    
    
        

class Game():
    def __init__(self, row=4, col=4, initial=2):

        """
        Creates a game grid and begins the game
        """

        self.game = Grid(row, col, initial)
        self.play()


    def printPrompt(self):

        """
        Prints the instructions and the game grid with a move prompt
        """

        if sys.platform == 'win32':
            os.system("cls")
        else:
            os.system("clear")

        print('Press "w", "a", "s", or "d" to move Up, Left, Down or Right respectively.')
        print('Enter "p" to quit.\n')
        self.game.drawGrid()
        print('\nScore: ' + str(self.game.score))


    def play(self):

        moves = {'w' : 'Up',
                 'a' : 'Left',
                 's' : 'Down',
                 'd' : 'Right'}

        stop = False
        collapsible = True

        while not stop and collapsible:
            self.printPrompt()
            key = input('\nEnter a move: ')

            while not key in list(moves.keys()) + ['p']:
                self.printPrompt()
                key = input('\nEnter a move: ')

            if key == 'p':
                stop = True
            else:
                move = getattr(self.game, 'collapse' + moves[key])
                collapsed = move()

                if collapsed:
                    self.game.updateEmptiesSet()
                    self.game.assignRandCell()

                collapsible = self.game.collapsible()

        if not collapsible:
            if sys.platform == 'win32':
                os.system("cls")
            else:
                os.system("clear")
            print()
            self.game.drawGrid()
            print('\nScore: ' + str(self.game.score))
            print('No more legal moves.')


def main():
    game = Game()

main()

