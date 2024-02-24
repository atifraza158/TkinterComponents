from tkinter import *

root = Tk()
root.title("Frames in TKinter")

frame = LabelFrame(root, text="This is my frame", padx=50, pady=50)
frame.pack(padx=10, pady=10)

my_btn = Button(frame, text="Click Me", padx=4, pady=5)
my_btn2 = Button(frame, text="Don't Click Me", padx=4, pady=5)

# We Can use Grid inside the pack of frame
my_btn.grid(row=0, column=0)
my_btn2.grid(row=1, column=1)




root.mainloop()