import csv
from utils import calculate_average

prices = []

with open("data/sample_prices.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader: 
        prices.append(float(row["price"]))

print("Prices: ", prices)

average_price = calculate_average(prices)
print("Max Price:", max(prices))
print("Min Price:", min(prices))
print("Average price: ", round(average_price, 2))