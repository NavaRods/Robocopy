import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import os
import sys
import psutil
from dataclasses import dataclass

try:
    import wmi
    print("Módulo 'wmi' importado correctamente.")
except ImportError:
    wmi = None
    print("ADVERTENCIA: El módulo 'wmi' no está instalado. Los nombres de volumen en Windows pueden no aparecer.")

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
        
        tk.Button(self.main_window,
                  text="Seleccionar unidad",
                  command=self.iniciar_seleccion
                  ).grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        
    def obtener_nombre_volumen_windows(self, device_path):
        """Intenta obtener el nombre de volumen de una unidad en Windows usando WMI."""
        if sys.platform == "win32" and wmi:
            try:
                c = wmi.WMI()
                device_caption = device_path.replace('\\', '')
                for disk in c.Win32_LogicalDisk():
                    if disk.Caption == device_caption:
                        return disk.VolumeName if disk.VolumeName else None
            except Exception as e:
                print(f"ERROR al obtener nombre de volumen WMI para {device_path}: {e}")
        return None

    def obtener_info_unidad_por_ruta(self, path):
        """
        Dada una ruta, encuentra la información de la unidad a la que pertenece,
        incluyendo su nombre de volumen si es posible.
        """
        # Asegurarse de que la ruta esté normalizada para comparación
        path = os.path.normcase(os.path.normpath(path))

        for partition in psutil.disk_partitions(all=False):
            # Normalizar el mountpoint de la partición para una comparación consistente
            mountpoint_norm = os.path.normcase(os.path.normpath(partition.mountpoint))

            # Verificar si la ruta seleccionada comienza con (o es igual a) el punto de montaje
            if path.startswith(mountpoint_norm):
                # Para Windows, asegurar que sea la raíz o un subdirectorio directo del mountpoint
                # Por ejemplo, si path es 'D:/' y mountpoint es 'D:\', ambas deberían ser reconocidas
                # Si path es 'D:/MiCarpeta' y mountpoint es 'D:\', también se debe reconocer
                if sys.platform == "win32":
                    # Si path es "D:/", el mountpoint es "D:\", ambos normalizados deberían coincidir o ser subrutas
                    if path == mountpoint_norm or path.startswith(mountpoint_norm + os.sep):
                        nombre_volumen = self.obtener_nombre_volumen_windows(partition.device)
                        return {
                            "mountpoint": partition.mountpoint,
                            "volume_name": nombre_volumen,
                            "fstype": partition.fstype,
                            "device": partition.device
                        }
                else: # Linux/macOS
                    if path == mountpoint_norm or path.startswith(mountpoint_norm + os.sep):
                        nombre_volumen = None
                        if sys.platform == "darwin" and partition.mountpoint.startswith("/Volumes/"):
                            nombre_volumen = os.path.basename(partition.mountpoint)
                        
                        return {
                            "mountpoint": partition.mountpoint,
                            "volume_name": nombre_volumen,
                            "fstype": partition.fstype,
                            "device": partition.device
                        }
        return None

    def seleccionar_ruta_con_explorador(self):
        """
        Abre un cuadro de diálogo del explorador de archivos para que el usuario
        seleccione una carpeta.
        """
        temp_root = tk.Tk()
        temp_root.withdraw()

        if sys.platform == "win32":
            initial_dir = "C:\\"
        elif sys.platform == "darwin":
            initial_dir = "/Volumes"
        else:
            initial_dir = "/"

        selected_path = filedialog.askdirectory(
            parent=temp_root,
            initialdir=initial_dir,
            title="Selecciona una carpeta en la unidad de destino"
        )
        temp_root.destroy()
        return selected_path

    def iniciar_seleccion(self):
        print("Abriendo explorador de archivos para seleccionar una carpeta...")
        
        self.path_seleccionado = self.seleccionar_ruta_con_explorador()

        if self.path_seleccionado:
            print(f"DEBUG: Ruta seleccionada por filedialog: '{self.path_seleccionado}'")
            info_unidad = self.obtener_info_unidad_por_ruta(self.path_seleccionado)

            if info_unidad:
                mountpoint = info_unidad["mountpoint"]
                volume_name = info_unidad["volume_name"]
                
                display_info = ""
                if sys.platform == "win32":
                    # Usar os.path.splitdrive para obtener la letra del disco de forma más robusta
                    drive_letter_part = os.path.splitdrive(mountpoint)[0]
                    if volume_name:
                        display_info = f"**{drive_letter_part}\\ ({volume_name})**"
                    else:
                        display_info = f"**{drive_letter_part}\\ [Sin Nombre]**"
                else:
                    if volume_name:
                        display_info = f"**{mountpoint} ({volume_name})**"
                    else:
                        display_info = f"**{mountpoint}**"
                
                messagebox.showinfo(
                    "Unidad de Almacenamiento Seleccionada",
                    f"Has seleccionado la ruta:\n'{self.path_seleccionado}'\n\n"
                    f"La **Unidad de Almacenamiento** es:\n{display_info}"
                )
                print(f"Ruta seleccionada: {self.path_seleccionado}")
                print(f"Unidad de Almacenamiento: {display_info}")

                if (volume_name and "soporte" in volume_name.lower()) or \
                   ("soporte" in mountpoint.lower()):
                    messagebox.showinfo("Unidad 'SOPORTE'", "¡Has seleccionado una unidad relacionada con 'SOPORTE'!")

            else:
                # Modificado para imprimir la salida específica solicitada
                print(f"No se pudo determinar la unidad para la ruta: {self.path_seleccionado}")
                messagebox.showwarning("Información de Unidad", 
                                       f"No se pudo determinar la unidad de almacenamiento para la ruta seleccionada:\n'{self.path_seleccionado}'")
        else:
            messagebox.showwarning("Selección Cancelada", "No se seleccionó ninguna carpeta.")
            print("Selección cancelada.")

    def return_to_main(self):
        self.cleanWindow()
        self.callback_return()