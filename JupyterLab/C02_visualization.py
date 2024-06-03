# lib data visualizations
import matplotlib.pyplot as plt
# ----------------------------------------------------------------------------------------

# function of lineplot
def timeseries_matplotlib(df, nm_labels):

    # create lineplot
    fig, ax = plt.subplots(figsize = (8,4))
    for x in range(len(df.columns.values)):
      ax.plot(df["Date"], df.iloc[:, x:x+1], label=nm_labels[x], linewidth=2.5)

    # set label-labels
    ax.set_title("", fontsize=12)
    ax.set_xlabel("", fontsize=10)
    ax.set_ylabel("", fontsize=10)
    ax.legend(loc="best")
    ax.grid(True)
    
    # show lineplot
    return plt.show()
# ----------------------------------------------------------------------------------------

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
    return plt.show()
# ----------------------------------------------------------------------------------------

def lineplot_matplotlib2(df, nm_labels):

    # create lineplot
    fig, ax = plt.subplots(figsize = (8,4))
    ax.plot(df, label=nm_labels, linewidth=2.5)
    ax.plot(df, label=nm_labels, linewidth=2.5)
    
    # set label-labels
    ax.set_title("", fontsize=12)
    ax.set_xlabel("", fontsize=10)
    ax.set_ylabel("", fontsize=10)
    ax.legend(loc="best")
    ax.grid(True)
    
    # show lineplot
    return plt.show()
# ----------------------------------------------------------------------------------------