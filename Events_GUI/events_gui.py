import tkinter as tk
from tkinter import ttk

class MainApplication(tk.Frame):
    """Application used to track events versus time"""
    
    #Initialize master and paned window
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.title('Events APP')
        self.paned_window = ttk.PanedWindow(master, orient=tk.HORIZONTAL)
        self.paned_window.pack(fill=tk.BOTH, expand=True)

    #Create Frames inside paned window
    def create_frames(self):
        self.frame1 = ttk.Frame(self.paned_window, width=200, height=500, relief=tk.SUNKEN)
        self.frame2 = ttk.Frame(self.paned_window, width=300, height=500, relief=tk.SUNKEN)
        self.paned_window.add(self.frame1, weight=2)
        self.paned_window.add(self.frame2, weight=3)
    
    #Initialize Widgets
    def create_widgets(self):
        self.button1 = ttk.Button(self.frame2, text='1', command=lambda: self.callback(1))
        self.button2 = ttk.Button(self.frame2, text='2', command=lambda: self.callback(2))
        self.button3 = ttk.Button(self.frame2, text='3', command=lambda: self.callback(3))
        self.button4 = ttk.Button(self.frame2, text='4', command=lambda: self.callback(4))
        self.button5 = ttk.Button(self.frame2, text='5', command=lambda: self.callback(5))
        self.button6 = ttk.Button(self.frame2, text='6', command=lambda: self.callback(6))
    
    #Position Widgets with grid
    def position_widgets(self):
        self.button1.grid(row=0, column=0, columnspan=1, padx=15, pady=20, ipadx=50)
        self.button2.grid(row=0, column=1, columnspan=1, padx=15, pady=20, ipadx=50)
        self.button3.grid(row=1, column=0, columnspan=1, padx=15, pady=20, ipadx=50)
        self.button4.grid(row=1, column=1, columnspan=1, padx=15, pady=20, ipadx=50)
        self.button5.grid(row=2, column=0, columnspan=1, padx=15, pady=20, ipadx=50)
        self.button6.grid(row=2, column=1, columnspan=1, padx=15, pady=20, ipadx=50)
    
    #Create callback fuction
    def callback(self, num):
        print(num)



def main():
    root = tk.Tk()
    app = MainApplication(root)
    app.create_frames()
    app.create_widgets()
    app.position_widgets()
    root.mainloop()

if __name__ == "__main__": main()