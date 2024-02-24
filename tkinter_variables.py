from tkinter import *
from tkinter import ttk

def button_clicked():
    print(string_var.get())

root = Tk()
root.title("Tkinter Variables")

string_var = StringVar(value="test")


my_label = ttk.Label(master=root, text="label", textvariable=string_var,)
my_label.pack()

my_input = ttk.Entry(master=root, textvariable=string_var)
my_input.pack()

my_input2 = ttk.Entry(master=root, textvariable=string_var)
my_input2.pack()


my_button = ttk.Button(master=root, text="Click Me", command=button_clicked)
my_button.pack()



root.mainloop()