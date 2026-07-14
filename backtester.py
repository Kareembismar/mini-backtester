prices = [100.0, 102.5, 101.0, 105.3, 104.8, 108.2, 107.0]

def moving_average(prices, window):
    ma = []
    for i in range(len(prices) - window + 1):
        chunk = prices[i:i+window]   # slice starting at i, `window` wide
        ma.append(sum(chunk) / len(chunk))                # the average of chunk — sum and len
    return ma

print(moving_average(prices, 3))


def signals(prices, ma, window):
    calls = []
    
    for k in range(len(ma)):
        today = prices[k + window - 1]

        if today>ma[k]:
            calls.append("BUY")
        else:
            calls.append("SELL")

        
    return calls

averages = moving_average(prices, 3)
print(signals(prices, averages, 3))