import os
from os import walk
import pprint

filelist = []


dirname = r'C:\Users\USER\Desktop\tmp'

dirlist = []


for root, dirs, files in os.walk(dirname):
    for file in files:
        dirlist.append(os.path.join(root, file))

print(len(dirlist))

dirlist = [x for x in dirlist
           if 'db' not in x]

print(len(dirlist))

#pprint.pprint(dirlist)
