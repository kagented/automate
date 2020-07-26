import tkinter as tk
import tkinter.font as tkFont



window = tk.Tk()


window.title('Worship Assistant')

window.resizable(True, True)

window.geometry('400x400')

label1 = tk.Label(window, 
        text = '기본 화면', 
        font = ('HY 견고딕', 50, 'bold')
        )

label1.pack()

window.mainloop()
