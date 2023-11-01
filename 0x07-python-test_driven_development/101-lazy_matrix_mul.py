#!/usr/bin/python3
"""matrix_mult fun"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """matrix_mul"""
    return (np.matmul(m_a, m_b))


if __name__ == "__main__":
    from doctest import testfile
    testfile("tests/101-lazy_matrix_mul.txt")
