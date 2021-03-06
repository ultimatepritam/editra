# -*- coding: utf-8 -*-
# Setup script to build the PyShell plugin. To build the plugin
# just run 'python setup.py' and an egg will be built and put into 
# the plugin directory
"""Adds an interactive PyShell that can be opened in the Shelf. Multiple
instances can be opened in the Shelf at once.

"""

import sys
try:
    from setuptools import setup
except ImportError:
    print "You must have setup tools installed in order to build this plugin"
    setup = None

__author__ = "Cody Precord"

if setup != None:
    sys.argv.append("bdist_egg")
    sys.argv.append("--dist-dir=../.")
    setup(
        name='PyShell',
        version='0.4',
        description=__doc__,
        author=__author__,
        author_email="cprecord@editra.org",
        license="GPLv2",
        url="editra.org",
        platforms=["Linux", "OS X", "Windows"],
        packages=['pyshell'],
        entry_points='''
        [Editra.plugins]
        PyShell = pyshell:PyShell
        '''
        )
