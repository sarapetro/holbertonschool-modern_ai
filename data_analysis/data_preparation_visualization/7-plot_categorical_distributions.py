#!/usr/bin/env python3
"""Visualize categorical feature distributions in a grid."""

import matplotlib.pyplot as plt


def plot_categorical_distributions(df, columns_to_plot=None):
    """Display categorical counts with three plots per row."""
    if columns_to_plot is None:
        columns_to_plot = [
            column for column in df.select_dtypes(include='object').columns
            if column != 'Churn'
        ]

    if len(columns_to_plot) == 0:
        return None

    ncols = 3
    nrows = (len(columns_to_plot) + ncols - 1) // ncols
    fig, axes = plt.subplots(
        nrows, ncols, figsize=(15, 5 * nrows), squeeze=False
    )

    for ax, column in zip(axes.flat, columns_to_plot):
        counts = df[column].value_counts()
        ax.bar(counts.index, counts.values)
        ax.set_title(column)
        ax.tick_params(axis='x', labelrotation=45)

    for ax in list(axes.flat)[len(columns_to_plot):]:
        fig.delaxes(ax)

    plt.tight_layout()
    plt.show()
