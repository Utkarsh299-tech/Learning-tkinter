from tkinter import *


def button_clicked():
    print('You clicked on me!')


root = Tk()  # creates a window
root.geometry('720x480')  # widthxheight

title = Label(root, text="First Window", fg="#F94747", font=('', 32))
title.pack()

btn1 = Button(root, text='Click me!', command=button_clicked)
btn1.pack()  # a dynamic layout to show up the widgets
root.mainloop()  # loops the window until we close
