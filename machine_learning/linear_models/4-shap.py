#!/usr/bin/env python3
"""Module for explaining regression models with SHAP."""

import shap


def get_shap_explainer_and_values(model, X_train, X_test):
    """Return a SHAP explainer and explanations for the test data."""
    explainer = shap.Explainer(model, X_train)
    shap_values = explainer(X_test)
    return explainer, shap_values
