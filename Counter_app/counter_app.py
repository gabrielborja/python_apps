import tkinter as tk
from tkinter import ttk
from datetime import datetime
import csv

class MainApplication(tk.Frame):
    """Python GUI Application used to track events versus time"""
    
    def __init__(self, master, *args, **kwargs):
        """Initialize master and paned window"""
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.title('Counter APP')
        self.paned_window = ttk.PanedWindow(master, orient=tk.HORIZONTAL)
        self.paned_window.pack(fill=tk.BOTH, expand=True)
        self._buttons = [] #Initialize empty list to store tkk Buttons
        self._events_counter = [] #Initialize empty list to store button events

    def check_time(self):
        """Returns the current datetime"""
        return (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def display_records(self):
        """Display the list of buttons clicked"""
        self.listbox.delete(0, tk.END)
        self.count_label.configure(text=f'Count: {len(self._events_counter)}')
        return [self.listbox.insert(tk.END, '\n'.join(str(val))) for val in reversed(self._events_counter)]

    def add_event(self, num):
        """Callback factory. Calling it returns the current time, the number of
        the button pressed and displays the list of buttons clicked"""
        return lambda: (self._events_counter.append((self.check_time(), num)), self.display_records())
    
    def save_to_csv(self):
        """Save list of events to a csv file"""
        csv_columns = ['Time','Num']
        time_str = str(self.check_time()[:15].replace(":", "_")) #Turning current time into file name.
        with open(f'{time_str}_count.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([i for i in csv_columns]) #Writing the column headers at the top of the csv file
            for event in self._events_counter:
                writer.writerow([*event]) #Writing values to the csv file
        print('\nThe file was saved successfully...')
    
    def create_frames(self):
        """Create frames inside paned window"""
        self.frame1 = ttk.Frame(self.paned_window, width=200, height=500, relief=tk.SUNKEN)
        self.frame2 = ttk.Frame(self.paned_window, width=300, height=500, relief=tk.SUNKEN)
        self.paned_window.add(self.frame1, weight=2)
        self.paned_window.add(self.frame2, weight=3)

    def create_widgets(self):
        """Initialize widgets for Frame 1"""
        self.top_label = ttk.Label(self.frame1, text='List of events', font=('Arial', 15))
        self.top_label.grid(row=0, column=0, padx=10, pady=10)
        self.listbox = tk.Listbox(self.frame1, bg='white', height=24, width=35)
        self.listbox.grid(row=1, column=0, padx=10, pady=2)
        self.scrollbar = ttk.Scrollbar(self.frame1, orient=tk.VERTICAL)
        self.scrollbar.grid(row=1, column=1, padx=2, sticky='ns')
        self.listbox.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.listbox.yview)
        self.count_label = ttk.Label(self.frame1, text='Count:')
        self.count_label.grid(row=2, column=0, pady=3)
        self.save_button = ttk.Button(self.frame1, text='Save', command=self.save_to_csv)
        self.save_button.grid(row=3, column=0, padx=10, pady=10)
        
    def create_buttons(self):
        """Initialize buttons for Frame 2"""
        names = (str(i) for i in range(36)) #Create str names for the buttons
        for i, name in enumerate(names):
            self._buttons.append(ttk.Button(self.frame2, text=name, command=self.add_event(i)))
            row,col=divmod(i, 3) #Denominator marks max number of columns
            self._buttons[i].grid(row=row, column=col, columnspan=1, padx=10, pady=10, ipadx=15)

def main():
    root = tk.Tk()
    app = MainApplication(root)
    app.create_frames()
    app.create_widgets()
    app.create_buttons()
    root.mainloop()

if __name__ == "__main__": main()