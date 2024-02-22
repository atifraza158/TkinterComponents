from tkinter import *

def myClick():
    my_label = Label(root, text="Button is Clicked...!")
    my_label.pack()

root = Tk()

root.title("Buttons")

my_btn = Button(root, text="Click Me", padx=50, command=myClick, fg="skyblue", bg='black')
my_btn.pack()
root.mainloop()