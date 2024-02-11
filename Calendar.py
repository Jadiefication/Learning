
import customtkinter as Ctk
import datetime

class App:
    
    def __init__(self):
        
        self.rt = Ctk.CTk()
        
        self.rt.geometry("500x800")
        
        self.rt.mainloop()
        
if __name__ == "__main__":
    app = App()