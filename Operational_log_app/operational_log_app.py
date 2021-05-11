import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Feedback:

    def __init__(self, master):
        
        master.title('Operational Log APP')
        master.geometry('500x615')
        master.resizable(False, False)
        
        self.style = ttk.Style()
        #self.style.configure('TFrame')
        self.style.configure('Header.TLabel', font=('Arial', 18, 'bold'))  
        self.style.configure('TButton')
        self.style.configure('TLabel', font=('Arial', 11))

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        
        self.logo = tk.PhotoImage(file = 'images/freia_logo.png').subsample(2, 2)
        ttk.Label(self.frame_header, image=self.logo).grid(row=0, column=0, rowspan=2)
        ttk.Label(self.frame_header, text = 'Anlegg Driftslogg', style = 'Header.TLabel').grid(row=0, column=1, padx=15, pady=15)
        ttk.Label(self.frame_header, wraplength = 250,
                  text = ('Velkommen til programmet for å registrere informasjonen fra Anlegget.\n\n'
                  'Vennligst skriv kommentarene nedenfor.')).grid(row=1, column=1, padx=20)
        
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text = 'Skift:').grid(row=0, column=0, pady=5, padx=5, sticky='sw')
        ttk.Label(self.frame_content, text = 'Maskin:').grid(row=0, column=1, pady=5, padx=5, sticky='sw')
        ttk.Label(self.frame_content, text = 'Kommentarer:').grid(row=2, column=0, pady=5, padx=5, sticky='sw')

        self.entry_shift = ttk.Entry(self.frame_content, width=29, font=('Arial', 10), justify='left')
        self.entry_machine = ttk.Entry(self.frame_content, width=29, font=('Arial', 10), justify='left')
        self.text_comments = tk.Text(self.frame_content, width=60, height=20, font=('Arial', 10))
        
        self.entry_shift.grid(row=1, column=0)
        self.entry_machine.grid(row=1, column=1)
        self.text_comments.grid(row=3, column=0, columnspan=2, padx=5)

        ttk.Button(self.frame_content, text = 'Submit', style='TButton',
                   command=self.submit).grid(row=4, column=0, padx=5, pady=15, sticky='e')
        ttk.Button(self.frame_content, text = 'Clear', style='TButton',
                   command=self.clear).grid(row=4, column=1, padx=5, pady=15, sticky='w')

    def submit(self):
        print(f'Skift: {self.entry_shift.get()}')
        print(f'Maskin: {self.entry_machine.get()}')
        print(f'Kommentarer: {self.text_comments.get(1.0, tk.END)}')
        self.clear()
        messagebox.showinfo(title = 'Driftslogg', message = 'Kommentarer sendt!')
    
    def clear(self):
        self.entry_name.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.text_comments.delete(1.0, tk.END)
         
def main():            
    
    root = tk.Tk()
    feedback = Feedback(root)
    root.mainloop()
    
if __name__ == "__main__": main()