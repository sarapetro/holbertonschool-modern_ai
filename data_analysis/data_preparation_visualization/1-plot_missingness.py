#!/usr/bin/env python3
"""Visualize missing values in a DataFrame."""

import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    """Plot the positions of missing values in a DataFrame."""
    missing = df.isnull()
    rows, cols = np.where(missing)

    plt.scatter(rows, cols, marker='|')
    plt.xticks(range(len(df)))
    plt.yticks(range(len(df.columns)), df.columns)
    plt.title('Missingness Plot')
    plt.show()

    return None