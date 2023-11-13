from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#557C55"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pymodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200,height=223, bg=YELLOW, highlightthickness=0)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

check_mark = Label(text="✔", highlightthickness=0, fg=GREEN, bg=YELLOW, font=25)
check_mark.grid(column=1, row=3)

tomato_img = PhotoImage(file=r"C:\Users\User_\Downloads\pymodoro\tomato.png")

canvas.create_image(100, 112, image = tomato_img)
canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(column=1, row=1)

window.mainloop()