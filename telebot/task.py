import sys
sys.path.append(r'C:\GitHub\worship_assistant')

from bible import bible
from prayer import noon
from ppt import ppt


def show_scripture():
    return bible.scripture()

def show_prayer():
    return noon.prayer()

def get_ppt(req):
    filename = ppt.get_name(req)
    dirlist = ppt.get_file(filename)
    merged = ppt.merge_file(dirlist)
    return merged