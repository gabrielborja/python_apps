import tkinter as tk
from tkinter import ttk
from products import Product

class MainApplication(tk.Frame):
    """Initialize the main application for displaying the changeover time from one product to another"""
    
    #_PRODUCTS = ("Dai", "Krok", "Melk", "Milk", "Mint", "Mjol", "Ore", "Smi", "Schw")


    #Initialize master
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self._products = self.list_products()
        self._prod1 = tk.StringVar(value=self._products[0])
        self._prod2 = tk.StringVar(value=self._products[1])
        
    #Create main window object
    def create_window(self):
        self.master.title("Changeover App")
        #self.master.geometry("470x470")
        self.master.resizable(0,0)
        #master.config(bg="#ffffff")
    
    #Initialize list of available products
    def list_products(self):
        self._my_products = Product()
        return self._my_products.list_all_products()
       
    #Initialize Widgets
    def create_widgets(self):
        self._intro_text = tk.Label(self.master, text="Select from the dropdown list below to convert from " \
            "one product to another", justify="center", wraplength=250, font=('Arial', 14))
        self._combobox_one = ttk.Combobox(self.master, values=self.list_products(), textvariable=self._prod1)
        self._equal_sign = tk.Label(self.master, text=" = ", font=('Arial', 16))
        self._combobox_two = ttk.Combobox(self.master, state='readonly', values=self.list_products(), textvariable=self._prod2)
        self._convert_button = tk.Button(self.master, text='Convert', command=self.get_products, font=('Arial', 12))
        self._code_label = tk.Label(self.master, text='Code', width=8, font=('Arial', 12))
        self._group_label = tk.Label(self.master, text='Group', width=8, font=('Arial', 12))
        self._minutes_label = tk.Label(self.master, text='Minutes', width=8, font=('Arial', 12))
        self._code_output = tk.Entry(self.master, text='Hola')
        self._group_output = tk.Entry(self.master, text='Group')
        self._minutes_output = tk.Entry(self.master, text='Minutes')
        self._bottom_text = tk.Label(self.master, text='')
    
    #Position Widgets with grid
    def position_widgets(self):
        self._intro_text.grid(row=0, column=0, columnspan=3, padx=15, pady=20)
        self._combobox_one.grid(row=1, column=0, padx=15, pady=20)
        self._equal_sign.grid(row=1, column=1, padx=15, pady=20)
        self._combobox_two.grid(row=1, column=2, padx=15, pady=20)
        self._convert_button.grid(row=2, column=0, columnspan=3, padx=15, pady=20, ipadx=50)
        self._code_label.grid(row=3, column=0, padx=5, pady=5)
        self._group_label.grid(row=3, column=1, padx=5, pady=5)
        self._minutes_label.grid(row=3, column=2, padx=5, pady=5)
        self._code_output.grid(row=4, column=0, padx=5, pady=5)
        self._group_output.grid(row=4, column=1, padx=5, pady=5)
        self._minutes_output.grid(row=4, column=2, padx=5, pady=5)
        self._bottom_text.grid(row=5, column=0, columnspan=3, padx=5, pady=5)
    
    #Get products from dropdown list
    def get_products(self):
        self._prod1 = self._combobox_one.get()
        self._prod2 = self._combobox_two.get()
        return(self._prod1, self._prod2)


        

def main():
    root = tk.Tk()
    app = MainApplication(root)
    app.create_window()
    app.create_widgets()
    app.position_widgets()
    app.get_products()
    root.mainloop()

if __name__ == "__main__": main()