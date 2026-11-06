#!/usr/bin/env python3
"""Visualize pairwise correlations between numeric features."""

import matplotlib.pyplot as plt
import seaborn as sns


def plot_correlation_heatmap(df):
    """Display an annotated correlation heatmap for numeric columns."""
    correlations = df.select_dtypes(include='number').corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlations, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation Matrix')
    plt.show()
