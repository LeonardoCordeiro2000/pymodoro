﻿from distutils.cmd import Command
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#557C55"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 
def Reset_timer():
  window.after_cancel(TIMER)
  canvas.itemconfig(timer_text, text="00:00")
  title_label.config(text="Timer")
  check_mark.config(text="")
  global REPS
  REPS = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
   global REPS
   REPS += 1 
   
   if REPS % 8 == 0:
    title_label.config(text="Long Break!", fg=PINK)
    count_down(LONG_BREAK_MIN * 60)
   elif REPS % 2 == 0:
     title_label.config(text="Short breake!", fg=RED)
     count_down(SHORT_BREAK_MIN * 60)
   else:
     title_label.config(text="Work", fg=GREEN)
     count_down(WORK_MIN * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count / 60)
    
    count_sec = count % 60
    if count_sec < 10:
       count_sec = f"0{count_sec}"
        

    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    
    if count > 0:
     global TIMER
     TIMER = window.after(1000, count_down, count - 1)
    else:
      start_timer()
      marks = ""
      work_session = math.floor(REPS/2)
      for _ in range(work_session):
        marks += "✔"
      check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pymodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200,height=223, bg=YELLOW, highlightthickness=0)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, Command=Reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(highlightthickness=0, fg=GREEN, bg=YELLOW, font=25)
check_mark.grid(column=1, row=3)

tomato_img = PhotoImage(file=r"C:\Users\User_\Downloads\pymodoro\tomato.png")

canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(column=1, row=1)

window.mainloop()