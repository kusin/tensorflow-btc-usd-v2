import pandas as pd
import yfinance as yf

# func get crypto
@staticmethod
def getData(ticker, startDate, endDate):

  # set the ticker and datetime
  dataset = ticker.history(start=startDate, end=endDate).reset_index()

  # set the feature
  dataset = dataset[["Date", "Open", "High", "Low", "Close"]]
  dataset["Date"] = pd.to_datetime(dataset["Date"]).dt.date
  
  # return values
  return dataset