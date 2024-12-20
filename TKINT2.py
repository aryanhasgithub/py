import tkinter as tk
root = tk.Tk()
root.geometry("300x300")


def topwin():
    top = tk.Toplevel(root)
    top.title("New Window")
    label = tk.Label(top, text="This is a new window")
    label.pack()
    top.geometry("300x300")
    top.mainloop()
    

button = tk.Button(root, text="Open New Window", command=topwin)
button.pack()
tk.mainloop()    
