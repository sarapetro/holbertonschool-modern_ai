#!/usr/bin/env python3
"""Module for retrieving random forest feature importances."""

import numpy as np


def feature_importance(rf):
    """Return feature importances and their indices in ascending order."""
    importances = rf.feature_importances_
    indices = np.argsort(importances)
    return importances, indices
