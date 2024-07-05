# lib manipulation data
import numpy as np
import pandas as pd

# lib data preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
# ----------------------------------------------------------------------------------------

# function for supervised learning
def create_dataset(look_back, dataset):
    
    # declare variable X and Y
    dataX = []
    dataY = []
    
    # for loop for create supervised learning
    for i in range(look_back, len(dataset)):
        dataX.append(dataset[i-look_back:i, 0])
        dataY.append(dataset[i, 0])
        
    # return value X and Y
    return np.array(dataX), np.array(dataY)
# ----------------------------------------------------------------------------------------

# functions of data preprocessing
def preprocessing(dataset):
  
  # 1. set feature
  data = dataset.filter(['Close'])
  data = data.values

  # 2. normalize features
  scaler = MinMaxScaler(feature_range=(0, 1))
  scaled = scaler.fit_transform(np.array(data).reshape(-1,1))

  # 3. traing testing
  train_data, test_data = train_test_split(scaled, train_size=0.8, test_size=0.2, shuffle=False)

  # 4. supervised learning
  x_train, y_train = create_dataset(60, train_data)
  x_test, y_test = create_dataset(60, test_data)

  # 5. reshape input to be [samples, time steps, features]
  x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
  x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

  # return values
  return scaler, scaled, x_train, y_train, x_test, y_test

# function for inverse normalized
def inverse(scaler, scaled):
  return scaler.inverse_transform(scaled.reshape(-1,1))
# ----------------------------------------------------------------------------------------
