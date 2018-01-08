# distutils: language = c++
# distutils: sources = cpp/threshold.cpp

# Cython interface file for wrapping the object
#
#

from libcpp.vector cimport vector
from libcpp cimport bool
import numpy as np
cimport numpy as np
import cython

# c++ interface to cython
cdef extern from "threshold.hpp":
    vector[vector[vector[bool]]] threshold(const vector[vector[vector[double]]]&, double)
    vector[vector[vector[bool]]] threshold_use_ptr(double*, int, int, int, double)


@cython.boundscheck(False)
@cython.wraparound(False)
def threshold_cpp(np.ndarray[double, ndim=3, mode="c"] m not None, double cutoff):
    return np.asarray(threshold(m, cutoff))

@cython.boundscheck(False)
@cython.wraparound(False)
def threshold_cpp_ptr(np.ndarray[double, ndim=3, mode="c"] m not None, double cutoff):
    cdef int w, h, d
    w, h, d = m.shape[0], m.shape[1], m.shape[2]
    return np.asarray(threshold_use_ptr(<double*> m.data, w, h, d, cutoff))
