
THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.question = Canvas(width=300, height=250)
        self.question_text = self.question.create_text(150, 125,width=280 , text="This is a question", font=("Arial", 20, "italic"))
        self.question.grid(column=1, row=1, columnspan=2, pady=20, padx=20)
        self.score = Label(text=f"Score 0", background=THEME_COLOR, fg="white",)
        self.score.grid(column=2, row=0, padx=20, pady=20)
        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.submit_answer_false)
        self.false_button.grid(column=1, row=3, pady=20, padx=20)
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.submit_answer_true)
        self.true_button.grid(column=2, row=3, pady=20, padx=20)
        self.get_next_question()

        self.window.mainloop()
    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.question.itemconfig(self.question_text, text=q_text)

    def submit_answer_false(self):
        QuizBrain.check_answer(self.quiz, user_answer="False")
        self.get_next_question()

    def submit_answer_true(self):
        QuizBrain.check_answer(self.quiz, user_answer="True")
        self.get_next_question()
