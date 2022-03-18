'''
Created on 9/21/20
@author:   Dylan Tran and Serena Lee
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 2
'''
import sys
from cs115 import map, reduce, filter
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.
#def scorelist(character,value):

def letterScore(letter,scorelist):
    #if there is no letter return 0 for 0 points base statement
    if letter=='':
        return 0
    #That scrabblescores list 1 value 1[] and value 2[]
    elif letter==scorelist[0][0]:
        return scorelist[0][1]
    else:
        return letterScore(letter,scorelist[1:])
    
def wordScore(S, scorelist):
    if S=='':
        return 0
    #S[0]==a return 1
    else:
        return letterScore(S[0],scorelist)+wordScore(S[1:],scorelist)

#from lab2 Recusion Muscles Remove concept
def removeFirst(let, Rack):
    '''Base Case'''
    if Rack == []:
        return []
    """Removes first case of a letter from the Rack. Takes the next value in that index/skipping the orginal"""
    if let == Rack[0]:
        return Rack[1:]
    """Add the first value and continues"""
    return [Rack[0]] + removeFirst(let, Rack[1:])

def createWord(Rack):
    """Determines if the inputted Rack can form words in the dictionary. Returns True if possible, false if not"""
    def createWord_help(dict): 
        """Helper function which uses filter(Rack, Dictionary) -> calls createWord"""
        def help2(Rack, dict):
            """Recursive function for Rack and dict where dict is list"""
            if dict == '':
                return True
            '''If first value of dict call remove'''
            if dict[0] in Rack:
                return help2(removeFirst(dict[0], Rack), dict[1:])
            return False
        return help2(Rack, dict)
    return createWord_help


def useWordScore(w):
    """Uses wordScore to create a list of words and its associated values from the input"""
    if w == '':
        return ['', 0]
        '''Else return the total score'''
    else:
        return [w] + [wordScore(w, scrabbleScores)]

def scoreList(Rack):
    """Finds the words that can be created from the inputted string and returns it as a list and score"""
    return map(useWordScore, filter(createWord(Rack), Dictionary))

def compare(a,b):
    """Compares two values and returns the highest score"""
    if a[1] > b[1]:
        return a
    elif b[1] > a[1]:
        return b

def bestWord(Rack):
    """Takes the highest value of the output for function scoreList calling compare"""
    if scoreList(Rack) == []:
        return ['',0]
    return reduce(compare, scoreList(Rack))
    


        
