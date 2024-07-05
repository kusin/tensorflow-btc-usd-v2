# lib data visualizations
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
# ----------------------------------------------------------------------------------------

# function of lineplot
def timeseries_matplotlib(df, nm_labels):

    # create lineplot
    fig, ax = plt.subplots(figsize = (8,4))
    for x in range(len(nm_labels)):
      ax.plot(df.iloc[:, 0:1], df.iloc[:, x+1:x+2], label=nm_labels[x], linewidth=2.5)

    # set label-labels
    ax.set_title("", fontsize=12)
    ax.set_xlabel("", fontsize=10)
    ax.set_ylabel("", fontsize=10)
    ax.legend(loc="best")
    ax.grid(True)
    
    # show lineplot
    return plt.show()
# ----------------------------------------------------------------------------------------s

# visualisasi timeseries plot
def lineplot_matplotlib1(x, y, label, title):

  # membuat time series plot
  fig, ax = plt.subplots(figsize = (8,4))
  ax.plot(x, y, color="tab:blue", label=label, linewidth=2)

  # membuat label-label
  ax.xaxis.set_major_formatter(DateFormatter("%Y"))
  ax.set_title(title, fontsize=12)
  ax.set_xlabel("", fontsize=12)
  ax.set_ylabel("", fontsize=12)
  ax.legend(loc="best")
  ax.grid(True)

  # return values
  return plt.show()
# --------------------------------------------------------------

# visualisasi timeseries plot
def lineplot_matplotlib2(x1, y1, label1, x2, y2, label2, title):

  # membuat time series plot
  fig, ax = plt.subplots(figsize = (8,4))
  ax.plot(x1, y1, color="tab:blue", label=label1, linewidth=2, linestyle="solid")
  ax.plot(x2, y2, color="tab:red", label=label2, linewidth=2, linestyle="solid")

  # membuat label-label
  ax.xaxis.set_major_formatter(DateFormatter("%Y"))
  ax.set_title(title, fontsize=12)
  ax.set_xlabel("", fontsize=12)
  ax.set_ylabel("", fontsize=12)
  ax.legend(loc="best")
  ax.grid(True)

  # return values
  return plt.show()
# --------------------------------------------------------------