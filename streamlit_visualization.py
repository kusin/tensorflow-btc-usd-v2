# lib manipulation dat
import pandas as pd
import numpy as np

# lib visualization data
import plotly.express as px
import plotly.graph_objects as go
# ---------------------------------------------------------------------------

# func load-datase
def getData():
  dataset = pd.read_csv("dataset/BTC-USD.csv")
  dataset = dataset[["Date", "Open", "High", "Low", "Close"]]
  return np.round(dataset,2)

# func build heatmap coor
def timeseries_plot(df):

  # create a plot
  fig = go.Figure()
  
  # add lineplot with graph object
  for column in df.columns[1:]:
    fig.add_trace(
      go.Scatter(
          x=df["Date"],y=df[column], mode='lines', name=column
      )
    )
  
  # add colors on lineplot
  colorscale = px.colors.diverging.Portland_r
  for i, trace in enumerate(fig.data):
    trace.update(line=dict(color=colorscale[i]))

  # update layout lineplot
  fig.update_layout(
    title = "Visualization Timeseries of BTC-USD Price",
    # xaxis_title = "",
    # yaxis_title = "",
    legend=dict(title='', orientation='h', yanchor='top', y=1.1, xanchor='center', x=0.5),
  )

  # return values
  return fig