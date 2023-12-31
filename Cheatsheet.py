import tkinter as tk
from tkinter import messagebox
from typing import Any

class App:
  
  def __init__(self):
    
    self.root = tk.Tk()
    
    self.menubar = tk.Menu(self.root)
    
    self.filemenu = tk.Menu(self.menubar, tearoff=0)
    self.filemenu.add_command(label="Close", command=self.on_closing)
    self.filemenu.add_separator()
    self.filemenu.add_command(label="Exit", command=exit)
    
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
    
    self.clearbutton = tk.Button(self.root, text="Clear", command=self.clear)
    self.clearbutton.pack()
    
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
      
  def clear(self):
    self.textbox.delete("1.0", "end")
    
#TODO:Make a calculator

class Calculator:
  
  def number_clicked(self, number: int):
    current_text = self.textbox.cget("text")
    if current_text == "0":
      self.textbox.config(text=str(number))
    else:
      self.textbox.config(text=current_text + str(number))
  
  def button(self, text: str, row: int, column: int, anchor: str="center", width: int=10, height: int=1, command: any=None):
    button = tk.Button(self.rt, text=text, width=width, height=height, command=command, font="Arial 12 bold")
    button.grid(row=row, column=column, sticky=anchor)
  
  def __init__(self):
    self.rt = tk.Tk()
    
    self.rt.geometry("500x800")
    
    self.rt.title("Calculator")
    
    self.textbox = tk.Label(self.rt, height=1, width=20, text="0", font="Arial 12 bold")
    self.textbox.grid(columnspan=4, column=0, row=0, sticky="nsew")
    
    for i in range(0, 4):
      self.rt.grid_rowconfigure(i, weight=0)
      self.rt.grid_columnconfigure(i, weight=0)
    
    self.button("7" ,1, 0, anchor="nw", width=10, height=2, command=lambda: self.number_clicked(7))
    self.button("8" ,1, 1, anchor="nw", width=10, height=2, command=lambda: self.number_clicked(8))
    self.button("9" ,1, 2, anchor="nw", width=10, height=2, command=lambda: self.number_clicked(9))
    self.button("4", 2, 0, anchor="nw", width=10, height=2, command=lambda: self.number_clicked(4))
    self.button("5" ,2, 1, anchor="nw", width=10, height=2, command=lambda: self.number_clicked(5))
    self.button("6" ,2, 2, anchor="nw", width=10, height=2, command=lambda: self.number_clicked(6))
    self.button("1", 3, 0, anchor="nw", width=10, height=2, command=lambda: self.number_clicked(1))
    self.button("2" ,3, 1, anchor="nw", width=10, height=2, command=lambda: self.number_clicked(2))
    self.button("3" ,3, 2, anchor="nw", width=10, height=2, command=lambda: self.number_clicked(3))
    self.button("0", 4, 1, anchor="nw", width=10, height=2, command=lambda: self.number_clicked(0))
    self.button("," ,4, 2, anchor="nw", width=10, height=2, command=lambda: self.textbox.config(text=self.textbox.cget("text") + str(",")))
    
    self.rt.mainloop()
  
if __name__ == "__main__":
  calculator = Calculator()