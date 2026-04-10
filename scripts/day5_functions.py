from utils import analyze_trade, calculate_average

#Use the function
trade = analyze_trade(100, 115, 10)

print("Profit: ", trade["profit"])
print("Percent return: ", round(trade["percent_return"], 2), "%")
print("Result: ", trade["result"])

prices = [100,105,108,110,106,101]

#call the calculate average function
average_price = calculate_average(prices)
print("Average price: ", round(average_price, 2))
