import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_percentage_error

# Load data
data = pd.read_csv('dataset/BTC-USD.csv')
date = data['Date']
price = data['Close']

# Preprocess data
scaler = MinMaxScaler(feature_range=(0, 1))
#price = scaler.fit_transform(price.reshape(-1, 1))
price = scaler.fit_transform(price.to_numpy().reshape(-1, 1))

# Split data into training and testing sets
train_size = int(len(price) * 0.8)
train_data = price[:train_size]
test_data = price[train_size:]

# Create training and testing datasets
X_train = []
y_train = []
for i in range(60, len(train_data)):
    X_train.append(train_data[i-60:i, 0])
    y_train.append(train_data[i, 0])
X_train, y_train = np.array(X_train), np.array(y_train)

X_test = []
y_test = []
for i in range(60, len(test_data)):
    X_test.append(test_data[i-60:i, 0])
    y_test.append(test_data[i, 0])
X_test, y_test = np.array(X_test), np.array(y_test)

# Reshape data for LSTM
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

# Define LSTM model
def build_model():
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
    model.add(LSTM(units=50))
    model.add(Dense(units=1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

# Repeat model training and evaluation 30 times
for i in range(5):
    # Build and train model
    model = build_model()
    early_stopping = EarlyStopping(patience=5)
    model_checkpoint = ModelCheckpoint('model_{}.h5'.format(i), save_best_only=True)
    history = model.fit(X_train, y_train, epochs=2, batch_size=32, callbacks=[early_stopping, model_checkpoint])

    # Evaluate model on testing data
    y_pred = model.predict(X_test)
    y_pred = scaler.inverse_transform(y_pred)

    # Calculate RMSE and MAPE
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mape = mean_absolute_percentage_error(y_test, y_pred)

    # Print results
    print('Iteration {}: RMSE = {:.4f}, MAPE = {:.4f}'.format(i+1, rmse, mape))

    # Save RMSE and MAPE to file
    with open('results.csv', 'a') as f:
        f.write('{},{},{}\n'.format(i+1, rmse, mape))
