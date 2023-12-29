import tkinter as tk

class App:
  def __init__(self):
    self.root = tk.Tk()
    
    self.text = tk.Label(self.root, text="Your message")
    self.text.pack()
    
    self.textbox = tk.Text(self.root, height=10, width=30)
    self.textbox.pack()
    
    self.check_state = tk.IntVar()
    
    self.check = tk.Checkbutton(self.root, text="Check me", variable=self.check_state)
    self.check.pack()
    
    self.button = tk.Button(self.root, text="OK", command=self.show_message)
    self.button.pack()
    
    self.root.mainloop()
  
  def show_message(self):
    print(self.check_state.get())

if __name__ == "__main__":
  app = App()
    
