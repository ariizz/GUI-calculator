import tkinter as tk

calculation = "" 

def add_calcu(symbol):
    global calculation
    calculation += str(symbol)
    text.delete(1.0, "end")
    text.insert(1.0, calculation)

def clear():
    global calculation
    calculation = ""
    text.delete(1.0, "end")
    

def evaluate():
    global calculation
    try:
        calculation = str(eval(calculation))
        text.delete(1.0, "end")
        text.insert(1.0, calculation)

    except:
        clear()
        text.insert(1.0, "Error")
    

win = tk.Tk()
win.title("CALCULATOR")
win.geometry("300x270")
win.configure(bg="#02081C")

text = tk.Text(win, height=2, width=17, font=("Arian", 24), bg="#0d1634", fg="white")
text.grid(columnspan=5)

# numbers

btn1 = tk.Button(win, text=1, command=lambda: add_calcu(1), bg="#02081C", width=10, height=2, highlightthickness=0, fg="white")
btn1.grid(row=1, column=0, padx=0, pady=0)
btn2 = tk.Button(win, text=2, command=lambda: add_calcu(2), bg="#02081C", width=10, height=2, highlightthickness=0, fg="white")
btn2.grid(row=1, column=1, padx=0, pady=0)
btn3 = tk.Button(win, text=3, command=lambda: add_calcu(3), bg="#02081C", width=10, height=2, highlightthickness=0, fg="white")
btn3.grid(row=1, column=2, padx=0, pady=0)
btn4 = tk.Button(win, text=4, command=lambda: add_calcu(4), bg="#02081C", width=10, height=2, highlightthickness=0, fg="white")
btn4.grid(row=2, column=0, padx=0, pady=0)
btn5 = tk.Button(win, text=5, command=lambda: add_calcu(5), bg="#02081C", width=10, height=2, highlightthickness=0, fg="white")
btn5.grid(row=2, column=1, padx=0, pady=0)
btn6 = tk.Button(win, text=6, command=lambda: add_calcu(6), bg="#02081C", width=10, height=2, highlightthickness=0, fg="white")
btn6.grid(row=2, column=2, padx=0, pady=0)
btn7 = tk.Button(win, text=7, command=lambda: add_calcu(7), bg="#02081C", width=10, height=2, highlightthickness=0, fg="white")
btn7.grid(row=3, column=0, padx=0, pady=0)
btn8 = tk.Button(win, text=8, command=lambda: add_calcu(8), bg="#02081C", width=10, height=2, highlightthickness=0, fg="white")
btn8.grid(row=3, column=1, padx=0, pady=0)
btn9 = tk.Button(win, text=9, command=lambda: add_calcu(9), bg="#02081C", width=10, height=2, highlightthickness=0, fg="white")
btn9.grid(row=3, column=2, padx=0, pady=0)
btn0 = tk.Button(win, text=0, command=lambda: add_calcu(0), bg="#02081C", width=10, height=2, highlightthickness=0, fg="white")
btn0.grid(row=4, column=1, padx=0, pady=0)

# operators
plus = tk.Button(win, text="+", command=lambda: add_calcu("+"), bg="#02081C", width=10, height=2, highlightthickness=0, fg="white")
plus.grid(row=1, column=3, padx=0, pady=0)
minus = tk.Button(win, text="-", command=lambda: add_calcu("-"), bg="#02081C", width=10, height=2, highlightthickness=0, fg="white")
minus.grid(row=2, column=3, padx=0, pady=0)
mul = tk.Button(win, text="x", command=lambda: add_calcu("*"), bg="#02081C", width=10, height=2, highlightthickness=0, fg="white")
mul.grid(row=3, column=3, padx=0, pady=0)
divi = tk.Button(win, text="/", command=lambda: add_calcu("/"), bg="#02081C", width=10, height=2, highlightthickness=0, fg="white")
divi.grid(row=4, column=3, padx=0, pady=0)

# parenthisis
p1=tk.Button(win, text="(", bg="#02081C",command=lambda: add_calcu("("), width=10, height=2, highlightthickness=0, fg="white")
p1.grid(row=4, column=0, padx=0, pady=0)

p2=tk.Button(win, text=")", bg="#02081C",command=lambda: add_calcu(")"), width=10, height=2, highlightthickness=0, fg="white")
p2.grid(row=4, column=2, padx=0, pady=0)

# clear
clr = tk.Button(win, text="C", width=21, bg="#02081C", command=clear, height=2, highlightthickness=0, fg="white")
clr.grid(row=5, column=0, columnspan=2, padx=0, pady=0)

# equal

eql = tk.Button(win, text="=", width=21, command=evaluate, bg="#02081C", height=2, highlightthickness=0, fg="white")
eql.grid(row=5, column=2, columnspan=2, padx=0, pady=0)

win.mainloop()