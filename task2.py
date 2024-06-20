import tkinter as tk
from tkinter.constants import TOP, WORD
from typing import Text
from PIL import Image, ImageTk


root = tk.Tk()
root.title("T-Town Veterinary Clinic Database")

root.geometry("500x275")

entry1 = tk.Entry(root)
entry1.grid(row=1, column=5)
image = Image.open('dog.png')
image = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=image)
image_label.grid(row=3, column=2)

button = tk.Button(root, text="Search by text")
button.grid(row=1,column=10)



canvas= tk.Canvas(root)

canvas.create_text(text="Client Database", fill="black", font=('Helvetica 15 bold'))
canvas.grid()


root.mainloop()