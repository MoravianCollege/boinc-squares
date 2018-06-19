#!/usr/bin/env python
import sys, os, os.path, subprocess

"""
This program is a trivial validator that always passes.
This shows where the standard validation happens within the program.
"""

if sys.argv[1]!='--error':

    for arg in sys.argv:
        print(arg)

    sys.exit(0)
