'''
Dylan Tran and Serena Lee
I pledge my honor that I have abided by the Stevens Honor System.
Connect 4 Homework
'''

class Board(object):
    
    def __init__(self, width=7, height=6):
        self.width= width
        self.height= height
        self.board=[]
        for row in range(self.height):
            self.board.append([])
            for col in range(self.width):
                self.board[row].append(' ')
                
    def __str__(self):
        board = ''
        for row in range(self.height):
            board+='|'
            for col in range(self.width):
                board+= self.board[row][col]+'|'
            board+= '\n'
        
        board+= '-'*(self.width*2+1) +'\n'
        for element in range(0,self.width):
            board= board+ ' ' + str(element)
        return board
    
    def allowsMove(self, col):
        '''can allow a move into column c (because there is space available). It returns False if c does not have space available or if it is not a valid column.
'''
        '''Check if the coloum is not in the width then you can not make a move'''
        if col not in range(self.width):
            return False
        '''Check if the cell is empty if its empty return true'''
        for row in range(0,self.height):
            if self.board[row][col] == ' ':
                return True
                '''If its not in any of them then return false'''
        return False  
             

    def addMove(self, col, ox):
        '''The method should check ox check we should check from the bottom up'''
        if self.allowsMove(col)== True:
            BottomTop=list(range(self.height))
            BottomTop.reverse()
            for row in BottomTop:
                if self.board[row][col] == ' ':
                    self.board[row][col]=ox
                    break
            

    def delMove(self,col):
        '''This method should return True if the given checker, 'X' or 'O', held
in ox, has won the calling Board. It should return False otherwise'''
        for row in range(0, self.height):
            if self.board[row][col] != ' ':
                self.board[row][col] = ' '
                return #nothing
                
            

    def winsFor(self, ox):
        '''Check for vertical 4 in a row'''
        for row in range (self.height-3):
            for col in range(self.width):
                if self.board[row][col]==ox and self.board[row+1][col]==ox and self.board[row+2][col]==ox and self.board[row+3][col]==ox:
                    return True
                    '''Check for horizontal 4 in a row'''
        for row in range (self.height):
            for col in range(self.width-3):
                if self.board[row][col]==ox and self.board[row][col+1]==ox and self.board[row][col+2]==ox and self.board[row][col+3]==ox:
                    return True
                    '''Diagonal one way. Stairs downwards'''
        for row in range(self.height):
            for col in range(self.width):
                if((col+3) < self.width) and ((row+3) < self.height):
                    if self.board[row][col]==ox and self.board[row+1][col+1]==ox and self.board[row+2][col+2]==ox and self.board[row+3][col+3]==ox:
                        return True
                    '''Diagonal other way'''
        for row in range(self.height):
            for col in range(self.width):
                if((col+3) < self.width) and ((row+3) >= 0):
                    if self.board[row][col]==ox and self.board[row-1][col+1]==ox and self.board[row-2][col+2]==ox and self.board[row-3][col+3]==ox:
                        return True
        return False

    def setBoard( self, moveString ):
        """ takes in a string of columns and places alternating checkers in those columns, starting with 'X'
For example, call b.setBoard('012345') to see 'X's and 'O's alternate on the bottom row, or b.setBoard('000000') to
see them alternate in the left column. moveString must be a string of integers."""
        nextCh = 'X' # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
        if nextCh == 'X': nextCh = 'O'
        else: nextCh = 'X'

    def hostGame(self):
        print('Connect 4!')
        Player='O' #first is X
        '''When nobody wins keep playing switch player'''
        count = 0
        boardSize = self.width*self.height
        while (self.winsFor('X')==False and self.winsFor('O')==False) and (count <= boardSize):
            '''from set board'''
            if Player == 'X':
                Player = 'O'
            else:
                Player = 'X'   
            print(self)
            turn=int(input(Player+ "'s "+ 'choice:')) #Get option
            while (self.allowsMove(turn)==False) and (count < boardSize):
                turn=int(input('Invalid choice.' +Player+ "'s choice:"))
            self.addMove(turn,Player)
            count += 1
        print(self)       
        if self.winsFor('X')==True:
            print('X wins -- Congratulations!')
            return
        if self.winsFor('O') == True:
            print('O wins -- Congratulations!')
            return
        else:
            print("Draw -- No one wins!")
            return
        
                
                
            

b = Board( 7, 6 )
b.hostGame()

