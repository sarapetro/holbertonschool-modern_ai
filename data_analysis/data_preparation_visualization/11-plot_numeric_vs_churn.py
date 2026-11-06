#!/usr/bin/env python3
"""Compare numeric feature distributions between churn groups."""

import matplotlib.pyplot as plt


def plot_numeric_vs_churn(df, col):
    """Display histograms of a numeric feature grouped by churn."""
    churn_no = df.loc[df['Churn'] == 'No', col].dropna()
    churn_yes = df.loc[df['Churn'] == 'Yes', col].dropna()

    plt.figure(figsize=(12, 8))
    plt.hist(churn_no, bins=30, alpha=0.7, label='No')
    plt.hist(churn_yes, bins=30, alpha=0.7, label='Yes')
    plt.title('{} Distribution by Churn'.format(col))
    plt.xlabel(col)
    plt.legend(title='Churn', loc='upper center')
    plt.show()
