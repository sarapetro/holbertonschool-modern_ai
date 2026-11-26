#!/usr/bin/env python3
"""Module for creating a random forest classifier."""

from sklearn import ensemble


def random_forest(n_estimators, random_state):
    """Return an untrained random forest with the given tree count and seed."""
    return ensemble.RandomForestClassifier(
        n_estimators=n_estimators,
        random_state=random_state,
    )
