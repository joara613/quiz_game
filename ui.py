from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=30, pady=30, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, font=("Arial", 14,"normal"))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=260, bg="white", highlightthickness=0)
        self.quiz_text = self.canvas.create_text(150, 130, text="Quiz", fill="black", font=FONT, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        true_img = PhotoImage(file="./images/true.png")
        false_img = PhotoImage(file="./images/false.png")
        self.true_btn = Button(image=true_img, command=self.answer_true, highlightthickness=0)
        self.true_btn.grid(column=0, row=2)
        self.false_btn = Button(image=false_img, command=self.answer_false, highlightthickness=0)
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=question)
        else:
            self.canvas.itemconfig(self.quiz_text, text="You've reached the end of the quiz")
            self.false_btn.config(state="disabled")
            self.true_btn.config(state="disabled")


    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.canvas.update()
        self.window.after(1000, self.get_next_question)