'''
Created on 10/19/2020
@author:   Dylan Tran & Kevin Mamo
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

#Check 0s and 1s in the input string
#convert to binary
#compress("1111100000")=00000001010010100000

def compress(S):
    '''Write a function called compress(S) that takes a binary string S of length 64 as input and
returns another binary string as output. The output binary string should be a run-length encoding
of the input string'''
    return  GetRunhelp(S, 0)

def next_run_length(S):
    '''next run length where the interation is recursively performed to check if the first value matches the 2nd one and so on
    if at any point these matching string segments returns false. Reset. This gives the number of 0s and 1s'''
    def nextRunLengthHelper(S,acc,initial):
        if S=='' or acc==MAX_RUN_LENGTH:
            return acc
            '''if s[0] equals intial, the function would return the next recursive call'''
        if S[0]==initial:
            return nextRunLengthHelper(S[1:],acc+1,S[0])
        else:
            return acc
    return nextRunLengthHelper(S,0,S[0])

def GetRunhelp(S,num):
    ''' for each recursive call where we switch from 0 to 1, we can just keep
        incrementing num, and then check whether that new value it's even or odd. This with the addition of Zeros will return the final output in blocks of 5'''
    if S=='':
        return ''
    elif S[0]==str(num % 2):
        return Zeroes(numToBinary(next_run_length(S)))+GetRunhelp(S[next_run_length(S):], num + 1)
    else:
        return '0'*COMPRESSED_BLOCK_SIZE +GetRunhelp(S, num + 1)
        

def Zeroes(n):
    '''Finds the amount of 0s in the 5 digits that represent binary values, they represent how many 0's and
    then 1's are in the uncompressed string'''
    return '0'*(COMPRESSED_BLOCK_SIZE-len(n)) + n

def uncompress(S):
    '''step 1 every len 5 digits, convert that binary value to number value step 2 covert that value to binary
    step 3 multiply 0 to the front of that binary number and multiply 1 to the value of the other binary number'''
    '''that "inverts" or "undoes" the compressing in your compress function'''
    if S=='':
        return ''
        '''Add the amount of 0s in the first 5 values with amount of 1s in the next 5 and continue recursion for values past'''
    else:
        return '0'*binaryToNum(S[0:5])+'1'*binaryToNum(S[5:10])+uncompress(S[10:])

def compression(S):
    ''' the ratio of the compressed size to the original size for image S.'''
    return len(compress(S))/(len(S))

'''All values of compression are fairly low meaning that it is really not needed as ratio is float around 1'''


'''
 Professor I. Lai from the Pasadena Institute of Technology is Lai-ing since answer will always be >=1 and in binary.
'''


def isOdd(n):
    '''base case is not odd when divisble by 2 and remainder is 0'''
    if n % 2 ==0:
        return False
    else:
        return True




def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n==0:
        return ''
    #Going right to left
    elif isOdd(n):
        return numToBinary(n//2)+'1'
         #if it is odd add the 0 as 2='10' 
    else:
        return numToBinary(n//2)+'0'

def binaryToNum(S):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if S=='' or S== '0':
        return 0
    else:
        '''most significant value times 2 to the power of the 'level' under. Take the first value and recursively add the rest untill string len=0'''
        return binaryToNum(S[1:])+int(S[0])*2**(len(S)-1)
