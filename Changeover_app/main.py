import tkinter as tk
from tkinter import ttk

class MainApplication(tk.Frame):
    """Class used to initialize the main application for displaying the changeover time from one product to another"""
    
    _PRODUCTS = ("Dai", "Krok", "Melk", "Milk", "Mint", "Mjol", "Ore", "Smi", "Schw")

    #Initialize master
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
    
    #Create main window object
    def create_window(self):
        self.master.title("Changeover App")
        self.master.geometry("600x600")
        self.master.resizable(0,0)
        #master.config(bg="#ffffff")
        
    #Initialize Widgets
    def create_widgets(self):
        self._intro_text = tk.Label(self.master, text="Select from the dropdown lists below to convert the changeover " \
            "time of different products", justify="center", wraplength=250, font=("Monospace", 10))
        self._combobox_one = ttk.Combobox(self.master, value=self._PRODUCTS)
        self._equal_sign = tk.Label(self.master, text=" = ")
        self._combobox_two = ttk.Combobox(self.master, value=self._PRODUCTS)
        self._convert_button = tk.Button(self.master, text='Convert')
    
    #Position Widgets with grid
    def position_widgets(self):
        self._intro_text.grid(row=0, column=0, columnspan=3, padx=10, pady=20)
        self._combobox_one.grid(row=1, column=0, padx=10, pady=20, sticky="W")
        self._equal_sign.grid(row=1, column=1, padx=10, pady=20)
        self._combobox_two.grid(row=1, column=2, padx=10, pady=20, sticky="E")
        self._convert_button.grid(row=2, column=0, columnspan=3, padx=10, pady=20, ipadx=50)
        

def main():
    root = tk.Tk()
    app = MainApplication(root)
    app.create_window()
    app.create_widgets()
    app.position_widget()
    root.mainloop()

if __name__ == "__main__": main()