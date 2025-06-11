import tkinter as tk
from tkinter import messagebox, ttk
from dataclasses import dataclass

from Interfaces.Backup import window_Backup
from Interfaces.Restoration import window_Restoration

@dataclass
class main:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("CTA - Soporte Tecnico")
        self.main_window.geometry("600x400")
        self.main_window.resizable(False, False)

        self.create_main_window()

        self.main_window.mainloop()

    def create_main_window(self):
        tk.Label(self.main_window, text="CTA", font=("Arial", 20)
                 ).grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        tk.Button(self.main_window, 
                  text="PC -> Soporte", 
                  command=lambda: window_Backup(self.main_window, self.create_main_window)
                  ).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(self.main_window, 
                  text="Soporte -> PC", 
                  command=lambda: window_Restoration(self.main_window, self.create_main_window)
                  ).grid(row=1, column=1, padx=10, pady=10)

if __name__ == "__main__":
    main()