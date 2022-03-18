def change(amount, coins):
    #3 base cases 
        if amount==0:
            return 0
        if coins==[]:
           return float('inf')
        if amount==coins[0]:
            return 1
            '''if the coin is bigger than the amount. Go to the next index'''
        if coins[0]>amount:
            return change(amount,coins[1:])
        else:
            '''if amount is greter than the first term.'''
            '''In use,these coins can also repeat unlike the example'''
            use=1+change(amount-coins[0], coins)
            lose=change(amount, coins[1:])
            return min(use,lose)


