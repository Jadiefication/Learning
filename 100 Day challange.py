import tkinter as tk

root = tk.Tk()

root.geometry("1280x720")
root.title("test")

label = tk.Label(root, text="test", font=("Arial", 24))
label.pack(padx=10, pady=10)

textbox = tk.Entry(root, font=("Arial", 24), show=False)
textbox.pack()

frame = tk.Frame(root)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)

button = tk.Button(frame, text="Click me")
button.grid(row=0, column=0, sticky="nsew")

root.mainloop()