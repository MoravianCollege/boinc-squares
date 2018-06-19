#!/usr/bin/env python
import sys
import boinc2docker_create_work as b2d
import time

"""
This program creates work based from a command line argument
Creates jobs for sets of 100 numbers to be squared
:return:
"""
for job in range(int(sys.argv[1])):
    start = job * 100
    end = start + 99
    command = "python app.py " + str(start) + " " + str(end)
    b2d.boinc2docker_create_work("hauuuug/cube:v3", command)


