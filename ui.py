from tkinter import *


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("QuiZzLer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        canvas = Canvas(width=800, height=526)
        canvas.config(bg=THEME_COLOR, highlightthickness=0)
        canvas.grid(row=0, column=0, columnspan=2)

        cross_image = PhotoImage(file="images/false.png")
        unknown_button = Button(image=cross_image, highlightthickness=0)
        unknown_button.grid(row=1, column=0)

        check_image = PhotoImage(file="images/true.png")
        known_button = Button(image=check_image, highlightthickness=0)
        known_button.grid(row=1, column=1)







        self.window.mainloop()