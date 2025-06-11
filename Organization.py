import os 
import shutil

carpeta = 'C:\\Users\\foxys\\OneDrive\\Escritorio\\CP' # Carpeta principal
desktop = 'C:\\Users\\foxys\\OneDrive\\Escritorio\\Cosas2' # Carpeta organizada

# os.mkdir(desktop) # Crea la carpeta organizada

# pdfPath = 'C:\\Users\\foxys\\OneDrive\\Escritorio\\Cosas2\\PDF'
# wordPath = 'C:\\Users\\foxys\\OneDrive\\Escritorio\\Cosas2\\Words'

org = carpeta

def filtro():
    return [os.path.join(carpeta, carpetas) for carpetas in os.listdir(carpeta)]

def incarpeta():
    dicc = filtro()
    print(dicc)

    # Create destination folders if they don't exist
    try:
        os.makedirs(os.path.join(desktop, 'PDF'), exist_ok=True)
        os.makedirs(os.path.join(desktop, 'TXT'), exist_ok=True)
        os.makedirs(os.path.join(desktop, 'WORD'), exist_ok=True)
        os.makedirs(os.path.join(desktop, 'EXCEL'), exist_ok=True)
        os.makedirs(os.path.join(desktop, 'PPTX'), exist_ok=True)
    except Exception as e:
        print(f"Error creating directories: {e}")

    for subdir in dicc:
        # Get all files in the subdirectory
        for filename in os.listdir(subdir):
            filepath = os.path.join(subdir, filename)
            
            if filename.lower().endswith('.txt'):
                dest = os.path.join(desktop, 'TXT', filename)
            elif filename.lower().endswith(('.pptx', '.ppt')):
                dest = os.path.join(desktop, 'PPTX', filename)
            elif filename.lower().endswith(('.xlsx', '.xls')):
                dest = os.path.join(desktop, 'EXCEL', filename)
            elif filename.lower().endswith(('.docx', '.doc')):
                dest = os.path.join(desktop, 'WORD', filename)
            elif filename.lower().endswith('.pdf'):
                dest = os.path.join(desktop, 'PDF', filename)
            else:
                os.makedirs(os.path.join(desktop, 'Others'), exist_ok=True)
                dest = os.path.join(desktop, 'Others', filename)
            
            try:
                shutil.move(filepath, dest)
                print(f"Moved {filename} to {dest}")
            except Exception as e:
                print(f"Error moving {filename}: {e}")
    
        

incarpeta()
        


    
    



# for pdf in pdfs:
#     shutil.move(pdf, pdfPath)

# for word in words:
#     shutil.move(word, wordPath)
