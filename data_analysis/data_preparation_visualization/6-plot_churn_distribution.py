#!/usr/bin/env python3
"""Visualize the distribution of churn classes."""

import matplotlib.pyplot as plt


def plot_churn_distribution(df):
    """Display churn counts as a bar plot."""
    counts = df["Churn"].value_counts().reindex(["No", "Yes"], fill_value=0)

    plt.figure(figsize=(12, 6))
    plt.bar(counts.index, counts.values, color=["skyblue", "salmon"])
    plt.title("Churn Distribution")
    plt.ylabel("Count")
    plt.show()
