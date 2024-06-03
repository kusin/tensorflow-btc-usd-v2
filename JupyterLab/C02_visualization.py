# lib data visualizations
import matplotlib.pyplot as plt
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
    return plt.show()
# ----------------------------------------------------------------------------------------