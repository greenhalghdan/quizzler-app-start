
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
        self.question.config(bg="white")
        if self.quiz.still_has_questions():

            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.question.itemconfig(self.question_text, text=q_text)
        else:
            self.question.itemconfig(self.question_text, text=f"You have finished the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def submit_answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def submit_answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def give_feedback(self, is_right):
        if is_right:
            self.question.config(bg="green")
            self.window.after(1000, self.get_next_question)
        else:
            self.question.config(bg="red")
            self.window.after(1000, self.get_next_question)

    def next_question(self):
        self.get_next_question()

