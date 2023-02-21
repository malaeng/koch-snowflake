from distutils.core import setup
import py2exe
import turtle
import math

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    console = [{'script': "koch.py"}],
    zipfile = None,
)