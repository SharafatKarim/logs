# Tkinter - Day two

## Icon and image

```python
from tkinter import Label, Tk, Button, Entry, PhotoImage
from PIL import Image, ImageTk

root= Tk()
root.title("Simple GUI with pythonian")
# root.iconbitmap("/home/sharafat/Desktop/test/python/tkinter/logo.png")

root.iconphoto(False, PhotoImage(file='logo.png'))

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

my_img = ImageTk.PhotoImage(Image.open("logo.png"))
Label(root, image=my_img).pack()

root.mainloop() # Keep the window open
```

## Image viewer

```python
from tkinter import Label, Tk, Button, Entry, PhotoImage, DISABLED
from PIL import Image, ImageTk

root= Tk()
root.title("Simple GUI with pythonian")
# root.iconbitmap("/home/sharafat/Desktop/test/python/tkinter/logo.png")

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.grid(row=0, column=0)

button_next = Button(root, text="Next", command=lambda: next(1))
button_next.grid(row=0, column=1)

button_back = Button(root, text="Back", command=lambda: back(1))
button_back.grid(row=0, column=2)

my_img_1 = ImageTk.PhotoImage(Image.open("1.png"))
my_img_2 = ImageTk.PhotoImage(Image.open("2.png"))
my_img_3 = ImageTk.PhotoImage(Image.open("3.png"))
my_img_4 = ImageTk.PhotoImage(Image.open("4.png"))

my_img_list = [my_img_1, my_img_2, my_img_3, my_img_4]

# Label(root, image=my_img_list[0]).grid(row=1, column=0, columnspan=3)
my_label = Label(image=my_img_list[0])
my_label.grid(row=1, column=0, columnspan=3)

def next(image_number):
    global my_label
    global button_next
    global button_back

    my_label.grid_forget()
    my_label = Label(image=my_img_list[image_number-1])
    button_next = Button(root, text="Next", command=lambda: next(image_number+1))
    button_back = Button(root, text="Back", command=lambda: back(image_number-1))

    if image_number == 4:
        button_next = Button(root, text="Next", state=DISABLED)

    my_label.grid(row=1, column=0, columnspan=3)
    button_back.grid(row=0, column=1)
    button_next.grid(row=0, column=2)

def back(image_number):
    global my_label
    global button_next
    global button_back

    my_label.grid_forget()
    my_label = Label(image=my_img_list[image_number-1])
    button_next = Button(root, text="Next", command=lambda: next(image_number+1))
    button_back = Button(root, text="Back", command=lambda: back(image_number-1))

    if image_number == 1:
        button_back = Button(root, text="Back", state=DISABLED)

    my_label.grid(row=1, column=0, columnspan=3)
    button_back.grid(row=0, column=1)
    button_next.grid(row=0, column=2)

root.mainloop() # Keep the window open
```
