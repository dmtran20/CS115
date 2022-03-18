'''
Created on 10/27/2020
@author:   Dylan Tran
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 7
'''

def numToBaseB(n, b):
    '''Precondition: integer argument is non-negative. Takes as input a non-negative (0 or larger)
integer N and a base B (between 2 and 10 inclusive) and returns a string representing the number N in base B. '''
    '''base case'''
    if n==0:
        return '0'
    else:
        return NumtoBaseBhelp(n,b)
    
def NumtoBaseBhelp(n,b):
    '''helper function for first step'''
    if n==0:
        return ''
    else:
        return NumtoBaseBhelp(n//b,b)+str(n%b)

def baseBToNum(s,b):
    ''' takes as input a string S and a base B where S represents a number in
base B where B is between 2 and 10 inclusive'''
    if s=='' or s== '0':
        return 0
    else:
        '''most significant value times base to the power of the 'level' under. Take the first value and recursively add the rest until string empty'''
        return baseBToNum(s[1:],b)+int(s[0])*b**(len(s)-1)

def baseToBase(B1,B2,SinB1):
    '''takes three inputs: a base B1, a base B2 (both of which are
between 2 and 10, inclusive) and SinB1, which is a string representing a number in
base B1.return a string representing the same number in base B2'''
    if SinB1=='':
        return 0
    else:
        #first get integer in base 10
        a=baseBToNum(SinB1,B1)
        '''Get that integer and convert it into string'''
        b=numToBaseB(a, B2)
        return b
        
def add(S,T):
    '''takes two binary strings S and T as input and returns their sum, also in binary. You can do this by converting the
two binary strings to two base-10 numbers, adding the two numbers, and then converting the resulting
sum back into base 2!'''
    if S=='' or S== '0':
        return T
    if T=='' or T=='0':
        return S
    else:
        '''Convert binary strings to base 10 and add those values'''
        a=baseBToNum(S,2)
        b=baseBToNum(T,2)
        c=a+b
        #Convert that INTEGER value to base 2 numToBaseB(n, b)
        return numToBaseB(c,2)

def addB(S,T):
    '''takes two binary strings S and T as input and returns their sum using only strings'''
    if S=='' or S== '0':
        return T
    elif T=='' or T=='0':
        return S
    #when both last values of the strings are 0 the coloum/result is 0. Recursively call next value.
    elif S[-1]=='0' and T[-1]=='0':
        return addB(S[:-1],T[:-1])+'0'
    #when one string has the value 1 the coulum is 1. Recursively call next value.
    elif S[-1]=='1' and T[-1]=='0':
        return addB(S[:-1],T[:-1])+'1'
    elif S[-1]=='0' and T[-1]=='1':
        return addB(S[:-1],T[:-1])+'1'
    #when both string values are 1 the result is 0. Recursively call the next value set as S and add '0' to it. It will continue carrying that one until both S[-1] and T[-1] equals 0 
    elif S[-1]=='1' and T[-1]=='1':
        return addB(addB(S[:-1],T[:-1]),'1')+'0'

#Full adder was optional way to aproach addb
'''Full Adder way'''
def addC(S,T):
    def addChelper(S,T,C):
        if S=='' and T=='':
            if C==1:
                return C
            else:
                return ''
        else:
            return addCHelper(S[0:-1], T[0:-1],FullAdder[(S[-1],T[-1],carry)][1]+FullAdder[(S[-1],T[-1],carry[0])])
    
# if len(S)>len(T):

#return addChelper(S,T,'0')                                                                           
                                                                                            
                                                                                            



# Each row has (x,y,carry-in) : (sum,carry-out)
FullAdder ={ ('0','0','0') : ('0','0'),
('0','0','1') : ('1','0'),
('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1') }
    
    
