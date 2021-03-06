#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pybreach
----------------------------------

Tests for `pybreach` module.
"""

import pytest

from pybreach import pybreach
from pybreach.pybreach import left_reach, right_reach, breach_run

from numpy.testing import assert_array_equal

# @pytest.fixture
# def binary_performance_example():
#     """binary rendered example to test breach outcomes
#     """
#     import numpy as np


perf_meas_example = \
        [[0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1,
          0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1,
          1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0,
          0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1,
          1, 0, 1, 1, 1, 0, 1, 0, 1],
         [0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0,
          1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0,
          1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1,
          1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1,
          0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0,
          1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1,
          0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1,
          1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1,
          0, 0, 1, 0, 0, 1, 1, 1, 0],
         [0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1,
          0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1,
          1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1,
          0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1,
          0, 0, 0, 0, 0, 1, 1, 1, 1],
         [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1,
          0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0,
          0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1,
          0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
          1, 0, 0, 0, 1, 1, 0, 0, 1],
         [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1,
          1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0,
          1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0,
          1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1,
          1, 0, 1, 1, 1, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0,
          1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0,
          0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0,
          0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0,
          0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1,
          1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
          0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0,
          1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0,
          0, 0, 1, 1, 0, 0, 1, 1, 1],
         [1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0,
          1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1,
          0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0,
          1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0,
          0, 1, 1, 0, 1, 1, 1, 1, 1],
         [1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0,
          0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0,
          1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0,
          1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0,
          1, 1, 0, 0, 1, 1, 0, 1, 1],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0,
          0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0,
          1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0,
          1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0,
          1, 1, 0, 1, 0, 0, 1, 0, 1],
         [1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1,
          1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
          1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0,
          1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1,
          0, 1, 0, 0, 0, 1, 1, 0, 1],
         [0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0,
          0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1,
          1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1,
          0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0,
          0, 1, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0,
          1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0,
          0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0,
          0, 1, 1, 1, 1, 1, 1, 0, 1],
         [1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0,
          0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1,
          1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1,
          1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0,
          1, 1, 1, 1, 0, 1, 0, 1, 1],
         [0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1,
          0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1,
          0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1,
          0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1,
          0, 1, 0, 1, 0, 0, 1, 0, 1],
         [1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0,
          0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0,
          1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1,
          1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0,
          1, 1, 1, 1, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1,
          1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1,
          1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1,
          0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0,
          0, 1, 1, 0, 0, 1, 0, 0, 1],
         [0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1,
          1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1,
          1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1,
          0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0,
          1, 0, 0, 0, 1, 1, 1, 1, 0],
         [1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0,
          0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0,
          0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1,
          0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0,
          0, 1, 0, 0, 0, 0, 1, 1, 1],
         [1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1,
          0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0,
          1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1,
          0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0,
          1, 0, 0, 1, 1, 0, 0, 0, 1]]


def test_left_reach():
    """test the left reach derivation
    """
    import numpy as np

    overzichtl, maxreachl = left_reach(np.array(perf_meas_example), 100, 40)

    left_reach_100_40 = np.array([
            [0., 0., 1., 1., 100.],
            [1., 0., 1., np.nan, np.nan],
            [2., 0., 1., np.nan, np.nan],
            [3., 0., 3., 6., 95.],
            [4., 0., 1., 1., 100.],
            [5., 0., 1., np.nan, np.nan],
            [6., 0., 1., np.nan, np.nan],
            [7., 0., 4., 8., 93.],
            [8., 0., 14., 35., 66.],
            [9., 0., 3., 6., 95.],
            [10., 0., 1., 1., 100.],
            [11., 0., 1., 1., 100.],
            [12., 0., 1., np.nan, np.nan],
            [13., 0., 1., 1., 100.],
            [14., 0., 11., 26., 75.],
            [15., 0., 1., 1., 100.],
            [16., 0., 1., 1., 100.],
            [17., 0., 1., 1., 100.],
            [18., 0., 1., np.nan, np.nan],
            [19., 0., 3., 5., 96.],
            [20., 0., 1., 1., 100.]
        ])

    assert_array_equal(left_reach_100_40, overzichtl)


