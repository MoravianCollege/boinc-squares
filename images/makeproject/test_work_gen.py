#!/usr/bin/env python
import sys
import boinc2docker_create_work as b2d
import time

"""
This program creates work based from a command line argument
Creates jobs for sets of 1000 numbers to be squared
:return:
"""
for job in range(int(sys.argv[1])):
    start = job * 1000
    end = start + 999
    command = "python app.py " + str(start) + " " + str(end)
    b2d.boinc2docker_create_work("wbrandes/boinc:v8", command)


