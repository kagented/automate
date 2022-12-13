import os
import win32com.client
from glob import glob
from os import walk
import datetime as dt
import pythoncom
import time

#콘티 곡 제목 불러오기
def get_name(req):
    #req = '/sheet 문들아머리들어라'
    # req = '/sheet 문들아머리들어라, 오소서진리의성령님'
    filename = []

    #from songlist.txt file
    # f = open(r'C:\\GitHub\\worship_assistant\\ppt\\songlist.txt', 'rt', encoding='UTF8')
    # lines = f.readlines()
    # for line in lines:
    #     line = line.replace('\n', '')
    #     filename.append(line)
    # f.close()

    #from request
    if len(req[5:].split(',')) == 1:
        filename.append(req[5:])
    else:
        for i in range(0, len(req[5:].split(','))):
            filename.append(req[5:].split(',')[i].strip())

    return filename



def get_file(filename):
    #불러온 제목 검색
    dirname = r'C:\\data\\ppt'

    dirlist = []


    fileorder = 0

    while fileorder < len(filename):
        for root, dirs, files in os.walk(dirname):
            for file in files:
                if file.startswith(filename[fileorder]):
                    dirlist.append(os.path.join(root, file))
        fileorder = fileorder + 1
        
    return dirlist


def merge_file(dirlist):
    #피피티 병합
    output = f'C:\\GitHub\\worship_assistant\\tmp\\merged_{dt.datetime.now().strftime("%Y_%m_%d")}.pptx'

    Application = win32com.client.Dispatch("PowerPoint.Application",pythoncom.CoInitialize())
    outputPresentation = Application.Presentations.Add() 
    outputPresentation.SaveAs(output)
    pagecount = 0

    for file in dirlist:    
        currentPresentation = Application.Presentations.Open(file)
        pagecount = currentPresentation.Slides.Count+1
        currentPresentation.Slides.Range(range(1, currentPresentation.Slides.Count+1)).copy()
        Application.Presentations(output).Windows(1).Activate()    
        outputPresentation.Application.CommandBars.ExecuteMso("PasteSourceFormatting")
        currentPresentation.Close()
        time.sleep(3)
        


    #add blank
        # outputPresentation.Slides.Add(pagecount, 1)
        

    outputPresentation.save()
    outputPresentation.close()
    Application.Quit()

    #os.system('start '+ output)
    return output
