def main():
    playing_game=True
    player_x='x'
    player_o='o'
    player_turn=player_x
    myBoard=TicTacToe()
    myBoard.drawBoard()
    while playing_game:
        # if the board is not full
        if not myBoard.boardFull():
            # player enter the cell
            print('It is the turn for %s . What is your move?'%player_turn)
            cell=input('enter the cell: ')
            cell=int(cell)
            # if the cell is not valid enter again
            while not myBoard.cellIsEmpty(cell):
                if cell<1 or cell>10:
                    print('Please enter a valid integer lager than 0 less than 10')
                else:
                    print('This place has been occupied, please choose another one.')
                print('It is the turn for %s . What is your move?'%player_turn)
                cell=input('enter the cell: ')
                cell=int(cell) 
            # if the player enters the valid cell
            if myBoard.cellIsEmpty(cell):
                # assign the symbol/letter to the position cell of the grid
                myBoard.assignMove(cell,player_turn)
                # draw the board
                myBoard.drawBoard() 
                winner=myBoard.whoWon()
                # if there is a win
                if winner!='':
                    print('%s wins. Congrats!'%winner)
                    playing_game=False
            # change the player turn
            if player_turn==player_x:
                player_turn=player_o
            else:
                player_turn=player_x
        # if the board is full
        else:
            winner=myBoard.whoWon()
            # if there is a win
            if winner!='':
                print('%s wins. Congrats!'%winner)
                playing_game=False
            # if there is a tie
            else:
                print("It's a tie.")
                playing_game=False
                    
    
class TicTacToe:
    def __init__(self):
        # "board" is a list of 10 strings representing the board (ignore index 0)
        self.board = [" "]*10
        self.board[0]="#"
        #self.board=['#', 'x','o','x','o','o','x','x','x','o']
        
#------------------------------------------------------------- 
    def drawBoard(self):
        # This method prints out the board with current plays adjacent to a board with index.
        index=len(self.board)-1
        while index>0:
            pattern=' '+str(self.board[index-2])+' | '+str(self.board[index-1])+' | '+str(self.board[index])
            numbers=' '+str(index-2)+' | '+str(index-1)+' | '+str(index)
            print(pattern,'\t'+numbers)
            index=index-3
            if index>1:
                print('-----------\t-----------')
       
#write some code here

#------------------------------------------------------------- 
    def boardFull(self):
        # This method checks if the board is already full and returns True. Returns false otherwise
        t=0
        for item in self.board:
            if item!=self.board[0] and item!=" ":
                t=t+1
        return t==9
#write some code here

#------------------------------------------------------------- 
    def cellIsEmpty(self, cell):
        #check whether a given cell is available
        ifEmpty=False
        if cell>0 and cell<10:
            if self.board[cell]==" ":
                ifEmpty=True
            else:
                ifEmpty=False
        else:
            ifEmpty=False
        return ifEmpty
#write some code here

#------------------------------------------------------------- 
    def assignMove(self, cell,ch):
        # assigns the cell of the board to the character ch
        self.board[cell]=ch
#write some code here

#------------------------------------------------------------- 
    def whoWon(self):
    # returns the symbol of the player who won if there is a winner, otherwise it returns an empty string. 
        if self.isWinner("x"):
            return "x"
        elif self.isWinner("o"):
            return "o"
        else:
            return ""

#------------------------------------------------------------- 
    def is_row_win(self,ch):
        # -check if there is a row win
        is_win=False
        index=1
        while index<10:
            if self.board[index]==self.board[index+1]==self.board[index+2]==ch:
                is_win=True
            index=index+3
        return is_win
    def is_column_win(self,ch):
        # -check if there is a column win
        is_win=False
        index=1
        while index<3:
            if self.board[index]==self.board[index+3]==self.board[index+6]==ch:
                is_win=True
            index=index+1
        return is_win
    def is_diagonal_win(self,ch):
        # -check if there is a diagonal win
        is_win=False
        if self.board[1]==self.board[5]==self.board[9]==ch or self.board[3]==self.board[5]==self.board[7]==ch:
            is_win=True
        return is_win
    def isWinner(self, ch):
        # Given a player's letter, this method returns True if that player has won.
        if self.is_row_win(ch) or self.is_column_win(ch) or self.is_diagonal_win(ch):
            return True
    

#write some code here

main()