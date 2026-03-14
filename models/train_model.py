import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import pickle

# load dataset
data = pd.read_csv("data/stock_data.csv")

# convert Close column to numeric
data["Close"] = pd.to_numeric(data["Close"], errors="coerce")

# remove missing values
data = data.dropna()

# select closing prices
prices = data["Close"]

# train ARIMA model
model = ARIMA(prices, order=(5,1,0))
model_fit = model.fit()

# save model
with open("models/arima_model.pkl", "wb") as f:
    pickle.dump(model_fit, f)

print("Model trained and saved successfully!")