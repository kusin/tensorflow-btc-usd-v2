# lib manipulation data
import numpy as np
import pandas as pd

# lib data preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
# ----------------------------------------------------------------------------------------


# function of feature selection
def feature_selection(dataset, features):
  df = dataset.filter(features)
  df = df.values
  return df
# ----------------------------------------------------------------------------------------

def normalization(dataset):
  scaler = MinMaxScaler(feature_range=(0, 1))
  scaled = scaler.fit_transform(np.array(dataset))
  return scaled
# ----------------------------------------------------------------------------------------

def splitting(dataset, train_size, test_size):
  train_data, test_data = train_test_split(dataset, train_size=train_size, test_size=test_size, shuffle=False)
  return train_data, test_data
# ----------------------------------------------------------------------------------------

# function for supervised learning
def supervised_learning(look_back, dataset):
    
    # declare variable X and Y
    dataX = []
    dataY = []
    
    # for loop for create supervised learning
    for i in range(look_back, len(dataset)):
        
        # insert value X and Y 
        dataX.append(dataset[i-look_back:i, 0])
        dataY.append(dataset[i, 0])
        
    # return value X and Y
    return np.array(dataX), np.array(dataY)
# ----------------------------------------------------------------------------------------
