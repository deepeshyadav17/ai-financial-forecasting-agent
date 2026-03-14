import yfinance as yf
import pandas as pd

# choose stock ticker
ticker = "AAPL"

# download stock data
data = yf.download(ticker, start="2018-01-01", end="2024-01-01")

# save dataset
data.to_csv("data/stock_data.csv")

print("Stock data downloaded successfully!")
print(data.head())