# lib data manipulation 
import pandas as pd
import numpy as np

# function load dataset
def load_csv(df):

  # load dataset
  dataset = pd.read_csv("dataset/"+df, parse_dates=['Date'])

  # chose features
  dataset = dataset[["Date", "Open", "High", "Low", "Close"]]

  # set index
  dataset = dataset.set_index("Date")

  return dataset

