import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

from tkinter import *
import math

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    reps = 0

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=200, pady=100, bg=YELLOW)

def start_timer():
    global reps
    work_sec = 3
    short_break_sec = 1
    long_break_sec = 2


    if reps == 0 or reps == 2 or reps == 4:
        timer_label.config(fg=GREEN, text="Work")
        count_down(work_sec)
        print(reps)
    elif reps == 1 or reps == 3 or reps == 5:
        timer_label.config(fg=PINK, text="Break")
        count_down(short_break_sec)
        print(reps)
    elif reps == 6:
        timer_label.config(fg=RED, text="Break")
        count_down(long_break_sec)
        print(reps)

    reps += 1



def count_down(count):
    global reps
    min_time = math.floor(count / 60)
    sec_time = int(count % 60)

    if sec_time < 10:
        sec_time = f"0{sec_time}"

        if sec_time == 0:
            sec_time = "00"

    if reps == 1 and count == 0:
        check_mark.config(text="✅")
    if reps == 3 and count == 0:
        check_mark.config(text="✅✅")
    if reps == 5 and count == 0:
        check_mark.config(text="✅✅✅")

    canvas.itemconfig(timer_text, text=f"{min_time}:{sec_time}")

    if count == -1:
        if reps != 7:
            start_timer()
        elif reps == 7:
            canvas.itemconfig(timer_text, text="00:00")
            timer_label.config(text="Nice!\nYou completed whole session!", fg=GREEN, font=(FONT_NAME, 23, "bold"))
            reps = 0
    if count > -1:
        global timer
        timer = window.after(1000, count_down, count - 1) # after(delay, callback=None, *args)








canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) # 이미지 크기에 맞는 픽셀값, highlightthickness=0 는 테두리 제거(이미지 약간 이동함)
tomato_img = PhotoImage(file="tomato.png") # 이미지를 바로 가져올 수 없음.
canvas.create_image(100, 113, image=tomato_img) # 이미지 생성 그림의 중심 위치 지정, *args, **kwargs
timer_text = canvas.create_text(100, 123, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40), bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(bg=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()