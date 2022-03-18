'''
Created on 9/28/2020
@author:   Dylan Tran
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from cs115 import *

'''return and edit the list coin between recursions'''

def giveChange(amount,coins):
    #base case, want to return two lists.
    if amount==0:
        return [0,[]]
    #if there is no coins, return infinity 
    if coins==[]:
       return [float('inf'),[]]
    '''when the coin amount is larger, go to the next index'''
    if coins[0]>amount:
        return giveChange(amount,coins[1:])
    else:
        '''use and lose function and start coins at 0 as result can be multiple of a single value. For example[5,5]'''
        useit=giveChange(amount-coins[0],coins[0:])
        loseit=giveChange(amount,coins[1:])
        '''Add 1 to useit[0] to get the number of coins. '''
        if useit[0]<loseit[0]:
            return [1+useit[0],useit[1]+[coins[0]]]
        else:
            '''want to give the 'min' of use and lose. so returning loseit would provide the list with the fewest numbers'''
            return loseit

#Some test cases i made
def testgiveChange():
    assert((giveChange(35, [1, 3, 16, 30, 50])==[3, [16, 16, 3]]))
    assert ((giveChange(0, [1,5,10,25]))==[0, []])
    assert((giveChange(10, []))==[float('inf'), []])
    assert((giveChange(5, [1, 5, 10, 25]))==[1, [5]])
    assert((giveChange(48, [1, 7, 24, 42]))==[2, [24, 24]])
    assert((giveChange(48, [1, 5, 10, 25, 50]))==[6, [25, 10, 10, 1, 1, 1]])
    

# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''' '''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#letterscore and wordScore from hw2
def letterScore(letter,scores):
    #if there is no letter return 0 for 0 points base statement
    if letter=='':
        return 0
    #That scrabblescores list 1 value 1[] and value 2[]
    elif letter==scores[0][0]:
        return scores[0][1]
    else:
        return letterScore(letter,scores[1:])
def wordScore(S, scores):
    if S=='':
        return 0
    #S[0]==a return 1
    else:
        return letterScore(S[0],scores)+wordScore(S[1:],scores)

def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.
    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    '''base case for empty list'''
    if dct==[]:
        return []
    else:
        '''[First value of the list]+[the value from wordscore]. Then recursively add the rest of values in the list starting with index 1.'''
        return [[dct[0]]+[wordScore(dct[0],scores)]]+wordsWithScore(dct[1:], scores)
    #map(lambda x:[x,wordScore(x,scrabbleScores)],dct) works aswell the same way

#test function.
def testwordsWithScore():
    assert (wordsWithScore(Dictionary, scrabbleScores)==[['a', 1], ['am', 4], ['at', 2], ['apple', 9], ['bat', 5], ['bar', 5], ['babble', 12], ['can', 5], ['foo', 6], ['spam', 8], ['spammy', 15], ['zzyzva', 39]])
    




'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
' (Notice that you cannot assume anything about the length of the list.)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n], assuming L is a list and n is at least 0.'''
    #base cases empty list
    if L==[]:
        return []
    #if first value equal n return a empty list as we want to stop at value n(not including n)
    if L[0]==n:
        return []
    else:
        #first element of list and recursively use take
        return [L[0]]+take(n,L[1:])

#test function not sure if we need them but just included it.

def testtake():
    assert (take(3,[1,2,3,4,5,6,7,8,9])==[1, 2])



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:], assuming L is a list and n is at least 0.'''
    #base cases empty list
    if L==[]:
        return []
    #if first value equal n return that value and go to the next value
    if L[0]==n:
        return [L[0]]+L[1:]
    #return empty list and recursively add the function drop until L[0]==n
    else:
        return []+drop(n,L[1:])

def testdrop():
    assert (drop(3,[1,2,3,4,5,6,7,8,9])==[3, 4, 5, 6, 7, 8, 9])
    

