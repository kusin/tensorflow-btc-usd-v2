# lib neural network algorithms
import tensorflow as tf
from keras.layers import LSTM
from keras.layers import GRU

# lib evaluate models
import scipy.stats as sc
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import root_mean_squared_error
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
    x=x_train, y=y_train,
    batch_size=16, epochs=50, verbose="auto", 
    validation_data=(x_test, y_test),
    shuffle=False, use_multiprocessing=False,
  )

  # 3. predict models
  predictions = model.predict(x_test, verbose=0)

  # return values
  return history, predictions
# ----------------------------------------------------------------------------------------

# func evaluate models
def evaluate_models(ytrue,ypred):

  # calculate mae, rmse, mape
  r     = sc.mstats.pearsonr(ytrue,ypred)[0]
  p     = sc.mstats.pearsonr(ytrue,ypred)[1]
  mae   = mean_absolute_error(ytrue,ypred)
  rmse  = root_mean_squared_error(ytrue,ypred)
  mape  = mean_absolute_percentage_error(ytrue,ypred)

  # return values
  return np.round(r,4), np.round(p,4), np.round(mae,4), np.round(rmse,4), np.round(mape,4)
# ----------------------------------------------------------------------------------------