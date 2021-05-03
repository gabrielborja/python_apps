import tkinter as tk
from tkinter import ttk
from datetime import datetime

class MainApplication(tk.Frame):
    """Application used to track events versus time"""
    
    #Initialize master and paned window
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.title('Counter APP')
        self.paned_window = ttk.PanedWindow(master, orient=tk.HORIZONTAL)
        self.paned_window.pack(fill=tk.BOTH, expand=True)
        self.counter = tk.StringVar()

    #Create Frames inside paned window
    def create_frames(self):
        self.frame1 = ttk.Frame(self.paned_window, width=200, height=500, relief=tk.SUNKEN)
        self.frame2 = ttk.Frame(self.paned_window, width=300, height=500, relief=tk.SUNKEN)
        self.paned_window.add(self.frame1, weight=2)
        self.paned_window.add(self.frame2, weight=3)
    
    #Return current date and time
    def check_time(self):
        """Function used to return a datetime object with milliseconds precision"""
        return str(datetime.now())

    #Create callback fuction
    def register_events(self, num):
        """Callback factory. Calling it returns function with the current time and
        the number of the button pressed"""
        my_event = tk.StringVar()
        my_event = (self.check_time(), num)
        print(my_event)
        #def _callback():
        #    print(num)
        #return _callback
    
    def save_events(self, func):
        """Save events to a list of tuples"""
        pass

    #Initialize Widgets
    def create_buttons(self):
        #Create Listbox and Scrollar for from Frame 1
        self.listbox = tk.Listbox(self.frame1, bg='white', height=33, width=35)
        self.listbox.grid(row=0, column=0, rowspan=1, padx=10, pady=10)
        self.scroll = tk.Scrollbar(self.frame1)
        self.scroll.grid(row=0, column=1, rowspan=1, pady=10)

        #Configure Listbox and Scrollbar for from Frame 1
        self.listbox.configure(yscrollcommand=self.scroll.set)
        self.scroll.configure(command=self.listbox.yview)

        #Create Buttons for Frame 2
        names = (str(i) for i in range(36)) #Create str names for the buttons
        self.button = []
        for i, name in enumerate(names):
            self.button.append(ttk.Button(self.frame2, text=name, command=lambda: self.register_events(i)))
            row,col=divmod(i, 3) #Denominator marks max number of columns
            self.button[i].grid(row=row, column=col, columnspan=1, padx=10, pady=10, ipadx=15)
            self.button50 = ttk.Button(self.frame2, text='50', command=lambda: self.register_events(50))
            self.button50.grid(row=36, column=0, columnspan=1, padx=10, pady=10, ipadx=15)
        


def main():
    root = tk.Tk()
    app = MainApplication(root)
    app.create_frames()
    app.create_buttons()
    root.mainloop()

if __name__ == "__main__": main()