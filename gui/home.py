import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# from bible import bible


root = tk.Tk()

#root.configure(bg = 'black')

root.title('Worship Assistant-Home')

root.resizable(True, True)

root.geometry('400x400')

def saveText():
        entry = bible.get()
        if len(entry) > 0:
                print(entry)
        newWindow = tk.Toplevel(root)
        newWindow.title('Worship Assistant-Proejected')
        newWindow.geometry('400x400')
        label1 = tk.Label(newWindow, text = entry)
        label1.pack()
        return entry

bible = Entry(root)
bible.pack()

enter = Button(root, text="Enter", command=saveText)
enter.pack()

# entry = saveText()

root.mainloop()
