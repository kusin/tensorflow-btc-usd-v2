import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# function of lineplot
def line_matplotlib(df, nm_labels):
    
    # create figure
    fig, ax = plt.subplots(figsize = (10,5))
    
    # create lineplot
    for x in range(len(df.columns.values)):
        ax.plot(df.index.values, df.iloc[:, x:x+1], label=nm_labels[x], linewidth=2.5)
    
    # set label-labels
    ax.set_title("", fontsize=12)
    ax.set_xlabel("", fontsize=10)
    ax.set_ylabel("", fontsize=10)
    ax.legend(loc="best")
    ax.grid(True)
    
    # show lineplot
    plt.show()