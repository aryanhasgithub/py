import tkinter as tk 
window = tk.Tk()
window.title("hello world")
window.geometry("300x300")

label = tk.Label(window, text="Hello, World!",fg="blue",bg="green")
label.pack()
button = tk.Button(text="bye world",fg="blue",bg="green")
button.pack()
tk.mainloop()
