# Basic User Input
file_path = input("Enter path to CSV file (default: data/sample_prices.csv): ")

if file_path == "":
    file_path = "data/sample_prices.csv"

# Load Data

import pandas as pd

df = pd.read_csv(file_path)

# Ask for moving average window

window = input("Enter moving average window (default = 3): ")

if window == "":
    window = 3
else:
    window = int(window)

# Perform Analysis

df["moving_avg"] = df["price"].rolling(window=window).mean()
df["percent_change"] = df["price"].pct_change() * 100

# Display Summary
print("\n---- Analysis Summary ----")
print("Average price: ", round(df["price"].mean(), 2))
print("Max price: ", df["price"].max())
print("Min price: ", df["price"].min())

# Trend Detection
latest_change = df["percent_change"].iloc[-1]

if latest_change > 0:
    print("Latest trend: Up 📈")
elif latest_change < 0:
    print("Latest Trend: DOWN 📉")
else:
    print("Latest Trend: FLAT ⚖️")

# Visualization
import matplotlib.pyplot as plt

plt.plot(df["date"], df["price"], label="price")
plt.plot(df["date"], df["moving_avg"], label=f"MA ({window})")

plt.title("Interactive Stock Analysis")
plt.xlabel("Date")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()