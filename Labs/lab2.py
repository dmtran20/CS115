'''Dylan Tran'''
'''I pledge my honor that I have abided by the Stevens Honor System'''

def dot(L,K):
#if L is absent return 0
    if not L:
        return 0
#If K is absent return 0
    if not K:
        return 0
    return L[0]*K[0]+dot(L[1:],K[1:])
'''Return the first value of list L multiply first value of list K. '''
'''Add the second value of list L multiply second value of list K'''


def explode(S):
    '''Base statement return []'''
    if S=='':
        return []
    else:
        '''Make a list starting with the intial later and call itself until the end of the string/word'''
        return [S[0]]+explode(S[1:])
    
def ind(e, L):
    '''if the first element appears as the first term L[0] and the base cases'''
    if L==[] or L=='' or L[0]==e:
        return 0
        '''If it is in range of the list, it will return where it is in the list by adding 1 every time.'''
    else:
        return 1+ind(e,L[1:])

def removeAll(e, L):
    '''base case which is when list is empty return empty[]'''
    if L==[]:
        return []
        '''If e== the first term, continue moving along to the next case'''
    if L[0]==e:
        return removeAll(e,L[1:])
        '''If e!= the first term, take first term continue moving along to the next case. Adding the 2nd, 3rd, 4th, etc then cycles to do the process again'''
    else:
        return [L[0]]+ removeAll(e,L[1:]) 

#Given in sheet
def even(L):
    if not L % 2 == 0:
        return False
    else:
        return True

def myFilter(n,L):
    '''Base Statement when list is empty return empty[]'''
    if not L:
        return []
        '''If first term is true when even is the function used for n, take the first term continue moving along to the next case'''
    if n(L[0]):
        return[L[0]]+myFilter(n,L[1:])
        '''If first term is true when even is the function used for n, skip and continue moving along'''
    else:
        return myFilter(n,L[1:])

def listgood(L):
    '''L equals any index in the list L, then the function returns the index of where that list is'''
    return isinstance(L,list)

# if x is a list you want to go back to the deepreverse to reverse that list
#Starting from end, add all the terms
def deepReverse(L):
    '''Base statement for strings'''
    if L==[]:
        return L
    if not listgood(L[0]):
        ''' take every index of a list, and splice it until and add 1 term each time'''
        return deepReverse(L[1:])+[L[0]]
    else:
        '''list is empty or the index contains the value, so every time you go through a ''new'' L[0]'''
        return deepReverse(L[1:])+[deepReverse(L[0])]
    
    
