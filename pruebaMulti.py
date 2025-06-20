import os
import subprocess
import tkinter as tk
from tkinter import filedialog, scrolledtext, simpledialog

def Backup():
    paired_backups = []

    output_text.insert(tk.END, "--- Modo de emparejamiento de origen y destino ---\n")
    output_text.insert(tk.END, "Seleccionará un origen y luego su destino correspondiente.\n")
    output_text.insert(tk.END, "Presione 'Cancelar' en cualquier diálogo para detener la selección.\n\n")

    while True:
        # Select Origin
        origin = filedialog.askdirectory(title="Selecciona una carpeta origen para el par (o Cancelar para finalizar)")
        if not origin:
            break # User cancelled, stop selecting pairs

        # Select Destination for this specific origin
        destination = filedialog.askdirectory(title=f"Selecciona la carpeta destino para '{os.path.basename(origin)}' (o Cancelar para finalizar)")
        if not destination:
            # If user cancels destination, assume they don't want to pair this origin
            output_text.insert(tk.END, f"Destino no seleccionado para '{origin}'. Este par será omitido.\n\n")
            continue # Continue to allow selecting another origin

        origin = os.path.normpath(origin)
        destination = os.path.normpath(destination)
        paired_backups.append((origin, destination))
        output_text.insert(tk.END, f"Par agregado: Origen: '{origin}' -> Destino: '{destination}'\n\n")

    if not paired_backups:
        output_text.insert(tk.END, "No se seleccionaron pares de origen y destino.\n")
        return

    output_text.insert(tk.END, "\n--- Iniciando Backups Emparejados ---\n")
    for origin, destination in paired_backups:
        perform_robocopy(origin, destination)
    
    output_text.insert(tk.END, "\n------ Todas las operaciones de respaldo emparejadas completadas ------\n\n")
    output_text.see(tk.END)

def perform_robocopy(origin, destination):
    """Executes the robocopy command for a given origin and destination."""
    output_text.insert(tk.END, f"\n--- Procesando: '{origin}' a '{destination}' ---\n")
    output_text.insert(tk.END, f"Origen: {origin}\n")
    output_text.insert(tk.END, f"Destino: {destination}\n")

    # Comando robocopy
    command = ['robocopy', origin, destination, '/E', '/R:3', '/W:0', '/ETA'] # Added /ETA for estimated time of arrival
    output_text.insert(tk.END, f"Ejecutando: {' '.join(command)}\n\n")

    # Ejecutar y capturar salida
    try:
        # Use a higher encoding number or 'latin-1' if 'cp850' still shows issues with special characters
        result = subprocess.run(command, capture_output=True, text=True, check=True, encoding='latin-1') 
        output_text.insert(tk.END, result.stdout)
        output_text.insert(tk.END, "\n")
    except subprocess.CalledProcessError as e:
        output_text.insert(tk.END, f"ERROR AL EJECUTAR ROBOCOPY PARA {origin} A {destination}:\n")
        output_text.insert(tk.END, f"Código de salida: {e.returncode}\n")
        output_text.insert(tk.END, "SALIDA ESTÁNDAR:\n")
        output_text.insert(tk.END, e.stdout)
        output_text.insert(tk.END, "ERRORES ESTÁNDAR:\n")
        output_text.insert(tk.END, e.stderr)
    except FileNotFoundError:
        output_text.insert(tk.END, "Error: Robocopy no encontrado. Asegúrate de que está en tu PATH.\n")
    except Exception as e:
        output_text.insert(tk.END, f"Ocurrió un error inesperado: {e}\n")
    
    output_text.insert(tk.END, "\n--- Respaldo completado para este par ---\n\n")


# Crear ventana principal
root = tk.Tk()
root.title("Backup Emparejado con Robocopy")
root.geometry("800x600") 

# Botón de respaldo
backup_button = tk.Button(root, text="Iniciar Backup Emparejado con Robocopy", command=Backup)
backup_button.pack(pady=10)

# Área de texto estilo terminal
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Consolas", 10), bg="black", fg="lime") 
output_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()