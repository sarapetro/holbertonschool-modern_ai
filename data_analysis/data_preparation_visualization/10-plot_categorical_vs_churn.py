#!/usr/bin/env python3
"""Visualize the churn rate for each category of a feature."""

import matplotlib.pyplot as plt


def plot_categorical_vs_churn(df, col):
    """Display the proportion of Churn='Yes' in each category."""
    churn_rates = df.groupby(col, observed=True)['Churn'].apply(
        lambda values: (values == 'Yes').mean()
    )

    plt.figure(figsize=(12, 8))
    plt.bar(churn_rates.index, churn_rates.values)
    plt.title('Churn Rate by {}'.format(col))
    plt.ylabel('Churn Rate')
    plt.xticks(rotation=45)
    plt.show()
