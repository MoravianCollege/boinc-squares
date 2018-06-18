#!/usr/bin/env python
import sys
import boinc2docker_create_work as b2d
import time

for job in range(10):
    start = job * 1000
    end = start + 999
    command = "python app.py " + str(start) + " " + str(end)
    b2d.boinc2docker_create_work("wbrandes/boinc:v8", command)
#bin/boinc2docker_create_work.py python:alpine python -c "print('Hello BOINC')"
