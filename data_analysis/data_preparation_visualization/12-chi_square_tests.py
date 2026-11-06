#!/usr/bin/env python3
"""Test independence between categorical features and churn."""

import pandas as pd
from scipy import stats


def chi_square_tests(df):
    """Return chi-square p-values for categorical features versus Churn."""
    p_values = {}
    categorical = df.select_dtypes(
        include=['object', 'category', 'string', 'bool']
    ).columns
    for feature in categorical:
        if feature != 'Churn':
            contingency = pd.crosstab(df[feature], df['Churn'])
            p_values[feature] = stats.chi2_contingency(contingency)[1]
    return p_values
