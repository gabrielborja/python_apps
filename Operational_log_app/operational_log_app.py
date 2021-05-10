import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Feedback:

    def __init__(self, master):
        
        master.title('Operational Log APP')
        master.resizable(False, False)
        master.configure(background='#383838')
        
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#383838')
        self.style.configure('Header.TLabel', font=('Arial', 18, 'bold'))  
        self.style.configure('TButton')
        self.style.configure('TLabel', background='#383838', foreground='#C5E478', font=('Arial', 11))

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        
        self.logo = tk.PhotoImage(file = 'images/freia_logo.png')
        ttk.Label(self.frame_header, image=self.logo).grid(row=0, column=0, rowspan=2)
        ttk.Label(self.frame_header, text = 'Anlegg Driftslogg', style = 'Header.TLabel').grid(row=0, column=1, padx=15, pady=5)
        ttk.Label(self.frame_header, wraplength = 250,
                  text = ('Welcome to the program to record information for the Molding Line.\n\n'
                  'Please write down your comments below.')).grid(row=1, column=1, padx=20, pady=5)
        
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text = 'Shift:').grid(row=0, column=0, padx=5, pady=5, sticky='sw')
        ttk.Label(self.frame_content, text = 'Machine:').grid(row=0, column=1, padx=5, pady=5, sticky='sw')
        ttk.Label(self.frame_content, text = 'Comments:').grid(row=2, column=0, padx=5, pady=5, sticky='sw')
        
        self.entry_name = ttk.Entry(self.frame_content, width=24, font=('Arial', 10))
        self.entry_email = ttk.Entry(self.frame_content, width=24, font=('Arial', 10))
        self.text_comments = tk.Text(self.frame_content, width=50, height=10, font=('Arial', 10))
        
        self.entry_name.grid(row= 1, column=0, padx=5)
        self.entry_email.grid(row=1, column=1, padx=5)
        self.text_comments.grid(row=3, column=0, columnspan=2, padx=5)
        
        ttk.Button(self.frame_content, text = 'Submit', style='TButton',
                   command = self.submit).grid(row=4, column=0, padx=5, pady=15, sticky='e')
        ttk.Button(self.frame_content, text = 'Clear', style='TButton',
                   command = self.clear).grid(row=4, column=1, padx=5, pady=15, sticky='w')

    def submit(self):
        print('Name: {}'.format(self.entry_name.get()))
        print('Email: {}'.format(self.entry_email.get()))
        print('Comments: {}'.format(self.text_comments.get(1.0, tk.END)))
        self.clear()
        messagebox.showinfo(title = 'Explore California Feedback', message = 'Comments Submitted!')
    
    def clear(self):
        self.entry_name.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.text_comments.delete(1.0, tk.END)
         
def main():            
    
    root = tk.Tk()
    feedback = Feedback(root)
    root.mainloop()
    
if __name__ == "__main__": main()