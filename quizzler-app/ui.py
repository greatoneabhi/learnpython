from tkinter import Button, Canvas, Label, PhotoImage, Tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150, 125, width=280, fill=THEME_COLOR, font=FONT
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)

        check_image = PhotoImage(file="./quizzler-app/images/true.png")
        self.true_btn = Button(
            image=check_image,
            border=0,
            highlightthickness=0,
            command=self.clicked_true,
        )
        self.true_btn.grid(row=2, column=0)

        cross_image = PhotoImage(file="./quizzler-app/images/false.png")
        self.false_btn = Button(
            image=cross_image,
            border=0,
            highlightthickness=0,
            command=self.clicked_false,
        )
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text="You've reached the end of the quiz."
            )
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def clicked_true(self):
        self.give_feedback(self.quiz.check_answer("True"))
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def clicked_false(self):
        self.give_feedback(self.quiz.check_answer("False"))
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
