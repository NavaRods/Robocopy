import tkinter as tk
from tkinter import messagebox, ttk
import os
from dataclasses import dataclass

@dataclass
class window_Backup:
    main_window: tk.Tk
    callback_return: callable

    def __post_init__(self):
        self.cleanWindow()
        self.createWindowBackup()


    def cleanWindow(self):
        for widget in self.main_window.winfo_children():
            widget.destroy()

    def createWindowBackup(self):
        tk.Button(self.main_window, 
                  text="<- Regresar", 
                  command=lambda: (self.cleanWindow(), self.return_to_main())
                  ).grid(row=0, column=0, padx=10, pady=10)
        
        tk.Label(self.main_window, 
                 text="Respaldo", 
                 font=("Arial", 20, "bold")
                 ).grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    
    def return_to_main(self):
        self.cleanWindow()
        self.callback_return()