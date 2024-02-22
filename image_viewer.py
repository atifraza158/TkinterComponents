from tkinter import *
from PIL import Image, ImageTk

def forward(image_number):
    global my_label
    global btn_forward
    global btn_back
    
    my_label.grid_forget()
    my_label = Label(root, image=images_list[image_number-1], height=400, width=600)
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))
    
    if image_number == 5:
        button_forward = Button(root, text=">>", state='disabled')
    
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    

def back(image_number):
    global my_label
    global btn_forward
    global btn_back
    
    my_label.grid_forget()
    my_label = Label(root, image=images_list[image_number-1], height=400, width=600)
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))
    
    if image_number == 1:
        button_back = Button(root, text="<<", state='disabled')
    
    
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


root = Tk()
root.title("Image Viewer")
root.resizable(0, 0)


my_img1 = ImageTk.PhotoImage(Image.open("imageViewerImages/img1.jpeg"))
my_img2 = ImageTk.PhotoImage(Image.open("imageViewerImages/img2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("imageViewerImages/img3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("imageViewerImages/img4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("imageViewerImages/img5.jpg"))
my_img6 = ImageTk.PhotoImage(Image.open("imageViewerImages/img6.jpg"))



images_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6]

my_label = Label(root, image=my_img1, height=400, width=600)
my_label.grid(row=0, column=0, columnspan=3)


button_back = Button(root, text="<<", command=lambda: back, state='disabled')
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))


button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1,)
button_forward.grid(row=1, column=2)


root.mainloop()