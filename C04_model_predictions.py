# lib neural network algorithms
import tensorflow as tf
from keras.layers import LSTM
from keras.layers import GRU

# lib evaluate models
from math import sqrt
import scipy.stats as sc
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error

# libs manipulations array
import numpy as np
# ----------------------------------------------------------------------------------------

# func model predictions
def get_models(algorithm, x_train, y_train, x_test, y_test):

  # 1. The LSTM architecture
  if algorithm == "SBi-LSTM":
    tf.keras.backend.clear_session()
    model = tf.keras.Sequential([
      tf.keras.layers.Bidirectional(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1))),
      tf.keras.layers.Bidirectional(LSTM(units=50, return_sequences=False)),
      tf.keras.layers.Dropout(0.05),
      tf.keras.layers.Dense(1)
    ])
  
  # 2. The GRU-RNN architecture
  if algorithm == "SBi-GRU":
    tf.keras.backend.clear_session()
    model = tf.keras.Sequential([
      tf.keras.layers.Bidirectional(GRU(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1))),
      tf.keras.layers.Bidirectional(GRU(units=50, return_sequences=False)),
      tf.keras.layers.Dropout(0.05),
      tf.keras.layers.Dense(1)
    ])
  
  # 2. compile models
  model.compile(optimizer='adamax', loss='mean_squared_error')

  # fitting models
  history = model.fit(
    x_train, y_train,
    batch_size=16, epochs=3, verbose="auto", 
    validation_data=(x_test, y_test),
    use_multiprocessing=False, shuffle=False
  )

  # 3. predict models
  predictions = model.predict(x_test)

  # return values
  return history, predictions
# ----------------------------------------------------------------------------------------

# func evaluate models
def evaluate_models(y_test, predictions):

  # calculate mae, rmse, mape
  r = sc.mstats.pearsonr(y_test, predictions)[0]
  p_value = sc.mstats.pearsonr(y_test, predictions)[1]
  mae = mean_absolute_error(y_test, predictions)
  rmse = sqrt(mean_squared_error(y_test, predictions))
  mape = mean_absolute_percentage_error(y_test, predictions)
  
  # return values
  return np.round(r,4), np.round(p_value,4), np.round(mae,4), np.round(rmse,4), np.round(mape,4)
# ----------------------------------------------------------------------------------------