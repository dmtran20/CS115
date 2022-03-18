'''Dylan Tran'''
'''I pledge my honor that I have abided by the Stevens Honor System.'''
from cs115 import *
import math

#given function
def mult(x, y):
    """Returns the product of x and y"""
    return x * y

def factorial (n):
    #0! is 1
    if n == 0:
        return 1
    #Use Reduce to multiply every element to every subsequent element in the range
    else:
        return reduce(mult,range(1,n+1))

def add(x,y):
    return x + y
def mean(L):
    '''Need to add all the values in list to find the numerator value. call add function.'''
    Numerator=reduce(add,L)
    '''Then need to divide by the length of the list to find average'''
    return Numerator/len(L)

#Given function
def divides(n):
    def div(k):
#Returns the result of n divide by k
        return n % k==0
    return div

def ifprime(n):
    '''Takes function divides and returns a list if n is divisable by the numbers between 2 to the number below n'''
    return map(divides(n),(range(2,n-1)))

def prime(n):
    '''need positive integer and 1 is not prime or composite'''
    if n<=1:
        return False
    '''Given That True=1 and False=0'''
    '''Take the total of the map values True and False. Everything ==0 would be prime'''
    if sum(ifprime(n))==0:
        return True
        '''Everything >1 would be composite'''
    elif sum(ifprime(n))>0:
        return False
