#!/usr/bin/bash

# import OS module
import os
import sys
import hashlib

# Get the path
#path = "/home/almog/Desktop/test2"
path = sys.argv[1]
number = 1
    
# If the path does not exist
if not os.path.isdir(path):
    print("This is not a path")
    sys.exit(1)
# If there is a second path
if len(sys.argv) != 2:
    sys.exit("Please run the 1 path only again")
        
# List all files and directories in the specified path
for root, dirs,files in os.walk(path, topdown=True):
    for name in files:
        #print(os.path.join(root, name))
        FileName = (os.path.join(root, name))

        hasher = hashlib.md5()
        with open(str(FileName), 'rb') as afile:
            buf = afile.read()
            hasher.update(buf)
        print('%s, ./%s,' %(number,name),hasher.hexdigest())
        number +=1
        print(name)


