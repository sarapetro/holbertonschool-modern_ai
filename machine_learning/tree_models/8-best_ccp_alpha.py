#!/usr/bin/env python3
"""Module for selecting the best cost-complexity pruning alpha."""


def get_best_alpha(clfs, train_scores, test_scores, ccp_alphas):
    """Select by test accuracy, smallest absolute gap, then largest alpha."""
    best_index = max(
        range(len(clfs)),
        key=lambda i: (
            test_scores[i],
            -abs(train_scores[i] - test_scores[i]),
            ccp_alphas[i],
        ),
    )
    return ccp_alphas[best_index], clfs[best_index]
