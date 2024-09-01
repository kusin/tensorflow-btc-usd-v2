# set library
import yfinance as yf
import streamlit as st
import datetime as dt
import time as tm

# import custom func
from streamlit_dataset import *
from streamlit_visualization import *

# import custom func
from C03_preprocessing import *
from C04_model_predictions import *
from C05_model_evaluate import *

# set random number
import random as rm
rm.seed(1234)

# set random number
import numpy as np
np.random.seed(1234)

# set random number
import tensorflow as tf
tf.random.set_seed(1234)
# ------------------------------------------------

# config web streamlit
st.set_page_config(page_title="My Dasboard",layout="wide")

# container-header
st.markdown("## Prediction of cryptocurrency and stock price using neural network")
# ------------------------------------------------

# split three columns
col1, col2, col3 = st.columns([0.25, 0.25, 0.5], gap="small")

# columns form dataset
with col1:
  st.info("Config Dataset")
  with st.form("my-form1"):
    cryptocurrency = st.selectbox(label="Choose a cryptocurrency", options=("BTC-USD", "ETH-USD"))
    start = st.date_input(label="Start Date", value=dt.date(2015,1,1))
    end = st.date_input(label="End Date", value=dt.date(2024,4,30))
    process = st.form_submit_button(label="Process", type="secondary", use_container_width=True)
# ------------------------------------------------

# columns - information crypto
with col2:
  st.info("Top Five Cryptocurrency on Market")
  st.write("1. Bitcoin (BTC)")
  st.write("2. Ethereum (EHT)")
  st.write("3. Tether (USDT)")
  st.write("4. Binance Coin (BNB)")
  st.write("5. Solana (SOL)")
# ------------------------------------------------

# columns - results dataset
with col3:
  st.info("Exploratory Data Analysis")
  if process:
    ticker      = yf.Ticker(cryptocurrency)
    startDate   = start
    endDate     = end
  else:
    ticker      = yf.Ticker("BTC-USD")
    startDate   = "2015-01-01"
    endDate     = "2024-05-01"
  dataset = getData(ticker, startDate, endDate)
  # -----------------------------------------------

  # split two tab-index
  tab1, tab2 = st.tabs(["Visualization Data", "Historical Data"])
  tab1.plotly_chart(timeseries_plot(dataset), use_container_width=True)
  tab2.dataframe(dataset, use_container_width=True)
# ------------------------------------------------

# columns - form hyperparameter
col1, col2, col3 = st.columns([0.25, 0.25, 0.5], gap="small")
with col1:
  st.info("Hyperparameter Tuning")
  with st.form("my-form2"):
    algorithms = st.selectbox(label="Choose a algorithms", options=("SBi-LSTM-RNN", "SBi-GRU-RNN"), index=0)
    optimizers = st.selectbox(label="Choose a optimizers", options=("adam", "adamax", "rmsprop"), index=1)
    batch_size = st.selectbox(label="Choose a batch size", options=("8", "16", "24", "32"), index=1)
    epoch = st.selectbox(label="Choose a optimizers", options=("25", "50"), index=1)
    submit = st.form_submit_button(label="Submit", type="secondary", use_container_width=True)
# ------------------------------------------------

# columns - evaluation models
with col2:
  
  # process prediction
  st.info("Evaluation Models")
  with st.spinner("Loading ..."):
    if submit:
      # measuring execution time
      start_time = tm.time()

      # 1. preprocessing data
      scaler, scaled, x_train, y_train, x_test, y_test = preprocessing(dataset)

      # 2. model predictions
      history, predictions = get_models(algorithms, x_train, y_train, x_test, y_test)

      # 3. model evaluation
      r, p_value, mae, rmse, mape = evaluate_models(
        inverse(scaler=scaler,scaled=y_test),
        inverse(scaler=scaler,scaled=predictions)
      )

      # 4. measuring execution time
      end_time = tm.time()

      # 4. calculating the total execution time
      execution_time = end_time - start_time

      # 5. results model evaluation
      st.text("R    : "+str(r))
      st.text("MAPE : "+str(mape))
      st.text("TIME : "+"{:,.2f}".format(execution_time))

# columns - prediction results
with col3:

  # process prediction
  st.info("Prediction Results")
  if submit:

    # results prediction
    results = pd.concat([
      pd.DataFrame(np.array(dataset[["Date"]].iloc[len(y_train)+120:]), columns=["Date"]),
      pd.DataFrame(np.array(inverse(scaler=scaler,scaled=y_test)), columns=["Actual"]),
      pd.DataFrame(np.array(inverse(scaler=scaler,scaled=predictions)), columns=["Predictions"])
    ],axis=1)

    # split two tab-index
    tab1, tab2 = st.tabs(["Visualization Data", "Historical Data"])
    tab1.plotly_chart(results_prediction(algorithms,results), use_container_width=True)
    tab2.dataframe(results, use_container_width=True)
