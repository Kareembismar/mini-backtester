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

def simulate(prices, calls, window, starting_cash):
    cash = starting_cash
    shares = 0.0
    for k in range(len(calls)):
        today_price = prices[k + window - 1]  
        call = calls[k] # same alignment as signals!

        if call == "BUY" and cash > 0:
            shares = cash / today_price
            cash = 0 
        if call == "SELL" and shares>0: 
            cash = shares * today_price
            shares = 0

    if shares > 0:
        cash = shares * prices[-1]

    return cash

averages = moving_average(prices, 3)
print(signals(prices, averages, 3))


final = simulate(prices, signals(prices, averages, 3), 3, 1000.0)
print(f"Final: ${final:.2f}")

