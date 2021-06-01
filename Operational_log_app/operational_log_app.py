import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class MainApplication:
    def __init__(self, master):
        master.title('Operational Log APP')
        master.geometry('500x695+0+0')
        master.resizable(False, False)
        
        self.style = ttk.Style()
        #self.style.configure('TFrame')
        self.style.configure('Header.TLabel', font=('Arial', 18, 'bold'))  
        self.style.configure('TButton')
        self.style.configure('TLabel', font=('Arial', 11))

        #Upper frame for handling the logo and title
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        
        self.logo = tk.PhotoImage(file = 'images/freia_logo.png').subsample(2, 2)
        ttk.Label(self.frame_header, image=self.logo).grid(row=0, column=0, rowspan=2)
        ttk.Label(self.frame_header, text = 'Operational Log', style = 'Header.TLabel').grid(row=0, column=1, padx=15, pady=15)
        ttk.Label(self.frame_header, wraplength = 250,
                  text = ('Welcome to the program to record data from the daily operations.\n\n'
                  'Please write your comments below.')).grid(row=1, column=1, padx=20, pady=20)
        
        #Lower frame for handling the content and save records
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text = 'Date:').grid(row=0, column=0, padx=5, pady=5, sticky='w')
        ttk.Label(self.frame_content, text = 'Name:').grid(row=0, column=1, padx=5, pady=5, sticky='w')
        ttk.Label(self.frame_content, text = 'Shift:').grid(row=2, column=0, padx=5, pady=5, sticky='w')
        ttk.Label(self.frame_content, text = 'Machine:').grid(row=2, column=1, padx=5, pady=5, sticky='w')
        ttk.Label(self.frame_content, text = 'Comments:').grid(row=4, column=0, padx=5, pady=5, sticky='w')


        self.entry_date = ttk.Entry(self.frame_content, width=30, font=('Arial', 10), justify='left')
        self.entry_name = ttk.Entry(self.frame_content, width=30, font=('Arial', 10), justify='left')
        self.entry_shift = ttk.Combobox(self.frame_content, values=['Day', 'Afternoon', 'Night'], textvariable=['Day'], width=28, font=('Arial', 10), justify='left')
        self.entry_machine = ttk.Combobox(self.frame_content, values=self.machine_list(), textvariable='Machine_1', width=28, font=('Arial', 10), justify='left')
        self.text_comments = tk.Text(self.frame_content, width=64, height=20, font=('Arial', 10))
        
        self.entry_date.grid(row=1, column=0)
        self.entry_name.grid(row=1, column=1)
        self.entry_shift.grid(row=3, column=0)
        self.entry_machine.grid(row=3, column=1, columnspan=1)
        self.text_comments.grid(row=5, column=0, columnspan=2, padx=5)

        ttk.Button(self.frame_content, text = 'Save Record', style='TButton',
                   command=self.save_record).grid(row=6, column=0, padx=5, pady=15, ipadx=10, sticky='e')
        ttk.Button(self.frame_content, text = 'Clear all', style='TButton',
                   command=self.clear).grid(row=6, column=1, padx=5, pady=15, ipadx=10, sticky='w')

    def machine_list(self):
        """Pre-defined list of machines"""
        return [f'Machine_{i}' for i in range(1, 16)]

    def save_record(self):
        """Save the date, name, shift, machine and comments from the entry forms"""
        print(f'Date: {self.entry_date.get()}')
        print(f'Name: {self.entry_name.get()}')
        print(f'Shift: {self.entry_shift.get()}')
        print(f'Machine: {self.entry_machine.get()}')
        print(f'Comments: {self.text_comments.get(1.0, tk.END)}')
        self.clear()
        messagebox.showinfo(title = 'Operational Log', message = 'Record saved!')
    
    def clear(self):
        """Clear the content from the entry fields"""
        self.entry_date.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_shift.delete(0, tk.END)
        self.entry_machine.delete(0, tk.END)
        self.text_comments.delete(1.0, tk.END) #==> Text index must start with 1
         
def main():
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()
    
if __name__ == "__main__": main()