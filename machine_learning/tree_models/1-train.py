#!/usr/bin/env python3
"""Module for training a tree-based classifier."""


def train_tree(clf, X, y):
    """Fit the classifier on the input features and target labels."""
    clf.fit(X, y)
