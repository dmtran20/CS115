'''
Created on 10/8/20
@author:  Dylan Tran
Pledge: I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Lab 5
'''

import time
from cs115 import map

words = []
HITS = 10


def ED(first, second):
    ''' Returns the edit distance between the strings first and second.'''
    if first == '':
        return len(second)
    elif second == '':
        return len(first)
    elif first[0] == second[0]:
        return ED(first[1:], second[1:])
    else:
        substitution = 1 + ED(first[1:], second[1:])
        deletion = 1 + ED(first[1:], second)
        insertion = 1 + ED(first, second[1:])
        return min(substitution, deletion, insertion)

def fastED(first, second):
    '''Returns the edit distance between the strings first and second. Uses
    memoization to speed up the process.'''
    '''create the empty dictionary'''
    memo={}
    def fastEDhelp(first, second):
        '''if the result is already in memo table,look up the value and return memo value''' 
        if (first,second) in memo:
            return memo[(first,second)]
            '''Continuously store into memory table'''
            '''if first is empty'''
        if first == '':
            memo[(first,second)]=len(second)
            return memo[(first,second)]
            '''if second is empty'''
        elif second == '':
            memo[(first,second)]=len(first)
            return memo[(first,second)]
            '''if first and second are the same, remove the first element of each'''
            '''And store in memo'''
        elif first[0] == second[0]:
            answer=fastEDhelp(first[1:], second[1:])
            memo[(first,second)]=answer
            return answer
            '''This will start with recursive calls and look into memo table for their values, so less recursive calls'''
        else:
            substitution = 1 + fastEDhelp(first[1:], second[1:])
            deletion = 1 + fastEDhelp(first[1:], second)
            insertion = 1 + fastEDhelp(first, second[1:])
            answer=min(substitution, deletion, insertion)
            memo[(first,second)]=answer
            return answer
    return fastEDhelp(first, second)

def getSuggestions(user_input):
    '''For each word in the global words list, determine the edit distance of
    the user_input and the word. Return a list of tuples containing the
    (edit distance, word).
    Hint: Use map and lambda, and it's only one line of code!'''
    #return a tuple to find distance every word in the mastery list with our input and the word in the mastery list. Sequence would be the mastery list
    return map(lambda word:[fastED(word,user_input), word],words)

def spam():
    '''Main loop for the program that prompts the user for words to check.
    If the spelling is correct, it tells the user so. Otherwise, it provides up
    to HITS suggestions.

    To exit the loop, just hit Enter at the prompt.'''
    while True:
        user_input = input('spell check> ').strip()
        if user_input == '':
            break
        if user_input in words:
            print('Correct')
        else:
            start_time = time.time()
            suggestions = getSuggestions(user_input)
            suggestions.sort()
            endTime = time.time()
            print('Suggested alternatives:')
            for suggestion in suggestions[:HITS]:
                print(' %s' % suggestion[1])
            print('Computation time:', endTime - start_time, 'seconds')
    print('Bye')

if __name__ == '__main__':
    f = open('3esl.txt')
    for word in f:
        words.append(word.strip())
    f.close()
    spam()