def test_right_reach():
    """test the right reach derivation
    """
    import numpy as np

    overzichtr, maxreachr = right_reach(np.array(perf_meas_example), 100, 40)

    right_reach_100_40 = np.array([
        [0, 1, 0, 1, 100],
        [1, 0, 1, np.nan, np.nan],
        [2, 0, 1, np.nan, np.nan],
        [3, 1, 0, 1, 100],
        [4, 1, 0, 1, 100],
        [5, 0, 1, np.nan, np.nan],
        [6, 0, 1, np.nan, np.nan],
        [7, 1, 0, 1, 100],
        [8, 1, 0, 1, 100],
        [9, 1, 0, 1, 100],
        [10, 1, 0, 1, 100],
        [11, 1, 0, 1, 100],
        [12, 0, 1, np.nan, np.nan],
        [13, 1, 0, 1, 100],
        [14, 1, 0, 1, 100],
        [15, 1, 0, 1, 100],
        [16, 1, 0, 1, 100],
        [17, 1, 0, 1, 100],
        [18, 0, 1, np.nan, np.nan],
        [19, 1, 0, 1, 100],
        [20, 1, 0, 1, 100]
        ])

    assert_array_equal(right_reach_100_40, overzichtr)

def test_breach_20():
    """resulting breaches for single parameter set (single line, 2D matrix)
    """
    import numpy as np

    rel_levels = np.array([0, 5, 10, 20, 40])
    breach = breach_run(np.array(perf_meas_example)[:1, :20], rel_levels)

    breach_1_20 = np.array([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
        [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
        [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
        [9, 10, 9, 10, 9, 10, 9, 10, 9, 10],
        [9, 10, 9, 10, 9, 10, 9, 10, 7, 10],
        [11, 11, 11, 11, 11, 11, 11, 11, 11, 11],
        [12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
        [13, 13, 13, 13, 13, 13, 13, 13, 13, 13],
        [14, 15, 14, 15, 14, 15, 14, 15, 14, 19],
        [14, 15, 14, 15, 14, 15, 14, 15, 14, 15],
        [16, 16, 16, 16, 16, 16, 16, 16, 16, 16],
        [17, 17, 17, 17, 17, 17, 17, 17, 17, 17],
        [18, 18, 18, 18, 18, 18, 18, 18, 18, 18],
        [19, 19, 19, 19, 19, 19, 19, 19, 19, 19],
        [20, 20, 20, 20, 20, 20, 20, 20, 20, 20]])

    assert_array_equal(breach_1_20, breach + 1)

def test_breach_100():
    """resulting breaches for full range
    """
    import numpy as np

    rel_levels = np.array([0, 5, 10, 20, 40])
    breach = breach_run(np.array(perf_meas_example), rel_levels)

    breach_100_40 = np.array([
        [0,5,0,5,0,5,0,7,0,40],
        [0,5,0,5,0,5,0,7,0,40],
        [0,5,0,5,0,5,0,7,0,40],
        [0,6,0,6,0,6,0,10,0,59],
        [0,7,0,7,0,7,0,9,0,59],
        [0,9,0,9,0,9,0,11,0,54],
        [3,11,3,11,3,11,3,11,0,21],
        [4,11,4,11,4,11,4,11,0,23],
        [5,11,5,11,5,11,5,11,2,54],
        [5,12,5,12,5,12,2,14,0,38],
        [6,12,6,12,6,12,2,12,0,29],
        [6,14,6,14,6,14,2,22,0,41],
        [9,15,9,15,9,15,9,17,0,38],
        [11,15,11,15,11,15,11,15,0,28],
        [11,15,11,15,11,15,11,15,0,17],
        [12,21,12,21,12,21,12,21,0,38],
        [15,21,15,21,15,21,15,22,0,34],
        [15,21,15,21,15,21,15,22,0,34],
        [15,21,15,21,15,21,12,21,0,28],
        [15,22,15,22,15,22,11,22,0,29],
        [15,22,15,22,15,22,8,22,0,30],
        [15,25,15,25,15,25,3,25,0,32],
        [19,25,19,25,19,25,16,25,4,33],
        [21,25,21,25,21,25,21,25,19,33],
        [21,27,21,27,21,27,19,30,0,36],
        [21,27,21,27,21,27,21,27,3,36],
        [24,28,24,28,24,28,24,28,3,33],
        [24,29,24,29,24,29,24,29,17,34],
        [26,30,26,30,26,30,26,30,20,33],
        [27,30,27,30,27,30,27,30,0,32],
        [28,33,28,33,28,33,28,47,0,63],
        [30,33,30,33,30,33,30,33,25,56],
        [30,36,30,36,30,36,30,39,30,81],
        [30,36,30,36,30,36,30,39,20,76],
        [32,36,32,36,32,36,32,36,24,76],
        [32,41,32,41,32,41,32,47,24,99],
        [32,44,32,44,32,46,32,47,24,99],
        [35,44,35,44,35,44,35,47,17,66],
        [35,44,35,44,35,44,30,46,15,66],
        [35,44,35,44,35,44,30,46,15,92],
        [35,44,35,44,35,44,30,46,1,92],
        [35,44,35,44,35,44,30,46,1,54],
        [36,46,36,46,36,46,36,49,29,76],
        [36,46,36,46,36,46,36,49,13,54],
        [36,48,36,48,36,48,36,48,1,55],
        [42,48,42,48,42,48,42,51,1,92],
        [42,48,42,48,42,48,42,48,20,92],
        [44,51,44,51,44,51,41,54,17,82],
        [44,51,44,51,44,51,41,54,15,54],
        [47,51,47,51,47,51,47,51,20,54],
        [47,51,47,51,47,51,45,51,41,82],
        [47,57,47,57,47,57,45,61,15,100],
        [51,57,51,57,51,57,51,59,32,100],
        [51,57,51,57,51,57,51,59,49,100],
        [51,57,51,57,51,57,51,59,15,100],
        [51,57,51,57,51,57,50,57,15,100],
        [51,58,51,58,51,58,50,58,46,77],
        [51,61,51,61,51,61,51,63,42,76],
        [56,61,56,61,56,61,56,63,55,100],
        [57,62,57,62,57,62,57,66,55,78],
        [57,63,57,63,57,63,55,63,50,76],
        [57,68,57,68,57,68,55,70,52,77],
        [59,69,59,69,59,69,57,74,49,86],
        [60,69,60,69,60,69,58,74,49,100],
        [61,69,61,69,61,69,59,71,44,100],
        [61,69,61,69,61,69,59,71,15,100],
        [61,69,61,69,61,69,61,71,2,100],
        [61,70,61,70,61,70,61,72,37,95],
        [61,70,61,70,61,70,56,70,38,95],
        [62,71,62,71,62,71,59,71,38,95],
        [67,71,67,71,67,71,67,71,37,73],
        [69,72,69,72,69,72,69,72,66,76],
        [71,74,71,74,71,74,71,74,69,93],
        [72,74,72,74,72,74,72,74,37,83],
        [72,78,72,78,72,78,72,83,37,95],
        [74,78,74,78,74,78,74,83,67,95],
        [74,80,74,80,74,80,74,83,67,96],
        [74,80,74,80,74,80,72,80,37,96],
        [74,80,74,80,74,80,72,80,37,100],
        [76,82,76,82,76,82,74,82,71,82],
        [76,83,76,83,76,83,76,83,69,100],
        [79,88,79,88,79,88,79,88,67,100],
        [79,88,79,88,79,88,79,88,67,100],
        [80,88,80,88,80,88,72,88,44,100],
        [81,88,81,88,81,88,78,88,70,90],
        [81,88,81,88,81,88,78,88,70,100],
        [81,89,81,89,81,89,76,91,64,95],
        [81,89,81,89,81,89,76,89,64,96],
        [81,89,81,89,81,89,76,89,64,96],
        [86,91,86,91,86,91,83,91,66,95],
        [89,91,89,91,89,91,89,91,79,93],
        [89,92,89,92,89,92,89,92,87,100],
        [91,95,91,95,91,95,91,97,83,100],
        [92,98,92,98,92,98,92,100,79,100],
        [92,98,92,98,92,98,92,100,86,100],
        [92,98,92,98,92,98,89,100,69,100],
        [93,100,93,100,93,100,93,100,66,100],
        [93,100,93,100,93,100,93,100,93,100],
        [93,100,93,100,93,100,93,100,64,100],
        [96,100,96,100,96,100,93,100,66,100],
        [96,100,96,100,96,100,93,100,66,100]])

    assert_array_equal(breach_100_40, breach)

