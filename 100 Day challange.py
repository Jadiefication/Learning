import tkinter as tk

root = tk.Tk()

root.geometry("1280x720")
root.title("test")

label = tk.Label(root, text="test", font=("Arial", 24))
label.pack(padx=10, pady=10)

root.mainloop()