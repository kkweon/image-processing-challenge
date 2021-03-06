# Cython compile instructions

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy as np
# Use python setup.py build_ext --inplace
# to compile

ext_modules = [
    Extension(
        "python.threshold", ["python/threshold.pyx", "cpp/threshold.cpp"],
        language="c++",
        include_dirs=["cpp", np.get_include()],
        extra_compile_args=["-std=c++14"])
]
setup(
    name="imageprocessing",
    ext_modules=cythonize(ext_modules))
