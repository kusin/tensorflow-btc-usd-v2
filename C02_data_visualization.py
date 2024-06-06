# library data visualization
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
# -----------------------------------------------------------------------------------

# func line plot
def line_plot(df):

  # add lineplot with graph object
  fig = go.Figure()
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
    title = "Time series plot of BTC-USD price",
    # xaxis_title = "",
    # yaxis_title = "",
    # xaxis=dict(tickangle=0),
    # yaxis=dict(tickangle=0),
    legend=dict(title='', orientation='h', yanchor='top', y=1, xanchor='center', x=0.5),
  )

  # return values
  return fig


def lineplot_matplotlib1(df, nm_labels):

    # create lineplot
    fig, ax = plt.subplots(figsize = (8,4))
    ax.plot(df, label=nm_labels, linewidth=2.5)
    
    # set label-labels
    ax.set_title("", fontsize=12)
    ax.set_xlabel("", fontsize=10)
    ax.set_ylabel("", fontsize=10)
    ax.legend(loc="best")
    ax.grid(True)
    
    # show lineplot
    return fig

def lineplot_matplotlib2(line1, label1, line2, label2):

    # create lineplot
    fig, ax = plt.subplots(figsize = (8,4))
    ax.plot(line1, color="tab:blue", label=label1, linewidth=2)
    ax.plot(line2, color="tab:red", label=label2, linewidth=2)
    
    # set label-labels
    ax.set_title("", fontsize=12)
    ax.set_xlabel("", fontsize=10)
    ax.set_ylabel("", fontsize=10)
    ax.legend(loc="best")
    ax.grid(True)
    
    # show lineplot
    return fig
# ----------------------------------------------------------------------------------------