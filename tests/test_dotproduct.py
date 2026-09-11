import numpy as np
import pytest

from src.dotproduct import dot_product


def test_dot_product_basic():
    assert dot_product([1, 2, 3], [4, 5, 6]) == 32


def test_dot_product_numpy_arrays():
    x = np.array([1, 1, 1])
    y = np.array([2, 2, 2])

    assert dot_product(x, y) == 6

def test_dot_product_zero_vector():
    assert dot_product([0, 0, 0], [1, 2, 3]) == 0


def test_dot_product_shape_mismatch():
    with pytest.raises(ValueError):
        dot_product([1, 2], [1, 2, 3])
