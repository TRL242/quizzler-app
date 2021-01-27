from tkinter import *


THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("QuiZzLer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=300, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            150,
            text="Question Text.",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        check_image = PhotoImage(file="images/true.png")
        self.known_button = Button(image=check_image, highlightthickness=0)
        self.known_button.grid(row=2, column=0)


        cross_image = PhotoImage(file="images/false.png")
        self.unknown_button = Button(image=cross_image, highlightthickness=0)
        self.unknown_button.grid(row=2, column=1)









        self.window.mainloop()