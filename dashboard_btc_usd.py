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
  dataset = pd.read_csv("dataset/"+df, parse_dates=['Date'])
  dataset = np.round(dataset[["Date", "Open", "High", "Low", "Close"]],2)
  return dataset


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
        
  # add colors on lineplot
  colorscale = px.colors.diverging.Portland_r
  for i, trace in enumerate(fig.data):
    trace.update(line=dict(color=colorscale[i]))

  # update layout lineplot
  fig.update_layout(
    title = "",
    xaxis_title = "",
    yaxis_title = "",
    xaxis=dict(tickangle=0),
    yaxis=dict(tickangle=0),
    legend=dict(title='', orientation='h', yanchor='top', y=1.1, xanchor='center', x=0.5),
  )

  # return values
  return fig
# --------------------------------------------------------------------------------------- #


# --------------------------------------------------------------------------------------- #
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
    st.info("Data Visualization of BTC-USD Price")
    st.plotly_chart(line_plot(dataset))

# container-predictions
with st.container():
  col1, col2 = st.columns([0.4,0.6], gap="small")
  with col1:
    st.info("Predictions of BTC-USD Price")
    with st.form("my_form"):
      st.write("Setting your model predictions")
      algorithms = st.selectbox("Choose an algorithm", ("SB LSTM-RNN", "SB GRU-RNN"), placeholder="Choose an algorithm", index=None)
      models = st.selectbox("Choose a models ", ("Univariate", "Multivariate"), placeholder="Choose an algorithm",index=None)
      submitted = st.form_submit_button("Submit", type="primary")
    with col2:
      st.info("Evaluation models")
      st.text("R :")
      st.text("MAE :")
      st.text("RMSE :")
      st.text("MAPE :")
      st.info("Results of Prediction BTC-USD Price")