import tkinter as tk

class App:
  def __init__(self):
    self.root = tk.Tk()
    
    self.text = tk.label(self.root, text="Your message")
    self.text.pack()
    
    self.textbox = tk.Text(self.root, height=10, width=30)
    self.textbox.pack()
    
    self.check = tk.Checkbutton(self.root, text="Check me")
    self.check.pack()
    
    self.root.mainloop()