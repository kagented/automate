import os
import sys
import time
from langdetect import detect

#콘티 곡 제목 불러오기

f = open('test.txt', 'rt', encoding='UTF8')
lines = f.readlines()

filename = []

for line in lines:
    line = line.replace('\n', '')
    filename.append(line)

f.close()


#불러온 제목 검색

dirname = r'C:\Users\USER\Desktop\예배곡ppt'

dirlist = []

fileorder = 0

while fileorder < len(filename):
    for root, dirs, files in os.walk(dirname):
        for file in files:
            if file.startswith(filename[fileorder]):
                dirlist.append(os.path.join(root, file))
    fileorder = fileorder + 1

'''

print(dirlist)
print(len(dirlist))

dirlist = [ x for x in dirlist if x[-10] is not detect(x) == 'ko' ]

for dirname in dirlist:
    if detect(dirname[-6]) == 'ko':
        print(dirname)
        dirlist.remove(dirname)


print(dirlist)
print(len(dirlist))
'''

openorder = 0

while openorder < len(dirlist):
    os.system('start "" "'+dirlist[openorder]+'""')
    openorder = openorder + 1
    time.sleep(3)
