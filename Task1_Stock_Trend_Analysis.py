
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
sns.set(style="darkgrid")

# Step 1: Load stock data
ticker = "AAPL"  # You can replace with any other stock symbol like "TSLA", "INFY.NS"
data = yf.download(ticker, start="2020-01-01", end="2025-01-01")

# Step 2: Calculate indicators
data["MA20"] = data["Close"].rolling(window=20).mean()
data["MA50"] = data["Close"].rolling(window=50).mean()
data["Daily Return"] = data["Close"].pct_change()
data["Volatility"] = data["Daily Return"].rolling(window=20).std()

# Step 3: Plot Close Price + Moving Averages
plt.figure(figsize=(14,6))
plt.plot(data["Close"], label="Close Price")
plt.plot(data["MA20"], label="20-Day MA", linestyle='--')
plt.plot(data["MA50"], label="50-Day MA", linestyle='--')
plt.title("Stock Price with Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()

# Step 4: Plot Daily Return
plt.figure(figsize=(14,4))
plt.plot(data["Daily Return"], label="Daily Return", color='orange')
plt.title("Daily Return")
plt.xlabel("Date")
plt.ylabel("Return")
plt.legend()
plt.show()

# Step 5: Plot Volatility
plt.figure(figsize=(14,4))
plt.plot(data["Volatility"], label="Volatility", color="red")
plt.title("Rolling Volatility (20-day)")
plt.xlabel("Date")
plt.ylabel("Volatility")
plt.legend()
plt.show()
