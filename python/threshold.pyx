# distutils: language = c++
# distutils: sources = cpp/threshold.cpp

# Cython interface file for wrapping the object
#
#

from libcpp.vector cimport vector
from libcpp cimport bool
import numpy as np

# c++ interface to cython
cdef extern from "threshold.hpp":
    vector[vector[vector[bool]]] threshold(const vector[vector[vector[double]]]&, double)


def threshold_cpp(const vector[vector[vector[double]]]& m, double cutoff):
    return np.asarray(threshold(m, cutoff))
