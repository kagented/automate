from docx import Document
from docx.shared import Cm
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx2pdf import convert
import os
import glob
from shutil import copyfile

#콘티 곡 제목 불러오기

f = open('songlist.txt', 'rt', encoding='UTF8')
lines = f.readlines()

filename = []

for line in lines:
    line = line.replace('\n', '')
    filename.append(line)

f.close()


#불러온 제목 검색
dirname = r'C:\Users\USER\Documents\GitHub\worship_helper\sheet\search\sheet_db'

dirlist = []


fileorder = 0

while fileorder < len(filename):
    for root, dirs, files in os.walk(dirname):
        for file in files:
            if filename[fileorder] in file:              
                dirlist.append(os.path.join(root, file))
    fileorder = fileorder + 1

print(dirlist)


#os.remove('sheet.docx')

document = Document()

#column

section = document.sections[0]

sectPr = section._sectPr
cols = sectPr.xpath('./w:cols')[0]
cols.set(qn('w:num'),'2')

#margin

sections = document.sections
for section in sections:
    section.top_margin = Cm(0)
    section.bottom_margin = Cm(0)
    section.left_margin = Cm(0)
    section.right_margin = Cm(0)

#copy image files to tmp directory

for imgdir in dirlist:
    copyfile(imgdir, '\img')

#create msword document

imgs =  glob.glob("img/*.jpg")

print(len(imgs),"개의 악보가 있습니다.")

for img in imgs:
    document.add_picture(img, width=Cm(10))



document.save('sheet.docx')

#pdf
convert('sheet.docx')
convert('sheet.docx', 'sheet.pdf')
convert('/')
