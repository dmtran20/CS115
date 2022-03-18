#
# life.py - Game of Life lab
#
# Name:Dylan Tran
# Pledge:I pledge my honor that I have abided by the Stevens Honor System.
#

import random
import cs115

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [createOneRow(width)] # What do you need to add a whole row here?
    return A

import sys
def printBoard( A ):
    """ this function prints the 2d list-of-lists
 A without spaces (using sys.stdout.write)
 """
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )

def diagonalize(width,height):
    """ creates an empty board and then modifies it
 so that it has a diagonal strip of "on" cells.
 """
    A = createBoard( width, height )

    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def innerCells(w,h):
    ''' returns a 2d array of all live cells - with the value of 1
- except for a one-cell-wide border of empty cells'''
    
    A = createBoard(w, h )
    for row in range(1,h-1):
        for col in range(1,w-1):
            if row != col:
                A[row][col] = 1
            else:
                A[row][col] = 1
    return A

import random
    
def randomCells(w,h):
    ''' returns an array of randomly-assigned 1's
and 0's except that the outer edge of the array is still completely empty'''
    A = createBoard(w, h )
    for row in range(1,h-1):
        for col in range(1,w-1):
            if row != col:
                A[row][col] = random.choice( [0,1] )
            else:
                A[row][col] = random.choice( [0,1] )
    return A

def copy(A):
    ''' take in a 2d array A and it will output a new 2d array of data that has the same
pattern as the input array'''
    B = createBoard(len(A[0]), len(A) )
    for row in range(len(A)):
        for col in range(len(A[0])):
            B[row][col]=A[row][col]
    return B

def innerReverse( A ):
    '''that takes an old 2d array (or "generation") and then
creates a new generation of the same shape and size r, the new generation should be the
"opposite" of A's cells everywhere except on the outer edge'''
    copy(A)
    for row in range(1,len(A)-1):
        for col in range(1,len(A[0])-1):
            if A[row][col] == 1:
                A[row][col] = 0
            else:
                A[row][col] = 1  
    return A

def next_life_generation( A ):
    """ makes a copy of A and then advanced one generation of Conway's game of life within
 the *inner cells* of that copy. The outer edge always stays 0."""
    newA = copy(A)
    for row in range(1,len(A)-1):
        for col in range(1,len(A[0])-1):
            if A[row][col] == 1 and countNeighbors( row, col, A ) < 2:
                newA[row][col] = 0
            elif A[row][col] == 1 and countNeighbors( row, col, A ) > 3:
                newA[row][col] = 0
            elif A[row][col] == 0 and countNeighbors( row, col, A ) == 3:
                newA[row][col] = 1

    return newA
                
'''if A[row][col]==1:
                if NumNeighbors < 2 or NumNeighbors > 3:
                    Board[row][col]= 0
                else:
                    Board[row][col]= 1
                if A[row][col]==0:
                    if NumNeighbors==3:
                        Board[row][col]= 1
                    else:
                        Board[row][col]= 0'''                

def countNeighbors( row, col, A ):
    '''Returns the number of possible neighbors there are'''
    row2=row-1 #goes down x
    row3=row+1 #goes up x
    col2=col-1 #goes down y
    col3=col+1 #goes up y
    directions=[[row2,col],[row2,col2],[row2,col3],[row3,col],[row3,col2],[row3,col3],[row,col2],[row,col3]]
    count=0
    for x in range(len(directions)):
        count=count+A[directions[x][0]][directions[x][1]]
    return count
    

#Hints
'''1. All edge cells stay zero (0) (but see the extra challenges, below) #check
2. A cell that has fewer than two live neighbors dies (because of loneliness)#no diagonals
3. A cell that has more than 3 live neighbors dies (because of over-crowding) #next life
4. A cell that is dead and has exactly 3 live neighbors comes to life #next life mext
5. All other cells maintain their state'''
    
    
