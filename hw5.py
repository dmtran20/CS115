'''
Created on 10/13/2020
@author:  Dylan Tran
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 5 (Rev. Oct 2020 by D.N.)
'''
import turtle  # Needed for graphics

def sv_tree(trunk_length, levels):
    '''Base case if level==1 it is just a stick and return to your orginial position'''
    if levels==1:
        turtle.forward(trunk_length)
        turtle.forward(-trunk_length)
        return #nothing
    else:
        #go foward and turn cursor left
        turtle.forward(trunk_length)
        turtle.left(30)
        #go half, and ruduce level by 1. Recursion this
        sv_tree(trunk_length*0.5, levels-1)
        #go right and recursively call the tree
        turtle.right(60)
        sv_tree(trunk_length*0.5, levels-1)
        #go back to intial angle in order to go back to "orginial place"
        turtle.left(30)
        turtle.backward(trunk_length)

        
    
        
        

#Returns the nth Lucas number using the memoization technique
    #shown in class and lab. The Lucas numbers are as follows:
    #[2, 1, 3, 4, 7, 11, ...]
def fast_lucas(n):
    memo={}
    def fast_lucashelp(n):
        '''If it is in the stored memo return the value'''
        if (n) in memo:
            return memo[(n)]
        '''Base cases for Lucas numbers shown in the given instructions'''
        if n==0:
            return 2
        if n==1:
            return 1
        else:
            '''Store into memo as each number relies on the previous two values'''
            memo[(n)]=fast_lucashelp(n-1)+fast_lucashelp(n-2)
            answer=memo[(n)]
            return answer
    return fast_lucashelp(n)

    
def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    memo={}
    def fast_change_helper(amount,coins, memo):
        '''Does the job of fast_change_helper, assuming coins is a tuple.'''
        '''If stored in memo return the sotred value '''
        if amount in memo:
            return memo[amount]
        '''Base cases'''
        if amount==0:
            return 0
        if coins==():
            return float('inf')
        '''if the coin is bigger than the amount. Go to the next index'''
        if coins[0]>amount:
            return fast_change_helper(amount,coins[1:],memo)
        else:
            '''if amount is greter than the first term.'''
            use=1+fast_change_helper(amount-coins[0], coins,memo)
            lose=fast_change_helper(amount, coins[1:],memo)
            answer=min(use,lose)
            '''Memoize the minimum values to reduce the repeating patterns'''
            memo[amount]=answer
            return answer
        # Call the helper. Note we converted the list to a tuple.
    return fast_change_helper(amount, tuple(coins),{})

# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))

# Should take a few seconds to draw a tree.
sv_tree(100, 4)
