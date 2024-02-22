from tkinter import *

def getName():
    my_label = Label(root, text="Hello, " + email_input.get())
    my_label.pack()

root = Tk()
root.title("Input Fields")
root.geometry("600x400")

email_input = Entry(root, width=40,)
email_input.pack()

my_btn = Button(root, text="Enter Your Name", command=getName)
my_btn.pack(pady=(30, 10))

root.mainloop()