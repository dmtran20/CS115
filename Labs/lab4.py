'''
Created on 10/1/2020
@author:   Dylan Tran
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - lab4
'''

items = [[2, 100], [3, 112], [4, 125]]
#items[0][0]=2

def knapsack(capacity, itemList):
    '''base case'''
    if capacity==0:
        return [0,[]]
    #if the list of list is empty
    if itemList==[] or itemList==[0]:
        return [0,[]]
    '''if items[0][0] is greater than what u can hold. go to next index'''
    if itemList[0][0]>capacity:
        return knapsack(capacity, itemList[1:])

    else: #itemList[0][0]<capacity: if items[0][0] is less than what u can hold. Get that item
        '''use will subtract the first value of items from capacity, and move to the next first value of list [1][0]=3
        lose will just move to the next first value of list [1][0]=3'''
        use=knapsack(capacity-itemList[0][0], itemList[1:])
        lose=knapsack(capacity, itemList[1:])
        usevalue=[itemList[0][1]+use[0], [itemList[0]]+use[1]]
        losevalue=[lose[0],lose[1]]
        #if the value of lose is greater
        if usevalue[0]>losevalue[0]:
            #make list o
            return usevalue
        else:
            '''want to give the min of use and lose. so use would return the largest value''' 
            return losevalue
    
    
