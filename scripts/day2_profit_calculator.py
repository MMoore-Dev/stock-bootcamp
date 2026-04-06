buy_price = 100
sell_price = 115
shares = 10

total_cost = buy_price * shares
total_value = sell_price * shares
profit = total_value - total_cost
percent_return = (profit/total_cost) * 100

print("-----Trade Summary-----")
print("Total Cost:", total_cost)
print("Total Value:", total_value)
print("Profit/Loss", profit)
print("Percent Return", round(percent_return, 2), "%")

#Decision logic
if profit > 0:
    print("Result: PROFIT")
elif profit < 0:
    print("Result: LOSS")
else:
    print("Result: BREAK-EVEN")