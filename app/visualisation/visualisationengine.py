#!/usr/bin/env python3


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def main(matches_dict):
    matches_df = pd.DataFrame.from_dict(matches_dict)
    #sns.set_theme()
    plot = sns.lineplot(
        data=matches_df,
        x = "hit",
        y = "score",
    )
    for ind, label in enumerate(plot.get_xticklabels()):
        if ind % 10 == 0:
            label.set_visible(True)
        else:
            label.set_visible(False)
    #plot.set(yticks=np.arange(0, 1, step= 0.01))
    return plt.show()
