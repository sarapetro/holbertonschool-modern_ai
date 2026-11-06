#!/usr/bin/env python3
"""Compare numeric features between churn groups with Welch's t-tests."""

from scipy import stats


def ttest_numeric(df):
    """Return two-sided Welch's t-test p-values for numeric features."""
    p_values = {}
    for feature in df.select_dtypes(include='number').columns:
        if feature != 'Churn':
            churn_yes = df.loc[df['Churn'] == 'Yes', feature].dropna()
            churn_no = df.loc[df['Churn'] == 'No', feature].dropna()
            p_values[feature] = stats.ttest_ind(
                churn_yes, churn_no, equal_var=False
            ).pvalue
    return p_values
