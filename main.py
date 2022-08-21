from tkinter import *
import time

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# COUNTDOWN
def start_timer():
    count_down(5 * 60)


def count_down(count):
    count_minute = int(count / 60)
    count_second = count % 60
    canvas.itemconfig(timer_text, text=count)
    if count > 0:
        window.after(1000, count_down, count - 1)


# WINDOW and LABELS
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 120, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
timer_label.grid(row=0, column=1)
checkmark_label = Label(pady=0, text="✔", font=("Arial", 14, "bold"), bg=YELLOW, fg=GREEN)
checkmark_label.grid(row=3, column=1)

# BUTTONS
start_button = Button(command=start_timer, highlightthickness=0, bg=YELLOW, text="Start", font=(FONT_NAME, 10, "bold"))
start_button.grid(row=2, column=0)
reset_button = Button(highlightthickness=0, bg=YELLOW, text="Reset", font=(FONT_NAME, 10, "bold"))
reset_button.grid(row=2, column=2)


window.mainloop()
