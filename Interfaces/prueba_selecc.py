import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sys # Para os.path y sys.platform para mensajes
import os

# --- Función para Abrir el Explorador de Archivos y Seleccionar Unidad/Carpeta ---

def seleccionar_unidad_con_explorador():
    """
    Abre un cuadro de diálogo del explorador de archivos para que el usuario
    seleccione una carpeta, que podría ser la raíz de una unidad.
    """
    root = tk.Tk()
    root.withdraw() # Oculta la ventana principal de Tkinter
    root.title("Seleccionar Unidad de Almacenamiento")
    root.resizable(False, False)

    # Abrir el diálogo de selección de directorio
    # initialdir puede establecer un directorio de inicio, como la raíz en Unix o "C:\" en Windows
    # Pero el usuario puede navegar a cualquier lugar.
    if sys.platform == "win32":
        initial_dir = "C:\\"
    elif sys.platform == "darwin": # macOS
        initial_dir = "/Volumes" # Punto de montaje común para unidades externas
    else: # Linux
        initial_dir = "/" # Directorio raíz

    selected_path = filedialog.askdirectory(
        parent=root,
        initialdir=initial_dir,
        title="Selecciona la unidad o una carpeta en la unidad"
    )

    root.destroy() # Cierra la ventana oculta de Tkinter

    return selected_path

# --- Lógica principal ---

def iniciar_seleccion():
    print("Abriendo explorador de archivos para seleccionar una unidad...")
    
    path_seleccionado = seleccionar_unidad_con_explorador()

    if path_seleccionado:
        messagebox.showinfo(
            "Unidad Seleccionada",
            f"Has seleccionado la ruta:\n{path_seleccionado}\n"
            f"Esta ruta corresponde a la unidad: {path_seleccionado.split(os.sep)[0] + os.sep if sys.platform == 'win32' else os.path.splitdrive(path_seleccionado)[0] + os.sep}"
        )
        print(f"Ruta seleccionada: {path_seleccionado}")
        
        # Aquí puedes agregar la lógica para detectar la unidad "soporte"
        # Basándote en si 'path_seleccionado' contiene "soporte"
        # O si el nombre de la unidad padre de 'path_seleccionado' es "soporte"
        
        # Ejemplo muy básico de detección de "soporte" en la ruta seleccionada:
        if "soporte" in path_seleccionado.lower():
            messagebox.showinfo("Unidad 'SOPORTE' Detectada", "¡La ruta seleccionada contiene 'soporte'!")
            # Aquí podrías llamar a una función que muestre todos los discos,
            # pero dado que ya no listamos los discos, necesitarías readaptar esa lógica
            # o asumir que el usuario ya ha interactuado con el explorador.
            # print("Aquí podrías mostrar los detalles de todos los discos si tuvieras la lógica para detectarlos de nuevo.")
        
    else:
        messagebox.showwarning("Selección Cancelada", "No se seleccionó ninguna unidad o carpeta.")
        print("Selección cancelada.")

if __name__ == "__main__":
    # Necesitas que tkinter esté inicializado para usar filedialog
    # Puedes crear una pequeña ventana dummy si no quieres una interfaz completa
    
    # Este es el punto de entrada para iniciar el proceso
    iniciar_seleccion()