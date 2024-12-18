import tkinter as tk

window=tk.Tk()
window.title="row and coulmns"
window.geometry("300x300")
for i in range(3):
    for j in range(3):
        frame = tk.Frame(master=window,relief=tk.RAISED,borderwidth=5)
        frame.grid(row=i,column=j)
        label = tk.Label(master=frame, text=f"Row {i},\n Column {j}") 
        label.pack()  
tk.mainloop()     
        
        
        
        
