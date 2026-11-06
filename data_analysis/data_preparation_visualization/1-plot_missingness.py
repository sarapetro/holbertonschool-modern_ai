#!/usr/bin/env python3
"""Visualize missing values in a DataFrame."""

import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    """Plot the positions of missing values in a DataFrame."""
    rows, cols = np.where(df.isnull())

    plt.figure(figsize=(12, 6))
    plt.scatter(df.index.take(rows), cols, marker='|')
    plt.yticks(range(len(df.columns)), df.columns)
    plt.title('Missingness Plot')
    plt.tight_layout()
    plt.show()

    return None
