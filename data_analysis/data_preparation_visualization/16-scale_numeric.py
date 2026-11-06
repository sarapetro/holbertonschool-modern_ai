#!/usr/bin/env python3
"""Standardize customer charge features."""

from sklearn import preprocessing


def scale_numeric(df):
    """Return data with standardized MonthlyCharges and TotalCharges."""
    df = df.copy()
    columns = ['MonthlyCharges', 'TotalCharges']
    scaler = preprocessing.StandardScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df
