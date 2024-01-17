import tkinter as tk
from tkinter import ttk
from screeninfo import get_monitors
import bible

output_dict = {}

def text_process(input_text):
    return bible.scripture(input_text)

def display_text_on_screen2(translation_var, book_var, chapter_var, verse_var, screen2_label, processed_label):
    # read from ui
    translation = translation_var.get()
    book = book_var.get()
    chapter = chapter_var.get()
    verse = verse_var.get()
    input_text = f"{translation} {book} {chapter} {verse}"
    res = text_process(input_text)

    global output_dict
    output_dict = res
    print('output_dict:', output_dict)

    processed_text = res['scripture']

    screen2_label.config(text=res['user_input'], anchor="w", justify="left")
    processed_label.config(text=processed_text)

def update_text_on_screen2(func, screen2_label, processed_label):
    global output_dict
    res = output_dict

    if func == 'prev':
        new_query = res['query'] - 1
    elif func == 'next':
        new_query = res['query'] + 1

    print('new_query:',new_query)

    
        
    # processed_text = bible.find_scripture(res['bible'], new_query)
    # print('processed_text:', processed_text)

    # output_dict = res
    # print('output_dict:', output_dict)

    # screen2_label.config(text=res['user_input'], anchor="w", justify="left")
    # processed_label.config(text=processed_text)

def create_window(screen, fullscreen=False, on_close=None):
    window = tk.Toplevel()
    window.geometry('+{}+{}'.format(screen.x, screen.y))
    
    if on_close:
        window.protocol("WM_DELETE_WINDOW", on_close)
        window.geometry('200x300')
    
    if fullscreen:
        window.attributes('-fullscreen', True)
        window.configure(bg='black')
        window.bind('<Escape>', lambda event: window.destroy())

    return window

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main root window

    monitors = get_monitors()
    
    if len(monitors) < 2:
        raise ValueError("Two monitors are required!")

    # Create window on Screen 1 and add input options and show button
    screen1 = monitors[0]
    screen1_window = create_window(screen1, on_close=root.quit)
    
    translation_var = tk.StringVar(value="GAE")
    translation_label = tk.Label(screen1_window, text="번역본")
    translation_label.pack()
    translation_dropdown = ttk.Combobox(screen1_window, textvariable=translation_var, values=["GAE", "KJV"], state="readonly")
    translation_dropdown.pack()
    
    book_var = tk.StringVar()
    book_label = tk.Label(screen1_window, text="성경")
    book_label.pack()
    book_entry = tk.Entry(screen1_window, textvariable=book_var)
    book_entry.pack()
    
    chapter_var = tk.StringVar()
    chapter_label = tk.Label(screen1_window, text="장")
    chapter_label.pack()
    chapter_entry = tk.Entry(screen1_window, textvariable=chapter_var)
    chapter_entry.pack()
    
    verse_var = tk.StringVar()
    verse_label = tk.Label(screen1_window, text="절")
    verse_label.pack()
    verse_entry = tk.Entry(screen1_window, textvariable=verse_var)
    verse_entry.pack()

    # Bind the Enter key to call display_text_on_screen2
    screen1_window.bind('<Return>', lambda event: display_text_on_screen2(translation_var, book_var, chapter_var, verse_var, screen2_label, processed_label))
    
    # Add button to show text on screen 2
    show_button = tk.Button(screen1_window, text="Show", command=lambda: display_text_on_screen2(translation_var, book_var, chapter_var, verse_var, screen2_label, processed_label))
    show_button.pack(pady=10)

    # Create window on Screen 2 in fullscreen with labels
    screen2 = monitors[1]
    screen2_window = create_window(screen2, fullscreen=True)

    screen2_label = tk.Label(screen2_window, font=('Arial', 70), bg='black', fg='white')
    screen2_label.place(relx=0.5, rely=0.1, anchor='n')

    processed_label_width = screen2.width * 0.9
    processed_label = tk.Label(screen2_window, font=('Arial', 70), bg='black', fg='white', wraplength=processed_label_width, anchor="w", justify="left")
    processed_label.place(relx=0.5, rely=0.25, anchor='n', width=processed_label_width)

    # Add '이전' and '다음' buttons
    prev_button = tk.Button(screen1_window, text="이전", command=lambda: update_text_on_screen2('prev', screen2_label, processed_label))
    prev_button.pack(side="left", padx=10)
    
    next_button = tk.Button(screen1_window, text="다음", command=lambda: update_text_on_screen2('next', screen2_label, processed_label))
    next_button.pack(side="left", padx=10)
    
    root.mainloop()

if __name__ == '__main__':
    main()
