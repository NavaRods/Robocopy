import os

carpeta = 'C:\\Users\\foxys\\OneDrive\\Escritorio\\CP'
desktop = 'C:\\Users\\foxys\\OneDrive\\Escritorio\\Cosas2'

def filtro():
    print("Carpeta principal:", carpeta)
    return [os.path.join(carpeta, carpetas) for carpetas in os.listdir(carpeta)]

def mover_con_robocopy(origen, destino, nombre_archivo):
    comando = f'robocopy "{origen}" "{destino}" "{nombre_archivo}" /MOV /NFL /NDL /NJH /NJS /NC /NS >nul'
    resultado = os.system(comando)
    if resultado <= 1:
        print(f"Moved: {nombre_archivo} → {destino}")
    else:
        print(f"Error moving {nombre_archivo} (code {resultado})")

def incarpeta():
    dicc = filtro()
    print("Subdirectorios detectados:", dicc)

    # Crear carpetas destino si no existen
    categorias = ['PDF', 'TXT', 'WORD', 'EXCEL', 'PPTX', 'Others']
    for categoria in categorias:
        os.makedirs(os.path.join(desktop, categoria), exist_ok=True)

    for subdir in dicc:
        for filename in os.listdir(subdir):
            filepath = os.path.join(subdir, filename)
            print("Subcarpetas:", filepath)
            lower_name = filename.lower()

            if lower_name.endswith('.txt'):
                destino = os.path.join(desktop, 'TXT')
            elif lower_name.endswith(('.pptx', '.ppt')):
                destino = os.path.join(desktop, 'PPTX')
            elif lower_name.endswith(('.xlsx', '.xls')):
                destino = os.path.join(desktop, 'EXCEL')
            elif lower_name.endswith(('.docx', '.doc')):
                destino = os.path.join(desktop, 'WORD')
            elif lower_name.endswith('.pdf'):
                destino = os.path.join(desktop, 'PDF')
            else:
                destino = os.path.join(desktop, 'Others')

            # mover_con_robocopy(subdir, destino, filename)

print(filtro())
# incarpeta()
