# Day 5: Analyze trade function
from utils import analyze_trade

def calculate_profit(buy_price, sell_price, shares):
    total_cost = buy_price * shares
    total_value = sell_price * shares
    profit = total_value - total_cost
    return profit

# --- Single Trade Test ---
trade = analyze_trade(100, 110, 10)

print("Single Trade:")
print("Profit:", trade["profit"])
print("Percent Return:", round(trade["percent_return"], 2), "%")
print("Result:", trade["result"])


# --- Multiple Trades Test ---
trades = [
    (100, 115, 10),
    (50, 45, 20),
    (30, 30, 15)
]

print("\nMultiple Trades:")

for trade in trades:
    result_data = analyze_trade(*trade)

    print("\nTrade:", trade)
    print("Profit:", result_data["profit"])
    print("Percent:", round(result_data["percent_return"], 2), "%")
    print("Result:", result_data["result"])