# lib neural network algorithms
import tensorflow as tf
from keras.layers import LSTM
from keras.layers import GRU
# ----------------------------------------------------------------------------------------

# lib hide all warning
import warnings
warnings.filterwarnings('ignore')
# ----------------------------------------------------------------------------------------

# func lstm_algorithm
def models(algorithm, x_train, y_train, x_test, y_test):

  # 1. The LSTM architecture
  if algorithm == "SBi-LSTM":
    model = tf.keras.Sequential([
      tf.keras.layers.Bidirectional(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1))),
      tf.keras.layers.Bidirectional(LSTM(units=50, return_sequences=False)),
      tf.keras.layers.Dense(1)
    ])
  
  # The GRU-RNN architecture
  if algorithm == "SBi-GRU":
    model = tf.keras.Sequential([
      tf.keras.layers.Bidirectional(GRU(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1))),
      tf.keras.layers.Bidirectional(GRU(units=50, return_sequences=False)),
      tf.keras.layers.Dense(1)
    ])
  
  # 2. compile models
  model.compile(optimizer='adam', loss='mean_squared_error')

  # fitting models
  history = model.fit(
    x_train, y_train,
    batch_size=16, epochs=50, verbose="auto", 
    validation_data=(x_test, y_test),
    use_multiprocessing=False, shuffle=False
  )

  # 3. predict models
  predictions = model.predict(x_test)

  # return values
  return predictions