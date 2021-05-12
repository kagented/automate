import os
import sys
import time
import win32com.client
from glob import glob
from os import walk

#콘티 곡 제목 불러오기

f = open('songlist.txt', 'rt', encoding='UTF8')
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


#피피티 바로 열기
'''
openorder = 0

while openorder < len(dirlist):
    os.system('start "" "'+dirlist[openorder]+'""')
    openorder = openorder + 1
    time.sleep(2)
'''


#피피티 병합

output = r'C:\Users\USER\Documents\GitHub\worship_helper\ppt\merged.pptx'

Application = win32com.client.Dispatch("PowerPoint.Application")
outputPresentation = Application.Presentations.Add() 
outputPresentation.SaveAs(output)

for file in dirlist:    
    currentPresentation = Application.Presentations.Open(file)
    currentPresentation.Slides.Range(range(1, currentPresentation.Slides.Count+1)).copy()
    Application.Presentations(output).Windows(1).Activate()    
    outputPresentation.Application.CommandBars.ExecuteMso("PasteSourceFormatting")    
    currentPresentation.Close()

outputPresentation.save()
outputPresentation.close()
#Application.Quit()

os.system('start '+ output)
