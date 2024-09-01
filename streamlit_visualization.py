# lib visualization data
import plotly.express as px
import plotly.graph_objects as go
# ---------------------------------------------------------------------------

# func build heatmap coor
def timeseries_plot(df):

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
    title = "Visualization of Timeseries Data",
    legend=dict(orientation="h", xanchor="center", x=0.5, yanchor="top", y=1.1),
  )

  # return values
  return fig
# ---------------------------------------------------------------------------

def results_prediction(algorithms, df):

  # add lineplot with graph object
  fig = go.Figure()
  fig.add_trace(go.Scatter(
    x=df["Date"], y=df["Actual"], mode='lines', line_color="blue", name="actual data"
  ))
  fig.add_trace(go.Scatter(
    x=df["Date"], y=df["Predictions"], mode='lines', line_color="red", name="results predictions"
  ))

  # update layout lineplot
  fig.update_layout(
    title = "Results of Prediction using "+str(algorithms)+" algorithm",
    legend=dict(orientation="h", xanchor="center", x=0.5, yanchor="top", y=1.1),
  )

  # return values
  return fig
# ---------------------------------------------------------------------------