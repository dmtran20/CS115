#Dylan Tran
#I pledge my honor that I have abided be the Stevens Honor System
from cs115 import *
from cs115 import map
from cs115 import map, reduce
import math

def inverse(x):
    '''Returns inverse input x: a number'''
    return 1/x


#def e(n):
    #return 1/math.factorial(n)

'''Now we need to add these together with the list feature presented in the dbl example'''

'''define function of Taylor Series'''
def TS(x):
    return 1/math.factorial(x)

'''This is the lists and need 2, one for the iterable and one to start'''

def e(n):
    list1=range(0,n+1)
    list2=map(TS, list1)
    answer=sum(list2)
    return answer

'''Use subtraction to find the error and use absolute value to make error always positive '''
'''use large number like e(100) to get the closest value of e'''
def error(n):
    return abs(e(n)-e(100))
