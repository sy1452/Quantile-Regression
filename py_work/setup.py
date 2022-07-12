#setup.py
from distutils.core import setup, Extension, DEBUG

qcd_module = Extension('qcd', sources = ['QCD.cpp'])

setup (name = 'qcd',
      version = '1.0',
      description = 'Python package with QCD code C++ extension',
      ext_modules = [qcd_module])