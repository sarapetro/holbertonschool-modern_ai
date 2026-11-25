#!/usr/bin/env python3
"""Module for Lasso Regression"""

from sklearn import linear_model


def lasso_regression(random_state):
    """Return an untrained Lasso Regression model."""
    return linear_model.Lasso(random_state=random_state)
