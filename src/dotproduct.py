"""Simple vector operations."""

import numpy as np


def dot_product(x, y):
    """
    Calculate the dot product of two vectors.

    Parameters
    ----------
    x : array-like
    y : array-like

    Returns
    -------
    float
    """
    x = np.asarray(x)
    y = np.asarray(y)

    if x.shape != y.shape:
        raise ValueError("Vectors must have the same shape")

    return np.dot(x, y)
