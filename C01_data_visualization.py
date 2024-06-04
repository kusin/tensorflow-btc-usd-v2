# library data visualization
import plotly.express as px
import plotly.graph_objects as go
# -----------------------------------------------------------------------------------

# func line plot
def line_plot(df):

  # add lineplot with graph object
  fig = go.Figure()
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