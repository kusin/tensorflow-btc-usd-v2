# lib deep learning
import tensorflow as tf
from keras.utils import Sequence
from keras.models import Sequential
from keras.layers import SimpleRNN
from keras.layers import LSTM
from keras.layers import GRU
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import TimeDistributed
from keras.layers import Bidirectional
from keras.optimizers import Adam, Adamax, RMSprop, SGD
# -------------------------------------------------------------------------------------------------------

def LSTM_RNN(x_train):
  # reset of session model
  tf.keras.backend.clear_session()

  # The LSTM-RNN architecture
  model = tf.keras.Sequential([
    # First LSTM layer with Dropout regularisation
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1))),
    # Secound LSTM layer with Dropout regularisation
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(units=50, return_sequences=False)),
    # the dropout layers
    tf.keras.layers.Dropout(0.15),
    # The output layer
    tf.keras.layers.Dense(1)
  ])

  # Compile the model
  model.compile(optimizer='adam', loss='mean_squared_error')
  
  # return values
  return model
# -------------------------------------------------------------------------------------------------------

def fit_network(model, x_train, y_train, x_test, y_test):
  history = model.fit(
    x_train, y_train,
    batch_size=8, epochs=60, verbose="auto", 
    validation_data=(x_test, y_test),
    use_multiprocessing=True, shuffle=False
  )
  return history

