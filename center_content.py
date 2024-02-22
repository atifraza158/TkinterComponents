import tkinter as tk

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

root = tk.Tk()
root.title("Centered Window")

# Set the size of the window
window_width = 400
window_height = 300

center_window(root, window_width, window_height)

# Create and center a label
label = tk.Label(root, text="Centered Label")
label.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()
