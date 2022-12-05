import sys
sys.path.append(r'C:\GitHub\worship_assistant')

from bible import bible
from prayer import noon



def show_scripture():
    return bible.scripture()

def show_prayer():
    return noon.prayer()