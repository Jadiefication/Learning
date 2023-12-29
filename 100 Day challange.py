import tkinter as tk
from tkinter import messagebox

class App:
  
  def __init__(self):
    
    self.root = tk.Tk()
    
    self.menubar = tk.Menu(self.root)
    
    self.filemenu = tk.Menu(self.menubar, tearoff=0)
    self.filemenu.add_command(label="Close", command=exit)
    
    self.menubar.add_cascade(menu=self.filemenu, label="File")
    
    self.root.config(menu=self.menubar)
    
    self.text = tk.Label(self.root, text="Your message")
    self.text.pack()
    
    self.textbox = tk.Text(self.root, height=10, width=30)
    self.textbox.bind("<KeyPress>", self.key_press)
    self.textbox.pack()
    
    self.check_state = tk.IntVar()
    
    self.check = tk.Checkbutton(self.root, text="Check me", variable=self.check_state)
    self.check.pack()
    
    self.button = tk.Button(self.root, text="OK", command=self.show_message)
    self.button.pack()
    
    self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    self.root.mainloop()
  
  def show_message(self):
    if self.check_state.get() == 0:
      print(self.textbox.get("1.0", "end-1c"))
    else:
      messagebox.showinfo(title="Message", message=self.textbox.get("1.0", "end-1c"))
      
  def key_press(self, event):
    if event.state == 12 and event.keysym == "Return":
      self.show_message()
      
  def on_closing(self):
    if messagebox.askyesno(title="Quit?", message="Are you sure you want to quit?"):
      self.root.destroy()

if __name__ == "__main__":
  app = App()
    
