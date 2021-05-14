import os
import sys
import time
import win32com.client
from glob import glob
from os import walk
import shutil

#콘티 곡 제목 불러오기

f = open('songlist.txt', 'rt', encoding='UTF8')
lines = f.readlines()

filename = []

for line in lines:
    line = line.replace('\n', '')
    filename.append(line)

f.close()



#불러온 제목 검색
dirname = r'C:\Users\USER\Desktop\악보'

dirlist = []


fileorder = 0

while fileorder < len(filename):
    for root, dirs, files in os.walk(dirname):
        for file in files:
            if filename[fileorder] in file:              
                dirlist.append(os.path.join(root, file))
    fileorder = fileorder + 1

print(dirlist)


#악보 복사

copyorder = 0

target = r'C:\Users\USER\Documents\GitHub\worship_helper\sheet\search\img'

while copyorder < len(dirlist):
    shutil.copy(dirlist[copyorder], target)
    copyorder = copyorder + 1
    
    time.sleep(2)

'''

#바로 열기

openorder = 0

while openorder < len(dirlist):
    os.system('start "" "'+dirlist[openorder]+'""')

    openorder = openorder + 1
    
    time.sleep(2)

'''
