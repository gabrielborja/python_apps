import tkinter as tk
from tkinter import ttk

class SingleFrame(tk.Frame):
    """Class used to initialize a single Frame"""
    
    #Initialize Frame
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent