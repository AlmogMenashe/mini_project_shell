#!/usr/bin/bash

# import OS module
import os
import sys
import argparse

# Get the path
#path = "/home/almog/Desktop"
path = sys.argv[1]
if (path == '-r'): 
	path = sys.argv[2]
	if len(sys.argv) != 3:
		sys.exit("Please run the 1 path only again")
	print("Recursive:")
	print("Files and Directories in '% s':" % path)
	# to store files in a list
	list = []
	# dirs=directories
	for (root, dirs, file) in os.walk(path):
		for f in file:
			print(f)
	
# If the path does not exist
if not os.path.isdir(path):
    print("This is not a path")
    sys.exit(1)
# If there is a second path
if len(sys.argv) != 2 and (sys.argv[1] != '-r'):
    sys.exit("Please run the 1 path only again")

        
print("Non-recursively:") 
# Get the list of all files and directories
obj = os.scandir(path)
 # List all files and directories in the specified path
print("Files and Directories in '% s':" % path)
for entry in obj:
    if entry.is_dir() or entry.is_file():
        print(entry.name)

# Argparse (with multiple args):
parser = argparse.ArgumentParser()
parser.add_argument('-r','--recursive',action='store_true',help='run recursively over all sub-directories')
args = parser.parse_args()



