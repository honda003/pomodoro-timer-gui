from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 10
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 8

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
counter = 0
check_counter = 0
time = None


def count_down():
    global counter, check_counter
    counter += 1
    if (counter % 8) == 0:
        timer(LONG_BREAK_MIN)
        timer_label.config(text="Long Break", fg=RED)
    elif(counter % 2) == 0:
        check_counter += 1
        check_mark.grid(column=1, row=3)
        if check_counter == 1:
            check_mark.config(text="✓")
        elif check_counter == 2:
            check_mark.config(text="✓✓")
        elif check_counter ==3:
            check_mark.config(text="✓✓✓")
        timer(SHORT_BREAK_MIN)
        timer_label.config(text="Short Break", fg=PINK)
    else:
        timer(WORK_MIN)
        timer_label.config(text="Work", fg=GREEN)


def timer(count):
    global time
    min_counter = math.floor(count/60)
    sec_counter = count % 60
    if sec_counter < 10:
        sec_counter = f"0{sec_counter}"
    canvas.itemconfig(x, text=f"{min_counter}:{sec_counter}")
    if count > 0:
        time = window.after(1000, timer, count-1)
    elif count == 0:
        count_down()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Tomato")
window.minsize(width=500, height=400)
window.config(padx=100, pady=100, bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
x = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 34, "bold"))
canvas.grid(column=1, row=2)
#timer label
timer_label = Label(text="Timer", fg=GREEN,bg=YELLOW, font=(FONT_NAME, 34, "bold"))
timer_label.grid(column=1, row=1)
#functions
check_mark = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))


def fn1():
    count_down()


def reset():
    global time, counter, check_counter
    counter = 0
    check_counter = 0
    window.after_cancel(time)
    canvas.itemconfig(x, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")




#start Button

start_button = Button(text="Start", command=fn1)
start_button.grid(column=0, row=3)
#reset button
reset_button = Button(text="Reset", command=reset)
reset_button.grid(column=3, row=3)
# my_label = Label(text="Timer", bg=GREEN, font=(FONT_NAME, 25, "normal"))
# my_label.grid(column=1, row=1)


window.mainloop()