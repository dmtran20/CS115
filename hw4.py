
'''Dylan Tran
I pledge my honor that I have abided by the Stevens Honor System.
10/7/20

'''

def pascal_row(x):
    '''Base Case. row 0 is [1] according to the pascal triangle'''
    if x==0:
        return [1]
        '''add the first value of [1] +calling the pascal row inside for the inner values and the last value of the [1]'''
    else:
        return pascal_row(0)+pascalrow_inside(pascal_row(x-1))+pascal_row(0)

def pascalrow_inside(x):
    '''x=each row. base case if row is empty'''
    if x==[]:
        return []
    '''base case the len is 1 is a base case'''
    if len(x)==1:
        return []
    else:
        '''[return the first value plus the next value]+[next value plus the third value] until it hits length of 1 for the row to stop'''
        return [x[0]+x[1]]+pascalrow_inside(x[1:])


def pascal_triangle(n):
    '''Returns the base case of one block of n==0.'''
    if n == 0:
        return [[1]]
    else:
        '''Recursively call function and add each previous row in a pascal triangle until the end '''
        return pascal_triangle(n-1)+[pascal_row(n)]
'''
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
'''

def test_pascal_row():
    assert pascal_row(0)==[1]
    assert pascal_row(1)==[1,1]
    assert pascal_row(2)==[1,2,1]
    assert pascal_row(4)==[1, 4, 6, 4, 1]
    assert pascal_row(5)==[1, 5, 10, 10, 5, 1]

def test_pascal_triangle():
    assert pascal_triangle(0)==[[1]]
    assert pascal_triangle(1)==[[1], [1, 1]]
    assert pascal_triangle(2)==[[1], [1, 1], [1, 2, 1]]
    assert pascal_triangle(4)==[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert pascal_triangle(5)==[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1],[1, 5, 10, 10, 5, 1]]
