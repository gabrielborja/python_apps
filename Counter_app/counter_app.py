import tkinter as tk
from tkinter import ttk
from datetime import datetime

class MainApplication(tk.Frame):
    """Python GUI Application used to track events versus time"""
    
    def __init__(self, master, *args, **kwargs):
        """Initialize master and paned window"""
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.title('Counter APP')
        self.paned_window = ttk.PanedWindow(master, orient=tk.HORIZONTAL)
        self.paned_window.pack(fill=tk.BOTH, expand=True)
        self._buttons = []
        self._events_counter = [] #Initialize empty list to store button events

    def check_time(self):
        """Returns the current datetime"""
        return (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def display_records(self):
        """Display the list of buttons clicked"""
        self.listbox.delete(0, tk.END)
        return [self.listbox.insert(tk.END, '\n'.join(str(i))) for i in self._events_counter]

    def add_event(self, num):
        """Callback factory. Calling it returns the current time, the number of
        the button pressed and displays the list of buttons clicked"""
        return lambda: (self._events_counter.append((self.check_time(), num)), self.display_records())
        #def _callback():
        #    self._events_counter.append((self.check_time(), num))
        #return _callback
    
    def create_frames(self):
        """Create frames inside paned window"""
        self.frame1 = ttk.Frame(self.paned_window, width=200, height=500, relief=tk.SUNKEN)
        self.frame2 = ttk.Frame(self.paned_window, width=300, height=500, relief=tk.SUNKEN)
        self.paned_window.add(self.frame1, weight=2)
        self.paned_window.add(self.frame2, weight=3)

    def create_widgets(self):
        """Initialize Listbox and Scrollbar"""
        self.listbox = tk.Listbox(self.frame1, bg='white', height=33, width=35)
        self.listbox.grid(row=0, column=0, rowspan=1, padx=10, pady=10)
        self.scroll = tk.Scrollbar(self.frame1)
        self.scroll.grid(row=0, column=1, rowspan=1, pady=10)
        self.listbox.configure(yscrollcommand=self.scroll.set)
        self.scroll.configure(command=self.listbox.yview)
    
    def create_buttons(self):
        """Initialize buttons for Frame 2"""
        names = (str(i) for i in range(36)) #Create str names for the buttons
        #self.button = []
        for i, name in enumerate(names):
            self._buttons.append(ttk.Button(self.frame2, text=name, command=self.add_event(i)))
            row,col=divmod(i, 3) #Denominator marks max number of columns
            self._buttons[i].grid(row=row, column=col, columnspan=1, padx=10, pady=10, ipadx=15)
        #self.button50 = ttk.Button(self.frame2, text='50', command=lambda: self.add_event(50))
        #self.button50.grid(row=36, column=0, columnspan=1, padx=10, pady=10, ipadx=15)


def main():
    root = tk.Tk()
    app = MainApplication(root)
    app.create_frames()
    app.create_widgets()
    app.create_buttons()
    app.display_records()
    root.mainloop()
    print(app._events_counter)

if __name__ == "__main__": main()