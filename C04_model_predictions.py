# lib neural network algorithms
import tensorflow as tf
from keras.layers import LSTM
from keras.layers import GRU
# ----------------------------------------------------------------------------------------

# func model predictions
def get_models(algorithm, x_train, y_train, x_test, y_test):

  # set parameter tuning
  # best-param, {
  #   optimizers  : "adamax", 
  #   batch_size  : 16, 
  #   epoch       : 50,
  # }

  # set parameter tuning
  optimizers = "adamax"   # opsi : adam, adamax, rmsprop, sgd
  batch_size  = 16        # opsi : 2, 4, 8, 16, 32
  epoch = 50              # opsi : 50, 75, 100

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
  model.compile(optimizer='adamax', loss='mean_squared_error')

  # 3. fitting models
  history = model.fit(
    x=x_train, y=y_train,
    batch_size=16, epochs=50, verbose="auto", 
    validation_data=(x_test, y_test),
    shuffle=False, use_multiprocessing=False,
  )

  # 4. predict models
  predictions = model.predict(x_test, verbose=0)

  # return values
  return history, predictions
# ----------------------------------------------------------------------------------------

