import pickle

# load trained model
with open("models/arima_model.pkl", "rb") as f:
    model = pickle.load(f)

# forecast next day price
prediction = model.forecast(steps=1)

# get first value safely
predicted_price = prediction.iloc[0]

print("Next day predicted price:", predicted_price)