import tkinter as tk
from tkinter import ttk

class MainApplication(tk.Frame):
    """Application used to track events versus time"""
    
    #Initialize master and paned window
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.title('Counter APP')
        self.paned_window = ttk.PanedWindow(master, orient=tk.HORIZONTAL)
        self.paned_window.pack(fill=tk.BOTH, expand=True)

    #Create Frames inside paned window
    def create_frames(self):
        self.frame1 = ttk.Frame(self.paned_window, width=200, height=500, relief=tk.SUNKEN)
        self.frame2 = ttk.Frame(self.paned_window, width=300, height=500, relief=tk.SUNKEN)
        self.paned_window.add(self.frame1, weight=2)
        self.paned_window.add(self.frame2, weight=3)
    
    #Initialize Widgets
    #def create_widgets(self):
        #self.button1 = ttk.Button(self.frame2, text='1', command=lambda: self.callback(1))
        #self.button2 = ttk.Button(self.frame2, text='2', command=lambda: self.callback(2))
        #self.button3 = ttk.Button(self.frame2, text='3', command=lambda: self.callback(3))
        #self.button4 = ttk.Button(self.frame2, text='4', command=lambda: self.callback(4))
        #self.button5 = ttk.Button(self.frame2, text='5', command=lambda: self.callback(5))
        #self.button6 = ttk.Button(self.frame2, text='6', command=lambda: self.callback(6))
        #self.button7 = ttk.Button(self.frame2, text='7', command=lambda: self.callback(7))
        #self.button8 = ttk.Button(self.frame2, text='8', command=lambda: self.callback(8))
        #self.button9 = ttk.Button(self.frame2, text='9', command=lambda: self.callback(9))
        #self.button10 = ttk.Button(self.frame2, text='10', command=lambda: self.callback(10))
        #self.button11 = ttk.Button(self.frame2, text='11', command=lambda: self.callback(11))
        #self.button12 = ttk.Button(self.frame2, text='12', command=lambda: self.callback(12))
    
    #Create callback fuction
    def callback(self, num):
        """Callback factory. Calling it returns function with the number of the button pressed"""
        def _callback():
            print(num)
        return _callback

    #Initialize Widgets
    def create_widgets(self):
        names = (str(i+1) for i in range(36)) #Create str names for the buttons
        self.button = []
        for i, name in enumerate(names):
            self.button.append(ttk.Button(self.frame2, text=name, command=self.callback(i+1)))
            row,col=divmod(i, 3)
            self.button[i].grid(row=row, column=col, columnspan=1, padx=10, pady=10, ipadx=15)


def main():
    root = tk.Tk()
    app = MainApplication(root)
    app.create_frames()
    app.create_widgets()
    root.mainloop()

if __name__ == "__main__": main()