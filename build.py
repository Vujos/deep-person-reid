from setuptools import Extension, setup
from Cython.Build import cythonize
import numpy as np

def numpy_include():
    try:
        numpy_include = np.get_include()
    except AttributeError:
        numpy_include = np.get_numpy_include()
    return numpy_include

ext_modules = [
    Extension(
        'torchreid.metrics.rank_cylib.rank_cy',
        ['torchreid/metrics/rank_cylib/rank_cy.pyx'],
        include_dirs=[numpy_include()],
    )
]

setup(
    ext_modules=cythonize(ext_modules)
)
