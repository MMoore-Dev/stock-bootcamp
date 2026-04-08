# create the function
def calculate_profit(buy_price, sell_price, shares):
    total_cost = buy_price * shares
    total_value = sell_price * shares
    profit = total_value - total_cost
    return profit

# Call the function
profit = calculate_profit(100, 115, 10)
print("Profit: ", profit)

# Analyze trade function
def analyze_trade(buy_price, sell_price, shares):
    total_cost = buy_price * shares
    total_value = sell_price * shares
    profit = total_value - total_cost
    percent_return = (profit / total_cost) * 100

    if profit > 0:
        result = "PROFIT"
    elif profit < 0:
        result = "LOSS"
    else:
        result = "BREAK-EVEN"

    return {
        "profit": profit,
        "percent_return": percent_return,
        "result": result
    } 

#Use the function
trade = analyze_trade(100, 115, 10)

print("Profit: ", trade["profit"])
print("Percent return: ", round(trade["percent_return"], 2), "%")
print("Result: ", trade["result"])

# Test for multiple trades
trades = [(100, 115, 10), (50, 40, 20), (30, 30, 15)]

for trade in trades: 
    result_data = analyze_trade(*trade)
    print("\nTrade: ", trade)
    print("Profit: ", result_data["profit"])
    print("Percent: ", round(result_data["percent_return"], 2), "%")
    print("Result: ", result_data["result"])
