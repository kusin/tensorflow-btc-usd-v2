# load all functions
from C01_data_collection import *
from C01_data_visualization import *

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

# container dataset and visualization
col1, col2 = st.columns([0.4,0.6], gap="small")

dataset = data_collection("BTC-USD.csv")
col1.info("Dataset of BTC-USD")
col1.dataframe(dataset, use_container_width=True)

col2.info("Data Visualization")
col2.plotly_chart(line_plot(dataset), use_container_width=True)

# container dataset and visualization
col1, col2 = st.columns([0.4,0.6], gap="small")
col1.info("Predictions of BTC-USD Price")
form = col1.form("my-form");

algorithms = form.selectbox("Choose an algorithm", ("SBi-LSTM", "SBi-GRU"), placeholder="Choose an algorithm", index=None)
form.caption("Execution time is about 5 minutes")
submitted = form.form_submit_button(label="Submit", type="primary", use_container_width=False)
