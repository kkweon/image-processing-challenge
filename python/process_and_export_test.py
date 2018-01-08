from datetime import datetime

import numpy as np
import pytest
from numpy.testing import assert_array_almost_equal

from process_and_export import rescale, threshold
from threshold import threshold_cpp


def test_rescale_shrink():
    image = np.array([51., 102., 153.])
    out = rescale(image, output_min=0.0, output_max=1.0)
    assert_array_almost_equal(out, [0.0, 0.5, 1.0])


def test_rescale_shrink_and_shift():
    image = np.array([51., 102., 153.])
    out = rescale(image, output_min=0.5, output_max=1.0)
    assert_array_almost_equal(out, [0.5, 0.75, 1.0])


def test_cpp_function():
    image = np.random.randn(32, 32, 32)
    cutoff = 0.5
    assert_array_almost_equal(
        threshold(image, cutoff), threshold_cpp(image, cutoff))


@pytest.mark.xfail
def test_cpp_function_should_be_faster():
    def timeit(func):
        beg = datetime.now()
        func()
        end = datetime.now()
        return end - beg

    image = np.random.randn(128, 128, 128)
    cutoff = 0.5

    python_fn = lambda: threshold(image, cutoff)
    cpp_fn = lambda: threshold_cpp(image, cutoff)

    assert timeit(python_fn) > timeit(cpp_fn)
