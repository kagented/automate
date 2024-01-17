import tkinter as tk
import pandas as pd

class BibleApp:
    def __init__(self, root):
        self.root = root
        self.load_data()
        self.create_input_window()
        self.output_window = None
        self.current_id = None
        self.book_dict = {1: ['창세기', '창'], 2: ['출애굽기', '출'], 3: ['레위기', '레'], 4: ['민수기', '민'], 5: ['신명기', '신'], 6: ['여호수아', '수'], 7: ['사사기', '삿'], 8: ['룻기', '룻'], 9: ['사무엘상', '삼상'], 10: ['사무엘하', '삼하'], 11: ['열왕기상', '왕상'], 12: ['열왕기하', '왕하'], 13: ['역대상', '대상'], 14: ['역대하', '대하'], 15: ['에스라', '스'], 16: ['느헤미야', '느'], 17: ['에스더', '에'], 18: ['욥기', '욥'], 19: ['시편', '시'], 20: ['잠언', '잠'], 21: ['전도서', '전'], 22: ['아가', '아'], 23: ['이사야', '사'], 24: ['예레미야', '렘'], 25: ['예레미야애가', '애'], 26: ['에스겔', '겔'], 27: ['다니엘', '단'], 28: ['호세아', '호'], 29: ['요엘', '욜'], 30: ['아모스', '암'], 31: ['오바댜', '옵'], 32: ['요나', '욘'], 33: ['미가', '미'], 34: ['나훔', '나'], 35: ['하박국', '합'], 36: ['스바냐', '습'], 37: ['학개', '학'], 38: ['스가랴', '슥'], 39: ['말라기', '말'], 40: ['마태복음', '마'], 41: ['마가복음', '막'], 42: ['누가복음', '눅'], 43: ['요한복음', '요'], 44: ['사도행전', '행'], 45: ['로마서', '롬'], 46: ['고린도전서', '고전'], 47: ['고린도후서', '고후'], 48: ['갈라디아서', '갈'], 49: ['에베소서', '엡'], 51: ['골로새서', '골'], 52: ['데살로니가전서', '살전'], 53: ['데살로니가후서', '살후'], 54: ['디모데전서', '딤전'], 55: ['디모데후서', '딤후'], 56: ['디도서', '딛'], 57: ['빌레몬서', '빌'], 58: ['히브리서', '히'], 59: ['야고보서', '약'], 60: ['베드로전서', '벧전'], 61: ['베드로후서', '벧후'], 62: ['요한일서', '요1'], 63: ['요한이서', '요2'], 64: ['요한삼서', '요3'], 65: ['유다서', '유'], 66: ['요한계시록', '계']}


    def load_data(self):
        # Load data from CSV file
        self.data = pd.read_csv('./bibleshow/gae.csv', encoding='CP949')

    def create_input_window(self):
        self.input_window = tk.Toplevel(self.root)
        self.input_window.title("말씀출력기")

        # Creating input fields
        tk.Label(self.input_window, text="성경:").grid(row=0, column=0)
        self.book_input = tk.Entry(self.input_window)
        self.book_input.grid(row=0, column=1)

        tk.Label(self.input_window, text="장:").grid(row=1, column=0)
        self.chapter_input = tk.Entry(self.input_window)
        self.chapter_input.grid(row=1, column=1)

        tk.Label(self.input_window, text="절:").grid(row=2, column=0)
        self.verse_input = tk.Entry(self.input_window)
        self.verse_input.grid(row=2, column=1)

        # Navigation buttons
        tk.Button(self.input_window, text="이전", command=lambda: self.navigate_verse(-1)).grid(row=3, column=0)
        tk.Button(self.input_window, text="다음", command=lambda: self.navigate_verse(1)).grid(row=3, column=1)

        tk.Button(self.input_window, text="출력", command=self.display_verse).grid(row=4, columnspan=2)

        # Bind the closing of the input window to also exit the program
        self.input_window.protocol("WM_DELETE_WINDOW", self.exit_program)

    def exit_program(self):
        self.root.destroy()

    def close_windows(self):
        if self.output_window:
            self.output_window.destroy()
        self.input_window.destroy()

    def display_verse(self):
        book_input = self.book_input.get()
        chapter = self.chapter_input.get()
        verse = self.verse_input.get()

        # Convert book input to numeric value
        book = self.convert_book_input(book_input)

        if book and self.fetch_verse(book, chapter, verse):
            if not self.output_window or not tk.Toplevel.winfo_exists(self.output_window):
                self.create_output_window()
            else:
                self.update_display(self.current_verse_label, self.current_verse_text)


    def convert_book_input(self, input_book):
        for key, value in self.book_dict.items():
            if input_book in value:
                return key
            elif input_book == value[0]:  # Check if the input matches the full name
                return key
        return None

    def create_output_window(self):
        self.output_window = tk.Toplevel(self.root)
        self.output_window.title("출력화면")
        self.output_window.attributes('-fullscreen', True)
        self.output_window.configure(background='black')
        self.output_window.bind("<Escape>", self.close_output_window)

        # Book, Chapter, Verse Label
        self.book_chapter_verse_label = tk.Label(self.output_window, font=('Arial', 70), bg='black', fg='white')
        self.book_chapter_verse_label.place(relx=0.5, rely=0.1, anchor='n')

        # Verse Text Label
        self.versetext_label_width = self.output_window.winfo_screenwidth() * 0.9
        self.versetext_label = tk.Label(self.output_window, font=('Arial', 70), bg='black', fg='white', wraplength=self.versetext_label_width, anchor="w", justify="left")
        self.versetext_label.place(relx=0.5, rely=0.25, anchor='n', width=self.versetext_label_width)

        self.update_display(self.current_verse_label, self.current_verse_text)

    def close_output_window(self, event=None):
        self.output_window.destroy()
        self.output_window = None


    def fetch_verse(self, book, chapter, verse):
        try:
            book = int(book)
            chapter = int(chapter)
            verse = int(verse)
            filtered_data = self.data[(self.data['b'] == book) & (self.data['c'] == chapter) & (self.data['v'] == verse)]
            if not filtered_data.empty:
                verse_text = filtered_data.iloc[0]['t']
                self.current_id = filtered_data.iloc[0]['id']
                book_name = self.book_dict.get(book, ["Unknown"])[0]
                self.current_verse_label = f"{book_name} {chapter}장 {verse}절"
                self.current_verse_text = verse_text
                return True
            else:
                self.current_verse_label = ""
                self.current_verse_text = "말씀구절 없음"
                self.current_id = None
                return False
        except ValueError:
            self.current_verse_label = ""
            self.current_verse_text = "잘못된 입력값"
            return False

    def update_display(self, label_text, verse_text):
        if self.output_window and tk.Toplevel.winfo_exists(self.output_window):
            self.book_chapter_verse_label.config(text=label_text)
            self.versetext_label.config(text=verse_text)
        
        # Update book_input field with the converted book name
        self.book_input.delete(0, tk.END)
        self.book_input.insert(0, label_text.split()[0])  # Extract the book name from the label


    def navigate_verse(self, direction):
        if self.current_id is not None:
            new_id = self.current_id + direction
            if new_id > 0 and new_id <= self.data['id'].max():
                new_verse_data = self.data[self.data['id'] == new_id]
                if not new_verse_data.empty:
                    self.current_id = new_id
                    new_book = new_verse_data.iloc[0]['b']
                    new_chapter = new_verse_data.iloc[0]['c']
                    new_verse = new_verse_data.iloc[0]['v']
                    new_text = new_verse_data.iloc[0]['t']
                    book_name = self.book_dict.get(new_book, ["Unknown"])[0]
                    self.current_verse_label = f"{book_name} {new_chapter}장 {new_verse}절"
                    self.current_verse_text = new_text

                    # Update input fields
                    self.book_input.delete(0, tk.END)
                    self.book_input.insert(0, str(book_name))
                    self.chapter_input.delete(0, tk.END)
                    self.chapter_input.insert(0, str(new_chapter))
                    self.verse_input.delete(0, tk.END)
                    self.verse_input.insert(0, str(new_verse))

                    # Update display
                    self.update_display(self.current_verse_label, self.current_verse_text)
                else:
                    self.update_display("", "말씀구절 없음")
            else:
                self.update_display("", "말씀구절 없음")
        else:
            self.update_display("", "말씀 위치를 입력해주세요")

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    app = BibleApp(root)
    root.mainloop()
