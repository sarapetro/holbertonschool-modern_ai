#!/usr/bin/env python3
"""Module for evaluating classifier performance."""

from sklearn import metrics


def evaluate(true_labels, predicted_labels, class_names):
    """Return a classification report using the provided class names."""
    return metrics.classification_report(
        true_labels,
        predicted_labels,
        target_names=class_names,
    )
