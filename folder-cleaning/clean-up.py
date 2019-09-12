#!/usr/bin/env python3

# Documentation on how to clean up the file tree system (mainly for my own records/efforts)

# Modules: folderstats, scandir

# Local level folder/file names
import os
folder = '.'
filepaths = [os.path.join(folder, f) for f in os.listdir(folder)]

# Recursive version 
for (dirpath, dirnames, filenames) in os.walk('.'):
    for f in filenames:
        print('FILE :', os.path.join(dirpath, f))
    for d in dirnames:
        print('DIRECTORY :', os.path.join(dirpath, d))
