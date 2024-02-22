import tkinter as tk

def on_entry_click(event):
    if entry.get() == 'Enter your text here...':
        entry.delete(0, "end")
        entry.insert(0, '')
        entry.config(fg = 'black')

def on_focusout(event):
    if entry.get() == '':
        entry.insert(0, 'Enter your text here...')
        entry.config(fg = 'grey')

root = tk.Tk()
root.title("Placeholder Text Example")

# Create an entry widget
entry = tk.Entry(root, width=30, fg='grey')
entry.insert(0, 'Enter your text here...')
entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_focusout)
entry.pack(pady=10)

root.mainloop()
