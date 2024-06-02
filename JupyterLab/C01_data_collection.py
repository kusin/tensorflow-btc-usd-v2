# lib data manipulation 
import pandas as pd

# function load dataset
def data_collection(df):

  # load dataset
  dataset = pd.read_csv("../dataset/"+df, parse_dates=['Date'])
  dataset = dataset[["Date", "Open", "High", "Low", "Close"]]
  dataset = dataset.set_index("Date")

  # return values
  return dataset

