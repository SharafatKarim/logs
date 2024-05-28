+++
title = "Tkinter"
description = "```python
from tkinter import Label, Tk"
+++

# Tkinter

## Label

```python
from tkinter import Label, Tk

root= Tk()

myLabel = Label(root, text="Hello World!")
myLabel.pack() # Pack it into the window

root.mainloop() # Keep the window open
```

## Grid

```python
from tkinter import Label, Tk

root= Tk()

myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="I'm Sharafat!")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

root.mainloop() # Keep the window open
```

## Button

```python
from tkinter import Label, Tk, Button

root= Tk()

def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!")
    myLabel.pack()

aButon = Button(root, text="Click Me!", padx=50, pady=50, fg="blue", bg="#ffffff", command=myClick)

aButon.pack()

root.mainloop() # Keep the window open
```

## Entry

```python
from tkinter import Label, Tk, Button, Entry

root= Tk()

e = Entry(root, width=50, borderwidth=5)
e.pack()
e.insert(0, "Enter your name: ")

def myClick():
    myLabel = Label(root, text=e.get())
    myLabel.pack()

aButon = Button(root, text="Enter your name : ", padx=50, pady=50, fg="blue", bg="#ffffff", command=myClick)

aButon.pack()

root.mainloop() # Keep the window open

```

### A Simple Calculator

```python
from tkinter import Label, Tk, Button, Entry

root= Tk()
root.title("Simple calculator")
f_num = 0

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3)

def button_click_f(number):
    # e.delete(0, "END")
    current = e.get()
    e.delete(0, "end")
    e.insert(0, current + str(number))

def button_clear_f():
    e.delete(0, "end")
    global f_num
    f_num = 0

def button_equal_f():
    second_number = e.get()

    if math == "addition":
        e.delete(0, "end")
        e.insert(0, str(f_num + int(second_number)))
    if math == "subtraction":
        e.delete(0, "end")
        e.insert(0, str(f_num - int(second_number)))
    if math == "multiplication":
        e.delete(0, "end")
        e.insert(0, str(f_num * int(second_number)))
    if math == "division":
        e.delete(0, "end")
        e.insert(0, str(f_num / int(second_number)))

def button_add_f():
    first_number = e.get()
    e.delete(0, "end")
    global f_num 
    f_num += int(first_number)
    global math
    math = "addition"

def button_subtract_f():
    first_number = e.get()
    e.delete(0, "end")
    global f_num 
    f_num = int(first_number)
    global math
    math = "subtraction"

def button_multiply_f():
    first_number = e.get()
    e.delete(0, "end")
    global f_num 
    f_num = int(first_number)
    global math
    math = "multiplication"

def button_divide_f():
    first_number = e.get()
    e.delete(0, "end")
    global f_num 
    f_num = int(first_number)
    global math
    math = "division"

# Define buttons
button_1 = Button(root, text="1", padx=40, pady=20, fg="blue", bg="#ffffff", command=lambda: button_click_f(1))
button_2 = Button(root, text="2", padx=40, pady=20, fg="blue", bg="#ffffff", command=lambda: button_click_f(2))
button_3 = Button(root, text="3", padx=40, pady=20, fg="blue", bg="#ffffff", command=lambda: button_click_f(3))
button_4 = Button(root, text="4", padx=40, pady=20, fg="blue", bg="#ffffff", command=lambda: button_click_f(4))
button_5 = Button(root, text="5", padx=40, pady=20, fg="blue", bg="#ffffff", command=lambda: button_click_f(5))
button_6 = Button(root, text="6", padx=40, pady=20, fg="blue", bg="#ffffff", command=lambda: button_click_f(6))
button_7 = Button(root, text="7", padx=40, pady=20, fg="blue", bg="#ffffff", command=lambda: button_click_f(7))
button_8 = Button(root, text="8", padx=40, pady=20, fg="blue", bg="#ffffff", command=lambda: button_click_f(8))
button_9 = Button(root, text="9", padx=40, pady=20, fg="blue", bg="#ffffff", command=lambda: button_click_f(9))
button_0 = Button(root, text="0", padx=40, pady=20, fg="blue", bg="#ffffff", command=lambda: button_click_f(0))

button_add = Button(root, text="+", padx=40, pady=20, fg="blue", bg="#ffffff", command= button_add_f)
button_equal = Button(root, text="=", padx=40, pady=20, fg="blue", bg="#ffffff", command= button_equal_f)
button_clear = Button(root, text="clear", padx=28, pady=20, fg="blue", bg="#ffffff", command= button_clear_f)

button_subtract = Button(root, text="-", padx=40, pady=20, fg="blue", bg="#ffffff", command= button_subtract_f)
button_multiply = Button(root, text="*", padx=40, pady=20, fg="blue", bg="#ffffff", command= button_multiply_f)
button_divide = Button(root, text="/", padx=40, pady=20, fg="blue", bg="#ffffff", command= button_divide_f)

# putting buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=1)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1)
button_clear.grid(row=5, column=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

# aButon = Button(root, text="Enter your name : ", padx=50, pady=50, fg="blue", bg="#ffffff")
# aButon.grid(row=1, column=0)

root.mainloop() # Keep the window open
```

