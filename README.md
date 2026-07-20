# Mini Stock Backtester

A tiny stock trading backtester built from scratch in Python — no libraries, no frameworks, just the logic. It generates fake price data, runs a simple momentum strategy over it, and measures whether that strategy actually makes money once you account for trading fees.

## Features

- **Random-walk price generator** — builds a synthetic 100-day price series where each day moves ±3% from the last.
- **Moving average** — computes a rolling N-day average over the price series.
- **Buy/sell signal engine** — BUY when price is above its moving average, SELL when below (a classic 3-day momentum rule).
- **P&L simulation with fees** — walks the signals day by day, moving cash in and out of shares, and charges a configurable per-trade fee.
- **50-run tournament** — replays the whole strategy across 50 fresh random markets and reports the average result.
- **Controlled fee comparison** — runs each market *twice* on identical signals (0% fee vs. 0.1% fee) so the only variable is the fee itself.

## Key result 🔥

I tested a **3-day moving-average momentum strategy** across **50 random 100-day markets**, starting each run with $1,000.

A **0.1% per-trade fee flipped the strategy from ~+$23 average profit to ~−$15 average loss** — about **$37.79 of fee drag** per run. The fee alone turned a break-even strategy into a losing one.

One honest caveat: on random-walk data, **no strategy has a real edge** — prices are pure noise, so any "profit" without fees is luck averaging out toward zero. That's exactly what makes this useful: the tool correctly shows the strategy has no edge, *and* it quantifies precisely how much the fee costs. Measuring the fee damage is the whole point.

## How to run

```bash
python backtester.py
```

It prints the tournament summary plus one sample run:

```
Avg finish (no fees):   $1023.xx
Avg finish (0.1% fee):  $985.xx
Fee drag per run:       $37.79
Final: $9xx.xx (N trades)
```

(Numbers vary each run since the price data is randomly generated.)

## Built as part of

Summer CS prep — self-taught, week 2 of 7.
