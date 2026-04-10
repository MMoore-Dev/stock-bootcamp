from utils import analyze_trade

#Use the function
trade = analyze_trade(100, 115, 10)

print("Profit: ", trade["profit"])
print("Percent return: ", round(trade["percent_return"], 2), "%")
print("Result: ", trade["result"])