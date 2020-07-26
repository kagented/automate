import tkinter as tk
import tkinter.font as tkFont



window = tk.Tk()


window.attributes('-fullscreen', True)

window.bind("<F11>", lambda event: window.attributes("-fullscreen",
                                    not window.attributes("-fullscreen")))
window.bind("<Escape>", lambda event: window.attributes("-fullscreen", False))

window.title('Worship Assistant')

window.resizable(True, True)

window.configure(bg = 'black')

window.geometry('400x400')

scrt = '창세기 1장 1절'

verse = '태초에 하나님이 천지를 창조하시니라'

label1 = tk.Label(window, 
        text = scrt, 
        bg = 'black', 
        fg = 'white',
        font = ('HY 견고딕', 50, 'bold')
        )

label1.pack()

label2 = tk.Label(window, 
        text = verse, 
        bg = 'black', 
        fg = 'white',
        font = ('HY 견고딕', 50, 'bold')
        )

label2.pack()

window.mainloop()