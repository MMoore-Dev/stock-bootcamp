import pandas as pd
import matplotlib.pyplot as plt

# --- Load Data with Pandas ---
df = pd.read_csv("data/sample_prices.csv")

# --- Basic Line Chart ---
df["daily_change"] = df["price"].diff()
df["moving_average"] = df["price"].rolling(window=3).mean()

plt.plot(df["date"], df["price"])
plt.plot(df["date"], df["daily_change"])
plt.plot(df["date"], df["moving_average"])
plt.title("Stock Price Over Time")
plt.xlabel("Date")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()