import tkinter as tk
from tkinter import ttk

class ComboBox(tk.Frame):
    """Class used to initialize a Combobox"""
    
    _PRODUCTS = ("Dai", "Krok", "Melk", "Milk", "Mint", "Mjol", "Ore", "Smi", "Schw")

    #Initialize Combobox
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        parent = ttk.Combobox(parent, value=self._PRODUCTS, width=20, justify="center")