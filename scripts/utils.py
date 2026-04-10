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

def calculate_average(prices):
    return sum(prices) / len(prices)