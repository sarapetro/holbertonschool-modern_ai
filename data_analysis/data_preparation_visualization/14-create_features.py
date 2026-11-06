#!/usr/bin/env python3
"""Create service counts and tenure groups for customer churn data."""

import pandas as pd


def create_features(df):
    """Replace service columns and tenure with engineered features."""
    df = df.copy()
    service_columns = [
        'MultipleLines', 'InternetService', 'OnlineSecurity',
        'OnlineBackup', 'DeviceProtection', 'TechSupport',
        'StreamingTV', 'StreamingMovies'
    ]
    df['NumServices'] = df[service_columns].eq('Yes').sum(axis=1)
    df['NumServices'] += df['InternetService'].isin(['DSL', 'Fiber optic'])
    df['TenureGroup'] = pd.cut(
        df['tenure'],
        bins=[0, 12, 24, 48, 60, float('inf')],
        labels=['0-12', '13-24', '25-48', '49-60', '60+'],
        right=True,
        include_lowest=False
    )
    return df.drop(columns=service_columns + ['tenure'])
