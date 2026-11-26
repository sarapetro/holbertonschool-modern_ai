#!/usr/bin/env python3
"""Module for displaying the decision rules of a trained tree."""

from sklearn import tree


def draw(clf, feature_names, class_names):
    """Print the full decision tree using feature and class names."""
    print(tree.export_text(
        clf,
        feature_names=feature_names,
        class_names=class_names,
        max_depth=clf.get_depth(),
    ))
