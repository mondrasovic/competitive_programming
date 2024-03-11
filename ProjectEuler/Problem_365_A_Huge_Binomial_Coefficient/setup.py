from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

extensions = [
    Extension(
        "solution",
        ["solution.pyx"],
        include_dirs=[np.get_include()],
        extra_compile_args=["-O3", "-march=native", "-flto"],  # Optimization flags
        extra_link_args=["-flto"],  # Link-time optimization flag
    )
]

setup(
    ext_modules=cythonize(extensions),
)