#!/usr/bin/env python3
"""Plot histograms, density estimates, and boxplots for numeric features."""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def plot_continuous_distributions(df, columns_to_plot=None):
    """Display a histogram with KDE and a horizontal boxplot per feature."""
    if columns_to_plot is None:
        columns_to_plot = df.select_dtypes(include='number').columns

    if len(columns_to_plot) == 0:
        return None

    _, axes = plt.subplots(
        len(columns_to_plot), 2,
        figsize=(12, 6), squeeze=False
    )

    for row, column in enumerate(columns_to_plot):
        values = df[column].dropna()
        histogram_ax, boxplot_ax = axes[row]
        histogram_ax.hist(
            values, bins=30, density=True, alpha=0.7, edgecolor='black'
        )
        if len(values) > 1 and values.nunique() > 1:
            density = stats.gaussian_kde(values)
            points = np.linspace(values.min(), values.max(), 100)
            histogram_ax.plot(points, density(points), color='red',
                              linestyle='--')
        histogram_ax.set_title('{} Histogram + KDE'.format(column))

        boxplot_ax.boxplot(values, vert=False)
        boxplot_ax.set_title('{} Boxplot'.format(column))

    plt.tight_layout()
    plt.show()
