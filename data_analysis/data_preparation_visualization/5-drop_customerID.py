#!/usr/bin/env python3
"""Remove the customerID column from a DataFrame."""


def drop_customerID(df):
    """Return a DataFrame without the customerID column."""
    return df.drop(columns=['customerID'])