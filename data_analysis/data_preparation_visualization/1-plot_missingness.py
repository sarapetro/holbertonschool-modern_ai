#!/usr/bin/env python3
"""Visualize missing values in a DataFrame."""

import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    """Plot the positions of missing values in a DataFrame."""
    missing = df.isnull()

    rows, cols = np.where(missing)

    plt.scatter(rows, cols, marker='|')
    plt.yticks(range(len(df.columns)), df.columns)
    plt.show()

    return None
