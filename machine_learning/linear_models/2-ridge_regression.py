#!/usr/bin/env python3
"""Module for Ridge Regression"""

from sklearn import linear_model


def ridge_regression(random_state):
    """Return an untrained Ridge Regression model."""
    return linear_model.Ridge(random_state=random_state)
