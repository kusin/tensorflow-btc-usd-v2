# import library streamlit
import streamlit as st

# lib visualization data
import plotly.express as px
import plotly.graph_objects as go

# import custom func
from streamlit_visualization import *

# config web streamlit
st.set_page_config(
  page_title="My Dasboard - Cryptocurrency", 
  page_icon="🧊",
  layout="wide",
  initial_sidebar_state="auto",
  menu_items={
    "Get Help": "https://www.github.com/kusin",
    "Report a bug": "https://www.github.com/kusin",
    "About": "#### Copyright 2024, By Aryajaya Alamsyah"
  }
)

# load-dataset
dataset = getData()

# container-header
with st.container():
  st.markdown("# Model Prediction of BTC-USD Price Using Neural Network")
# -----------------------------------------------------------------------------------------------------------

# container-content
with st.container():
  
  # split two-columns
  col1, col2 = st.columns([0.4,0.6], gap="small")
  
  # show-dataset
  with col1.container():
    # show-dataset
    st.success("Dataset of BTC-USD Price")
    st.dataframe(dataset.sort_values(by=["Date"], ascending=False), use_container_width=True)
  
  # show-visualization
  with col2.container():
    st.success("Data Visualization of BTC-USD Price")
    st.plotly_chart(timeseries_plot(dataset))
# -----------------------------------------------------------------------------------------------------------

# container-content
with st.container():

  # split three-columns
  col1, col2, col3 = st.columns([0.25,0.15,0.6], gap="small")

  # col1-config-model
  with col1:
    st.success("Config Parameter Tuning")
    with st.form("my-form"):
      algorithms = st.selectbox(label="Choose a algorithms", options=("SBi-LSTM-RNN", "SBi-GRU-RNN"), placeholder="Choose a algorithms", index=None)
      optimizers = st.selectbox(label="Choose a optimizers", options=("adam", "adamax", "rmsprop", "sgd"), placeholder="Choose a optimizers", index=None)
      batch_size = st.selectbox(label="Choose a batch size", options=("8", "16", "32"), placeholder="Choose a optimizers", index=None)
      epoch = st.selectbox(label="Choose a optimizers", options=("25", "50", "75"), placeholder="Choose a optimizers", index=None)
      submit = st.form_submit_button(label="Submit", type="secondary", use_container_width=True)
      
  # col2-results-prediction
  with col2:
    # process prediction
    st.success("Results Prediction")
    if submit:
      st.text("R    : 0.999")
      st.text("MAE  : 0.999")
      st.text("RMSE : 0.999")
      st.text("MAPE : 0.999")

  # col2-data-visualization
  with col3:
    st.success("Data Visualization of BTC-USD Price")
    st.plotly_chart(timeseries_plot(dataset))
# -----------------------------------------------------------------------------------------------------------