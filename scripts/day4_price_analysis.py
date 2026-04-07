# Day 4 price analysis with loops

# price list
prices = [100, 102, 101, 105, 107, 103, 108]

# loop through the prices
for price in prices:
    print(price)

# find high price
max_price = prices[0]

for price in prices: 
    if price > max_price:
        max_price = price
print("Highest Pirce: ", max_price)

# find low price
min_price = prices[0]

for price in prices:
    if price < min_price:
        min_price = price
print("Lowest Price: ", min_price)

# Calculate average price
total = 0

for price in prices: 
    total += price
average_price = total / len(prices)

print("Average Price: ", round(average_price, 2))