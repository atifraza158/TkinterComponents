from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.iconbitmap("favicons/favicon1.ico")
quit_btn  = Button(root, text="Quit", command=root.quit)
quit_btn.pack()

my_img = ImageTk.PhotoImage(Image.open("images/img1.png"))
image_label = Label(root, image=my_img)
image_label.pack()


root.mainloop()