'''
Created on 10/15/2020
@author:   Dylan Tran
Pledge:   I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Lab 6
'''
def isOdd(n):
    '''base case is not odd when divisble by 2 and remainder is 0'''
    if n % 2 ==0:
        return False
    else:
        return True
#Questions
'''
Complete base-2 representation of the number 42 
32 16 8 4 2 1
1  0  1 0 1 0
'''


'''The least-significant bit for an odd base-10 number would be 1 as the first remainder is 1
While the least-significant bit for an even base-10 number would be 0 as the first remainder is 0
so it would even.


If we have a base-2 number and we eliminate the least-significant bit. The value of the original number would
be undergoing integer division by 2. As binary 1010(10), removing the last 0 would be 101(5). And 1011(11) removing
the last 0 would be 101(5) aswell. So dividing by 2 removing the remainder


In the case that N is even we can use recrsion, but you can simply add 0 at the end as the least significant value get double Y to get N.
With the odd numbers it can be just a simple add 1 instead of 0 as there is a remainder 1 to carry over. 

'''
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

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s=='' or s== '0':
        return 0
    else:
        '''most significant value times 2 to the power of the 'level' under. Take the first value and recursively add the rest untill string len=0'''
        return binaryToNum(s[1:])+int(s[0])*2**(len(s)-1)
    
##Tail recursion version works aswell. Start from the right continuously move along
# binaryToNum(s[:-1])*2+ (s[-1]=='1')


def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    '''Set up a system of equations to find the 1+number value '''
    x=binaryToNum(s) + 1
    y=numToBinary(x)
    #take 8 bits and subtract the len of the binary numbers
    j=8-len(y)
    #Then just add the binary nubers to the end of the string of 0s
    k='0'*j+y
    #base case
    if len(k)>8:
        return '00000000'
    else:
        #call the result k
        return k

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n<0:
        return #nothing
    else:
        '''print orginial then print increments by n times as n approaches 0'''
        print(s)
        count(increment(s), n-1)

'''
The Ternary representation for the value 59 is 2012. The value of the original number would
be undergoing integer division by 3 continuosly and carrying over the remainder. Until the
remainder= a number less than 3, which would be the leas significant digit

'''
def divby3(n):
    if n % 3==0:
        return True
    else:
        return False
def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    '''mod 3 get the remainder'''
    a=n%3
    '''base case'''
    if n==0:
        return ''
        '''if divisble by 3 add str of 0'''
    elif divby3(n):
        return numToTernary(n//3)+str(a)
        '''if divisble by 3 add str of 1 or 2'''
    else:
        return numToTernary(n//3)+str(a)

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s=='' or s== '0':
        return 0
    else:
        '''most significant value times 3 to the power of the 'level' under. Take the first value and recursively add the rest untill string len=0'''
        return ternaryToNum(s[1:])+int(s[0])*3**(len(s)-1)

def foursToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s=='' or s== '0':
        return 0
    else:
        '''most significant value times 3 to the power of the 'level' under. Take the first value and recursively add the rest untill string len=0'''
        return foursToNum(s[1:])+int(s[0])*4**(len(s)-1)
        
