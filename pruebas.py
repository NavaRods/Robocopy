import os
import subprocess
import tkinter as tk
from tkinter import filedialog, scrolledtext

def Backup():
    # Seleccionar origen
    origin = filedialog.askdirectory(title="Selecciona carpeta origen")
    if not origin:
        return
    # Seleccionar destino
    destination = filedialog.askdirectory(title="Selecciona carpeta destino")
    if not destination:
        return

    # Normalizar rutas para Windows
    origin = os.path.normpath(origin)
    destination = os.path.normpath(destination)

    # Mostrar rutas seleccionadas
    output_text.insert(tk.END, f"Origen: {origin}\n")
    output_text.insert(tk.END, f"Destino: {destination}\n")

    # Comando robocopy
    command = ['robocopy', origin, destination, '/E', '/R:3', '/W:0']
    output_text.insert(tk.END, f"Ejecutando: {' '.join(command)}\n\n")

    # Ejecutar y capturar salida
    result = subprocess.run(command, capture_output=True, text=True)

    # Mostrar resultado
    output_text.insert(tk.END, result.stdout)
    output_text.insert(tk.END, "\nERRORES:\n")
    output_text.insert(tk.END, result.stderr)
    output_text.insert(tk.END, "\n------ Operación completada ------\n\n")
    output_text.see(tk.END)

# Crear ventana principal
root = tk.Tk()
root.title("Backup con Robocopy")
root.geometry("800x500")

# Botón de respaldo
backup_button = tk.Button(root, text="Iniciar Backup con Robocopy", command=Backup)
backup_button.pack(pady=10)

# Área de texto estilo terminal
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Courier", 10), bg="black", fg="lime")
output_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()