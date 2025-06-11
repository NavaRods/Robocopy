import tkinter as tk
from tkinter import *
import os

idReport = 666

def robocopy():
    root = tk.Tk()
    root.title("Robocopy")
    root.geometry("300x300")

    Button(root, text="PC -> Soporte", command=lambda: window_Backup()).grid(row=0, column=0)
    Button(root, text="Soporte -> PC").grid(row=0, column=1)



    pathUser = tk.Entry(PC)
    selectDisk = tk.Entry(Soporte)

    root.mainloop()
    

robocopy()

def window_Backup():
    backup = tk.Tk()
    backup.title("PC -> Soporte")
    backup.geometry("300x300")

    backup.mainloop()

def window_Restoration():
    rest = tk.Tk()
    rest.title("PC ->")

def Backup(pathUser, selectDisk):
    os.system('robocopy \"c:\Users' + f'\\{pathUser}' + '\\Desktop\"' + f'{selectDisk}'+':\\Respaldo-'+ f'\\{idReport}' + f'\\{pathUser}' + '\\Desktop\"' + '/E /R:3 /W:0')
    os.system('robocopy \"c:\Users' + f'\\{pathUser}' + '\\Documents\"' + f'{selectDisk}'+':\\Respaldo-'+ f'\\{idReport}' + f'\\{pathUser}' + '\\Documents\"' + '/E /R:3 /W:0')
    os.system('robocopy \"c:\Users' + f'\\{pathUser}' + '\\Download\"' + f'{selectDisk}'+':\\Respaldo-'+ f'\\{idReport}' + f'\\{pathUser}' + '\\Download\"' + '/E /R:3 /W:0')

def Restoration(pathUser, selectDisk):
    os.system('robocopy' + f'{selectDisk}'+':\\Respaldo-'+ f'\\{idReport}' + f'\\{pathUser}' + '\\Download\"' + '\"c:\Users' + f'\\{pathUser}' + '\\Download\"' + '/E /R:3 /W:0')
    os.system('robocopy' + f'{selectDisk}'+':\\Respaldo-' + f'\\{idReport}' + f'\\{pathUser}' + '\\Download\"' + '\"c:\Users' + f'\\{pathUser}' + '\\Download\"' + '/E /R:3 /W:0')
    os.system('robocopy' + f'{selectDisk}'+':\\Respaldo-'+ f'\\{idReport}' + f'\\{pathUser}' + '\\Download\"' + '\"c:\Users' + f'\\{pathUser}' + '\\Download\"' + '/E /R:3 /W:0')
    

