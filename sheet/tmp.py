from docx import Document
from docx.shared import Cm
import os
import glob

#os.remove('sheet.docx')

document = Document()

#margin

sections = document.sections
for section in sections:
    section.top_margin = Cm(0)
    section.bottom_margin = Cm(0)
    section.left_margin = Cm(0)
    section.right_margin = Cm(0)


imgs =  glob.glob("img/*.jpg")

print(len(imgs))

for img in imgs:
    document.add_picture(img, width=Cm(10))






document.save('sheet.docx')

