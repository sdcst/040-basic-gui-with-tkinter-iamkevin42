import tkinter as tk
from PIL import Image, ImageTk


master = tk.Tk()
master.title("Example")
master.geometry("350x180")


image = Image.open('dog.png')
image = ImageTk.PhotoImage(image)
image_label = tk.Label(master, image=image)
image_label.grid(row=3, column=2)


canvas = tk.Canvas(master, width=200, height=100)
canvas.grid(row=4,column=2)
    
canvas.create_text(170, 10, text="Pochacco!", fill="black", font=("Arial", 10))

canvas.create_text(master,text="A cuddly little puppy")


master.mainloop()