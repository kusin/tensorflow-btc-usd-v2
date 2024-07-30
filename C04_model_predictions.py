# lib neural network algorithms
import tensorflow as tf
from keras.layers import LSTM
from keras.layers import GRU
# ----------------------------------------------------------------------------------------

# func model predictions
def get_models(algorithm, x_train, y_train, x_test, y_test):

  # set parameter tuning
  optimizers = "adamax"
  batch_size = 16
  epoch = 50

  # 1. The LSTM architecture
  if algorithm == "SBi-LSTM-RNN":
    tf.keras.backend.clear_session()
    model = tf.keras.Sequential([
      tf.keras.layers.Bidirectional(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1))),
      tf.keras.layers.Bidirectional(LSTM(units=50, return_sequences=False)),
      tf.keras.layers.Dropout(0.05),
      tf.keras.layers.Dense(1)
    ])
  
  # 2. The GRU-RNN architecture
  if algorithm == "SBi-GRU-RNN":
    tf.keras.backend.clear_session()
    model = tf.keras.Sequential([
      tf.keras.layers.Bidirectional(GRU(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1))),
      tf.keras.layers.Bidirectional(GRU(units=50, return_sequences=False)),
      tf.keras.layers.Dropout(0.05),
      tf.keras.layers.Dense(1)
    ])
  
  # 2. compile models
  model.compile(optimizer=optimizers, loss="mean_squared_error")

  # 3. fitting models
  history = model.fit(
    x=x_train, y=y_train,
    batch_size=batch_size, epochs=epoch, verbose="auto", 
    validation_data=(x_test, y_test),
    shuffle=False, use_multiprocessing=False,
  )

  # 4. predict models
  predictions = model.predict(x_test, verbose=0)

  # return values
  return history, predictions
# ----------------------------------------------------------------------------------------

