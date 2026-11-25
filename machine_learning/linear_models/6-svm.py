#!/usr/bin/env python3
"""Module for creating an SVM classifier with a specified kernel."""

from sklearn import svm


def get_SVM_model(name, random_state):
    """Return an untrained SVC with the given kernel and random seed."""
    return svm.SVC(kernel=name, random_state=random_state)
