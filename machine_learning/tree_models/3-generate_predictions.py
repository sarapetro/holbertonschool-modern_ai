#!/usr/bin/env python3
"""Module for generating predictions from a trained classifier."""


def generate_predictions(clf, X):
    """Return the predicted class labels for the input samples."""
    return clf.predict(X)
