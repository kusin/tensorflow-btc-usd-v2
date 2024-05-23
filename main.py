# library manipulation dataset
import pandas as pd

# library manipulation array
import numpy as np

# import library streamlit
import streamlit as st
import streamlit_extras.add_vertical_space as avs

# library data visualization
import plotly.express as px
import plotly.graph_objects as go

# library data preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# library deep learning
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

# library evaluations model
from math import sqrt
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_percentage_error

# config web streamlit
st.set_page_config(
  page_title="My Dasboard - BTC-USD",
  page_icon="",
  layout="wide",
  initial_sidebar_state="auto",
  menu_items={
    "Get Help": "https://www.github.com/kusin",
    "Report a bug": "https://www.github.com/kusin",
    "About": "### Copyright 2022 all rights reserved by Aryajaya Alamsyah"
  }
)

# --------------------------------------------------------------------------------------- #
# data acquisition ---------------------------------------------------------------------- #
# --------------------------------------------------------------------------------------- #
@st.cache_data
def load_data(df):
  dataset = pd.read_csv("dataset/"+df)
  dataset = np.round(dataset[["Date", "Open", "High", "Low", "Close"]],2)
  return dataset
# --------------------------------------------------------------------------------------- #

# --------------------------------------------------------------------------------------- #
# data visualization -------------------------------------------------------------------- #
# --------------------------------------------------------------------------------------- #
def line_plot(df):

  # create a plot
  fig = go.Figure()
        
  # add lineplot with graph object
  for column in df.columns[1:]:
    fig.add_trace(
      go.Scatter(x=df["Date"],y=df[column], mode='lines', name=column)
    )
        
  # # add colors on lineplot
  # colorscale = px.colors.diverging.Portland_r
  # for i, trace in enumerate(fig.data):
  #   trace.update(line=dict(color=colorscale[i]))

  # update layout lineplot
  fig.update_layout(
    title = "Time series plot of BTC-USD price",
    xaxis_title = "",
    yaxis_title = "",
    xaxis=dict(tickangle=0),
    yaxis=dict(tickangle=0),
    legend=dict(title='', orientation='h', yanchor='top', y=1, xanchor='center', x=0.5),
  )

  # return values
  return fig
# --------------------------------------------------------------------------------------- #


# function for supervised learning
def create_dataset(look_back, dataset):    
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
# --------------------------------------------------------------------------------------- #


# main method
if __name__ == "__main__":

  # container-header
  with st.container():
    st.markdown("## Predictions of BTC-USD Price using SBi-LSTM and SBi-GRU")
    avs.add_vertical_space(2)

  # container-dataset
  dataset = load_data("BTC-USD.csv")
  with st.container():
    col1, col2 = st.columns([0.4,0.6], gap="small")
    with col1:
      st.info("Dataset of BTC-USD")
      st.dataframe(dataset, use_container_width=True)
    with col2:
      st.info("Data Visualization")
      st.plotly_chart(line_plot(dataset), use_container_width=True)
  
  # container-predictions
  with st.container():

    # split two columns
    col1, col2 = st.columns([0.4,0.6], gap="small")

    # create form for choose model predictions
    with col1:
      st.info("Predictions of BTC-USD Price")
      with st.form("my-form"):
        algorithms = st.selectbox("Choose an algorithm", ("SBi-LSTM", "SBi-GRU"), placeholder="Choose an algorithm", index=None)
        submitted = st.form_submit_button(label="Submit", type="primary", use_container_width=False)
        st.caption("Execution time is about 5 minutes")

        # logic a process predictions
        mse=None; rmse=None; mape=None; model=None;
        if submitted and algorithms:
          # step 1 - choose a features
          data = dataset.filter(['Close'])
          data = data.values
          # ------------------------------------------------------------------------------------------------------------- #

          # step 2 - normalized min-max
          # normalize features
          scaler = MinMaxScaler(feature_range=(0, 1))
          scaled = scaler.fit_transform(np.array(data))
          # ------------------------------------------------------------------------------------------------------------- #

          # step 3 - splitting data
          train_data, test_data = train_test_split(scaled, train_size=0.80, test_size=0.20, shuffle=False)
          # ------------------------------------------------------------------------------------------------------------- #

          # step 4 - supervised learning
          look_back = 60
          x_train, y_train = create_dataset(look_back, train_data)
          x_test, y_test = create_dataset(look_back, test_data)

          # reshape input to be [samples, time steps, features]
          x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
          x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
          # ------------------------------------------------------------------------------------------------------------- #

          # step 5 - model predictions
          # The GRU-RNN architecture
          # reset of session model
          tf.keras.backend.clear_session()

          # The GRU-RNN architecture
          model = tf.keras.Sequential([
            
            # First GRU layer with Dropout regularisation
            tf.keras.layers.Bidirectional(
              GRU(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1))
            ),

            # the dropout layers
            tf.keras.layers.Dropout(0.05),

            # Secound GRU layer with Dropout regularisation
            tf.keras.layers.Bidirectional(
              GRU(units=50, return_sequences=False)
            ),

            # the dropout layers
            tf.keras.layers.Dropout(0.05),
            
            # The output layer
            tf.keras.layers.Dense(1)
          ])

          # Compile the model GRU
          model.compile(optimizer='adamax', loss='mean_squared_error')
          
          with st.spinner('Training the model...'):
            # fit network
            history = model.fit(
              x_train, y_train,
              batch_size=16, epochs=50, verbose=1, 
              validation_data=(x_test, y_test),
              use_multiprocessing=False, shuffle=False
            )

          # process predictions
          predictions = model.predict(x_test)
          # ------------------------------------------------------------------------------------------------------------- #

          # # step 6 - evaluation models
          # mse = np.round(mean_squared_error(y_test, predictions), 4)
          # rmse = np.round(sqrt(mse), 4)
          # mape = np.round(mean_absolute_percentage_error(y_test, predictions), 4)

          # step 7 - denormalize dataset
          # inverse value test predictions
          y_close = scaler.inverse_transform(scaled)
          y_test = scaler.inverse_transform(y_test.reshape(-1, 1))
          predictions = scaler.inverse_transform(predictions.reshape(-1, 1))

          # shift y_test
          y_test_inv = np.empty_like(scaled)
          y_test_inv[:, :] = np.nan
          y_test_inv[(len(dataset) - y_test.shape[0]):len(dataset), :] = y_test

          # shift predictions
          predictions_inv = np.empty_like(scaled)
          predictions_inv[:, :] = np.nan
          predictions_inv[(len(dataset) - predictions.shape[0]):len(dataset), :] = predictions

          # concate date, close, y_test, y_pred
          date = dataset[["Date"]]
          y_close = pd.DataFrame(y_close, columns=["Close Price"])
          y_test_inv = pd.DataFrame(y_test_inv, columns=["Testing data"])
          predictions_inv = pd.DataFrame(predictions_inv, columns=["Prediction"])
          results = pd.concat([date, y_close, y_test_inv, predictions_inv], axis=1)

          # step 8 - evaluation models
          mape = np.round(mean_absolute_percentage_error(y_test, predictions)*100, 4)
        
    # results of predictions
    with col1:
      # view a result predictions
      if submitted and algorithms:
        st.info("Evaluation models")
        st.markdown(f"##### MAPE : {mape}")

    # results of predictions
    with col2:
      # view a result predictions
      if submitted and algorithms:
        st.info("Result of BTC-USD price prediction")
        st.plotly_chart(line_plot(results), use_container_width=True)