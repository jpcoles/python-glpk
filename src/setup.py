import os
from distutils.core import setup, Extension

# Directory containing libglpk
GLPK_LIB_DIR = os.environ.get('GLPK_LIB_DIR', '/usr/lib')

# Directory containing glpk.h
GLPK_INC_DIR = os.environ.get('GLPK_INC_DIR', '/usr/include')

glpkpi = Extension('_glpkpi', libraries = ['glpk'],
                 include_dirs = [ GLPK_INC_DIR ],
                 library_dirs = [ GLPK_LIB_DIR ],
                 sources = ['swig/glpkpi_wrap.c', 'swig/glpkpi.c'] )
extmods = [glpkpi];

setup (name = 'glpk', 
    description = 'Python-glpk package',
    version = '0.4.43', 
    long_description = """
Python-glpk is a free software package providing bindings in the
Python programming language for the GLPK linear and integer
optimization package.  Its main purpose is to make the development of
software for optimization applications straightforward by building on
Python's extensive standard library and on the strengths of Python as
a high-level programming language.

Original url http://www.dcc.fc.up.pt/~jpp/code/python-glpk""", 
    author = 'Jonathan Coles  Original authors: J.P. Pedroso and F. Brandao',
    author_email = 'jonathan@jpcoles.com  Original authors: jpp@fc.up.pt, fdabrandao@gmail.com',
    url = "https://github.com/jpcoles/python-glpk",
    license = 'GNU GPL version 3',
    ext_package = "glpk",
    ext_modules = extmods,
    package_dir = {"glpk": "python"},
    packages = ["glpk"])
