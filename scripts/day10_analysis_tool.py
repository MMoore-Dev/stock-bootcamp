import pandas as pd
import matplotlib.pyplot as plt 
from utils import calculate_average

# Load Data
df = pd.read_csv("data/sample_prices.csv")

prices = df["price"]

# Core Analysis
average_price = calculate_average(prices)
max_price = prices.max()
min_price = prices.min()

# Add derived metrics
df["daily_change"] = df["price"].diff()
df["percent_change"] = df["price"].pct_change() * 100
df["moving_avg"] = df["price"].rolling(window=3).mean()

# Summary Report
print("----- Stock Analysis Report -----")
print("Average Price:", round(average_price, 2))
print("Max Price:", max_price)
print("Min Price:", min_price)

# Visualization
plt.plot(df["date"], df["price"], label="Price")
plt.plot(df["date"], df["moving_avg"], label="Moving Avg")

plt.title("Stock Price Analysis")
plt.xlabel("Date")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

