import os
from glob import glob
from os import walk
import datetime as dt
 
filepath = r'C:\\data\\sheet\\악보'

dirlist = os.path.dirname(filepath)

print(dirlist)