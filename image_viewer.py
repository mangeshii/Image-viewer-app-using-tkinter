import tkinter as tk
from tkinter import *
from PIL import ImageTk
from PIL import Image

root = tk.Tk()

my_img1 = ImageTk.PhotoImage(Image.open('eifel.jpeg'))
my_img2 = ImageTk.PhotoImage(Image.open('cat1.jpeg'))
my_img3 = ImageTk.PhotoImage(Image.open('cat2.jpeg'))
my_img4 = ImageTk.PhotoImage(Image.open('cat3.jpeg'))
my_img5 = ImageTk.PhotoImage(Image.open('cat4.jpeg'))
my_img6 = ImageTk.PhotoImage(Image.open('cat5.jpeg'))
  

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


my_list = [my_img1, my_img2, my_img3,my_img4,my_img5,my_img6]


def forward(number):
    global my_label
    global forward_button
    global back_button
    my_label.grid_forget()
    my_label = Label(image=my_list[number+1])
    my_label.grid(row=0, column=0, columnspan=3)

    forward_button = Button(root, text=">>", command=lambda: forward(number+1))
    forward_button.grid(row=1, column=2)

    back_button = Button(root, text="<<", command=lambda: forward(number-1))
    back_button.grid(row=1, column=0)


def back(number):
    global my_label
    global forward_button
    global back_button
    my_label.grid_forget()
    my_label = Label(image=my_list[number+1])
    my_label.grid(row=0, column=0, columnspan=3)

    forward_button = Button(root, text=">>", command=lambda: forward(number+1))
    forward_button.grid(row=1, column=2)

    back_button = Button(root, text="<<", command=lambda: forward(number-1))
    back_button.grid(row=1, column=0)

    if number == 0:
        back_button = Button(root, text='<<', state=DISABLED)


forward_button = Button(root, text=">>", command=lambda: forward(0))
exit_button = Button(root, text="Exit", command=root.quit)
back_button = Button(root, text="<<", command=back, state=DISABLED)


forward_button.grid(row=1, column=2)
exit_button.grid(row=1, column=1)
back_button.grid(row=1, column=0)

root.mainloop()
