import random


def moving_average(prices, window):
    ma = []
    for i in range(len(prices) - window + 1):
        chunk = prices[i:i+window]   
        ma.append(sum(chunk) / len(chunk))                
    return ma

def random_prices(days, start):
    basket = [start] 
    for i in range(days-1): 
        yesterday = basket[-1]
        move = random.uniform(-0.03, 0.03)
        basket.append(yesterday * (1+move))
    return basket

def signals(prices, ma, window):
    calls = []
    
    for k in range(len(ma)):
        today = prices[k + window - 1]

        if today>ma[k]:
            calls.append("BUY")
        else:
            calls.append("SELL")

        
    return calls

def simulate(prices, calls, window, starting_cash, fee):
    cash = starting_cash
    shares = 0.0
    trades = 0                           
    for k in range(len(calls)):
        today_price = prices[k + window - 1]
        call = calls[k]

        if call == "BUY" and cash > 0:
            shares = (cash * (1-fee)) / today_price
            cash = 0
            trades += 1                     
        if call == "SELL" and shares > 0:
            cash = ((shares * today_price) * (1-fee))
            shares = 0
            trades += 1                     
    if shares > 0:
        cash = ((shares * prices[-1])*(1-fee))

    return cash, trades                    

def tournament(runs):
    total_clean = 0.0
    total_fees = 0.0
    fee_taxed = 0.001
    for r in range(runs):
        prices = random_prices(100, 100.0)
        averages = moving_average(prices, 3)
        calls = signals(prices, averages, 3)
        final_clean, t1 = simulate(prices, calls, 3, 1000.0, 0.0)
        final_fees, t2 = simulate(prices, calls, 3, 1000.0, fee_taxed)
        total_clean += final_clean
        total_fees += final_fees
    print(f"Avg finish (no fees):   ${total_clean / runs:.2f}")
    print(f"Avg finish (0.1% fee):  ${total_fees / runs:.2f}")
    print(f"Fee drag per run:       ${(total_clean - total_fees) / runs:.2f}")

tournament(50)

prices = random_prices(100, 100.0)
averages = moving_average(prices, 3)

calls = signals(prices, averages, 3)
fee = 0.001
final, trades = simulate(prices, calls, 3, 1000.0, fee)
print(f"Final: ${final:.2f} ({trades} trades)")

