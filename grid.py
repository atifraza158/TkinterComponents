from tkinter import *


root = Tk()
root.title("Python GUI")
root.geometry("600x400")
root.resizable(0, 0)

label1 = Label(root, text="Python GUI")
label2 = Label(root, text="I'm a Python Developer")


label1.grid(row=0, column=0)
label2.grid(row=1, column=0)

root.mainloop()