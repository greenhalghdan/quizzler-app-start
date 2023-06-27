THEME_COLOR = "#375362"
from tkinter import *
class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.question = Canvas(width=300, height=250)
        self.question.create_text(140, 130, text="This is a question", font=("Arial", 20, "italic"))
        self.question.grid(column=1, row=1, columnspan=2, pady=20, padx=20)
        self.score = Label(text=f"Score 0", background=THEME_COLOR, fg="white",)
        self.score.grid(column=2, row=0, padx=20, pady=20)
        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img)
        self.false_button.grid(column=1, row=3, pady=20, padx=20)
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img)
        self.true_button.grid(column=2, row=3, pady=20, padx=20)
        self.window.mainloop()