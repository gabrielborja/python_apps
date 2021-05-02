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
        self.counter = {}

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
    def callback(self, num):
        """Callback factory. Calling it returns function with the number of the button pressed"""
        #def _get_button_clicked():
        #    self.counter.update({self.check_time(): num})
        #return _get_button_clicked
        return lambda: num
    
    def register_events(self):
        try:
            print(self.counter.update({self.check_time(): self.callback(num)}))
        except: TypeError()


        #def _callback():
        #    print(num)
        #return _callback

    #Initialize Widgets
    def create_buttons(self):
        names = (str(i+1) for i in range(36)) #Create str names for the buttons
        self.button = []
        for i, name in enumerate(names):
            self.button.append(ttk.Button(self.frame2, text=name, command=self.callback(i+1)))
            row,col=divmod(i, 3) #Denominator marks max number of columns
            self.button[i].grid(row=row, column=col, columnspan=1, padx=10, pady=10, ipadx=15)


def main():
    root = tk.Tk()
    app = MainApplication(root)
    app.create_frames()
    app.create_buttons()
    my_dict = app.register_events()
    print(my_dict)
    root.mainloop()

if __name__ == "__main__": main()