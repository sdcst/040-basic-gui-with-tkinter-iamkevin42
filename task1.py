import tkinter as tk


root = tk.Tk()
root.title("Tk")


entry1 = tk.Entry(root)
entry1.pack(side=tk.LEFT, padx=5)
multiplication_sign = tk.Label(root, text="×")
multiplication_sign.pack(side=tk.LEFT)
entry2 = tk.Entry(root)
entry2.pack(side=tk.LEFT, padx=5)
equals_sign = tk.Label(root, text= "=")
equals_sign.pack(side=tk.LEFT)
entry3 = tk.Entry(root)
entry3.pack(side=tk.RIGHT, padx=5)




result_label = tk.Label(root, text="")
result_label.pack(side=tk.RIGHT, padx=5)

root.mainloop()