#!/usr/bin/env python3
"""Module for retrieving a decision tree's cost-complexity pruning path."""


def get_pruning_path(clf, X, y):
    """Return effective pruning alphas and corresponding leaf impurities."""
    path = clf.cost_complexity_pruning_path(X, y)
    return path.ccp_alphas, path.impurities
