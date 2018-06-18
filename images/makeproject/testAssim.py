#!/usr/bin/env python

import sys, tarfile, os

"""
This program does the assimilation for Boinc. 
It creates a master file of squares and adds the results of all of the work to the file.
:return:
"""

if sys.argv[1]!='--error':

	filename = "/root/project/bin/mastersquare.csv" 

	if !os.path.exists(filename):
		append_write = 'w'
	else: 
		append_write = 'a'

	master = open(filename, append_write)
        os.system("tar xzf " + str(sys.argv[1]))
        file = open("output.txt", "r")
        for line in file:
                master.write(line)

        file.close()
        master.close()
