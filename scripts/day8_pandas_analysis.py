import pandas as pd

df = pd.read_csv("data/sample_prices.csv")

print(df)

#Inspect the data
print("\nColumn Names:")
print(df.columns)

print("\nFirst five rows:")
print(df.head())

#Access price column
prices = df["price"]

print("\nPrices:")
print(prices)

#Built-in Analysis
print("\nAverage Price:", round(prices.mean(), 2))
print("Max price:", prices.max())
print("Min price:", prices.min())

#Add new column
df["daily_change"] = df["price"].diff

print("\nUpdated DataFrame:")
print(df)