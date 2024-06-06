# load all functions
from C01_data_collection import *
from C02_data_visualization import *
from C03_data_preprocessing import *
from C04_model_predictions import *

# import library streamlit
import streamlit as st
from streamlit_extras import add_vertical_space as avs
# ----------------------------------------------------------------------------------

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

# container-header
st.markdown("## Predictions of BTC-USD Price using SBi-LSTM and SBi-GRU")
avs.add_vertical_space(2)
# ----------------------------------------------------------------------------------

# load dataset
dataset = data_collection("BTC-USD.csv")

# container dataset and visualization
col1, col2 = st.columns([0.4,0.6], gap="small")
with col1:
  st.info("Dataset of BTC-USD")
  st.dataframe(dataset, use_container_width=True)
with col2:
  st.info("Data Visualization")
  st.plotly_chart(line_plot(dataset), use_container_width=True)

# split three columns
col1, col2, col3 = st.columns([0.2,0.2,0.6], gap="small")
with col1:
  st.info("Predictions of BTC-USD Price")
  form = st.form("my-form");
  algorithms = form.selectbox("Choose an algorithm", ("SBi-LSTM", "SBi-GRU"), index=None)
  submitted = form.form_submit_button(label="Submit", type="primary", use_container_width=False)
with col2:
  st.info("Evaluation Model")
  st.caption("Execution time is about 5 minutes")
  if algorithms and submitted:
    scaler, scaled, x_train, y_train, x_test, y_test = preprocessing(dataset)
    history, predictions = get_models(algorithms, x_train, y_train, x_test, y_test)
    r, p_value, mae, rmse, mape = evaluate_models(y_test, predictions)
    # st.markdown(f"##### R    : {r}")
    # st.markdown(f"##### RMSE : {rmse}")
    # st.markdown(f"##### MAPE : {mape}")
    st.text(f"RMSE: {rmse}")
with col3:
  st.info("Results of Prediction BTC-USD")
  if algorithms and submitted:
    st.plotly_chart(
      lineplot_matplotlib2(
        line1=y_test, label1="actual data",
        line2=predictions, label2="results predictions"
      ), use_container_width=True
    )
    