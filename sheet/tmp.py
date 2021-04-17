from docx import Document
from docx.shared import Cm
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx2pdf import convert
import os
import glob

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


imgs =  glob.glob("img/*.jpg")

print(len(imgs),"개의 악보가 있습니다.")

for img in imgs:
    document.add_picture(img, width=Cm(10))



document.save('sheet.docx')

#pdf
convert('sheet.docx')
convert('sheet.docx', 'sheet.pdf')
convert('/')
