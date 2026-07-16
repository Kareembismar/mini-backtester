Calls = ['SELL', 'BUY', 'BUY', 'BUY', 'BUY']


def count_buys(calls):
    count = 0
    for c in calls:
        if c == "BUY":
            count += 1
    return count 
    
def count_sells(Puts):
    count = 0
    for c in Puts:  
        if c == "SELL":
            count +=1
    return count
    
print(count_buys(Calls))
print(count_sells(Calls)) 