from subzero import setup, Executable
from setuptools import Extension
setup(
    name='myapp',
    entry_points={
        'console_scripts': [Executable('myapp = myapp.main:main')]
    },
    ext_modules=[
        Extension('myapp.cython_module', ['myapp/cython_module.pyx'])
    ],
)
