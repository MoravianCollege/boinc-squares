#!/usr/bin/env python
import sys, os, os.path, subprocess, math

"""
This program is a trivial validator that always passes.
This shows where the standard validation happens within the program.
"""


def lengthChecker(fileName):
    
    result = open(fileName, "r")
    counter = 0

    for line in result:
        counter += 1

    return counter == 999


def rangeChecker(fileName, squareOrcube):

    result = open(fileName, "r")
    start = 0
    end = 0
    counter = 0

    if squareOrcube == "square":
        print("It was a square")
        for line in result:
            if counter == 0: 
                start = math.sqrt(int(line))

            if counter == 998:
                end = math.sqrt(int(line))

            counter += 1

    elif squareOrcube == "cube":
        print("It was a cube")
        for line in result:
            if counter == 0: 
                start = int(line)**(1./3.)

            if counter == 998:
                end = int(line)**(1./3.)
                end = end+1

            counter += 1

    start = int(start)
    end = int(end)
    return (start + 998) == end

if sys.argv[1]!='--error':

    os.system("tar xzf " + str(sys.argv[1]))

    if os.path.exists("testCubeFile.txt"):

        if lengthChecker("testCubeFile.txt") and rangeChecker("testCubeFile.txt", "cube"):
            sys.exit(0)
        else:
            sys.exit(1)
    
    elif os.path.exists("output.txt"):

        if lengthChecker("output.txt") and rangeChecker("output.txt", "square"):
            sys.exit(0)
        else:
            sys.exit(1)

    else:
        sys.exit(1) 
