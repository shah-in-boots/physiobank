#!/usr/bin/env python

# Modules needed to analyze the filetree system
import os
import scandir
import folderstats
import pandas

# Approach using base modules
folder = '.'
filepaths = [os.path.join(folder, f) for f in os.listdir(folder)]

# Scandir is faster than general path analysis
filepaths = [f.path for f in os.scandir('.') if f.is_file()]
dirpaths  = [f.path for f in os.scandir('.') if f.is_dir()]

# Using recursive method to analyze the directory system
for (dirpath, dirnames, filenames) in os.walk('.'):
    for f in filenames:
        print('FILE :', os.path.join(dirpath, f))
    for d in dirnames:
        print('DIRECTORY :', os.path.join(dirpath, d))

# Using folderstats module for analysis
df = folderstats.folderstats('/', ignore_hidden = True)
