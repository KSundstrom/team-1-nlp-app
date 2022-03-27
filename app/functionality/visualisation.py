#!/usr/bin/env python3


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def visualise(matches):
    matches_dataframe = pd.DataFrame.from_dict(matches)
    plot = sns.lineplot(data = matches_dataframe, x = "hit", y = "score")
    for ind, label in enumerate(plot.get_xticklabels()):
        if ind % 10 == 0:
            label.set_visible(True)
        else:
            label.set_visible(False)
    plt.savefig("app/static/plot.png")
