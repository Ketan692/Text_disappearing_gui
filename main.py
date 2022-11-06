from tkinter import Label, Tk, Text, Button
import random

tim = Tk()
tim.geometry("900x700+300+30")
tim.config(background="#C3FF99", padx=150, pady=20)
tim.title("DISAPPEARING TEXT APP")

count = 0


def change_color():
    colors = ["#E97777", "#8EC3B0", "#829460", "#B1AFFF", "#FA7070", "#937DC2"]
    a = random.choice(colors)
    heading.config(fg=a)
    tim.after(200, change_color)


def delete_text():
    my_text.delete("1.0", "end-1c")
    my_text.insert("end-1c", "")


def check_text():
    global result, count
    if result == my_text.get("1.0", "end-1c"):
        if count == 5:
            tim.after(200, delete_text)
            count += 1
        tim.after(1000, check_text)
        count += 1
    else:
        tim.after(1000, check_text)
        result = my_text.get("1.0", "end-1c")
        counter = 0



heading = Label(text="THE TEXT DISAPPEATING APP", font="courier 30 bold", fg="pink", bg="black")
heading.grid(row=0, column=0, pady=10)

warn = Label(text="your text will be disappeared by 5 seconds of inactivity.", font="courier 10 bold", fg="red")
warn.grid(row=1, column=0, pady=10)

result = ""
my_text = Text(width=51, height=20, font="courier 15 bold")
my_text.focus()
my_text.grid(row=2, column=0, pady=20)

change_color()
check_text()

tim.mainloop()