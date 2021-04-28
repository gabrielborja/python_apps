import tkinter as tk
from tkinter import ttk

class MainApplication(tk.Frame):
    """Application used to track events versus time"""
    
    #Initialize master and paned window
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.paned_window = ttk.PanedWindow(master, orient=tk.HORIZONTAL)
        self.paned_window.pack(fill=tk.BOTH, expand=True)

    #Create Frames inside paned window
    def create_frames(self):
        self.frame1 = ttk.Frame(self.paned_window, width=100, height=500, relief=tk.SUNKEN)
        self.frame2 = ttk.Frame(self.paned_window, width=400, height=500, relief=tk.SUNKEN)
        self.paned_window.add(self.frame1, weight=1)
        self.paned_window.add(self.frame2, weight=4)
    
    


def main():
    root = tk.Tk()
    app = MainApplication(root)
    app.create_frames()
    #app.create_widgets()
    #app.position_widgets()
    root.mainloop()

if __name__ == "__main__": main()