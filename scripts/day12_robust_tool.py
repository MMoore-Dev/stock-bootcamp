import pandas as pd

# Safe file loading
file_path = input("Enter CSV file path (default: data/sample_prices.csv): ")

if file_path == "":
    file_path = "data/sample_prices.csv"

try:
    df = pd.read_csv(file_path)
except FileNotFoundError: 
    print("ERROR: File not found. Using deafult file.")
    df = pd.read_csv("data/sample_prices.csv")

# Validate columns
if "price" not in df.columns:
    print("ERROR: 'price' column not found in file")
    exit()

# Safe input for window
window_input = input("Enter moving average window (default 3): ")

try:
    window = int(window_input)
except:
    print("Invalid input. Using default window = 3")
    window = 3

# Prevent division / data errors
df["percent_change"] = df["price"].pct_change() * 100
df["moving_average"] = df["price"].rolling(window=window).mean()
df = df.dropna()

# Safe trend detection
try:
    latest_change = df["percent_change"].iloc[-1]

    if latest_change > 0:
        print("Latest Trend: UP 📈")
    elif latest_change < 0:
        print("Latest Trend: DOWN 📉")
    else:
        print("Latest Trend: FLAT ⚖️")
except:
    print("Not enough data to determine trend.")

# Visualization
import matplotlib.pyplot as plt

plt.plot(df["date"], df["price"], label="Price")
plt.plot(df["date"], df["moving_average"], label=f"MA ({window})")

plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()