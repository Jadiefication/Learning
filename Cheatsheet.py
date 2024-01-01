# CustomTkinter
import customtkinter as CTk
    
#TODO:Make a calculator

class Calculator:
  
  def number_clicked(self, number: int):
    current_text = self.text.cget("text")
    if current_text == "0":
      self.text.configure(text=str(number))
    else:
      self.text.configure(text=current_text + str(number))
  
  def button(self, text: str, row: int, column: int, anchor: str="center", width: int=10, height: int=1, command: any=None):
    button = CTk.CTkButton(self.rt, text=text, width=width, height=height, command=command)
    button.grid(row=row, column=column, sticky=anchor)
  
  def __init__(self):
    
    self.rt = CTk.CTk()
    
    CTk.set_appearance_mode("System")
    CTk.set_default_color_theme("blue")
  
    self.rt.geometry("500x800")
    
    self.rt.title("Calculator")
    
    self.text = CTk.CTkLabel(self.rt, height=1, width=20, text="0")
    self.text.grid(columnspan=4, column=0, row=0, sticky="nsew")
    
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
    self.button("," ,4, 2, anchor="nw", width=10, height=2, command=lambda: self.text.configure(text=self.text.cget("text") + str(",")))
    
    self.rt.mainloop()
  
if __name__ == "__main__":
  calculator = Calculator()
  
