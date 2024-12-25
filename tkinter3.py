import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk




root = tk.Tk()
root.geometry("300x300")
root.title("denomination calculator ")
image_path = "img.jpg"   
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

# Add the image to a label
image_label = tk.Label(root, image=photo)
image_label.pack() 

def msg():
    msgbox = messagebox.showinfo("do you want to start the calculator")
    if msgbox == "ok":
        topwin()
        
    
button= tk.Button(root,text="Start calculating",command=msg)
def topwin():
    top = tk.Toplevel()
    top.title("Denomination Calculator")
    top.geometry("250x300")  # Set a fixed size for the window

    label = tk.Label(top, text="Enter amount:")
    label.pack(pady=(10, 5))
    amount = tk.Entry(top)
    amount.pack()

    result_frame = tk.Frame(top)
    result_frame.pack(pady=10)

    labels = ["2000", "500", "200"]
    result_labels = []

    for i, label_text in enumerate(labels):
        label = tk.Label(result_frame, text=label_text)
        label.grid(row=i, column=0, padx=5, pady=2, sticky="e")
        result_label = tk.Label(result_frame, bg="white", width=10)
        result_label.grid(row=i, column=1, padx=5, pady=2, sticky="w")
        result_labels.append(result_label)

    def calculate():
        try:
            amt = int(amount.get())
            denominations = [2000, 500, 200]
            results = []

            for denomination in denominations:
                count = amt // denomination
                amt %= denomination
                results.append(str(count))

            for label, result in zip(result_labels, results):
                label.config(text=result)

        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid integer amount.")

    calc_button = tk.Button(top, text="Calculate", command=calculate)
    calc_button.pack(pady=10)


button.pack()
root.mainloop()
            
        
        
            
    



