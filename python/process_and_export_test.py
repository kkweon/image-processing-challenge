from numpy.testing import assert_array_almost_equal
from process_and_export import rescale, threshold

from threshold import threshold_cpp
import numpy as np


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
