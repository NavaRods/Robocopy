import subprocess
import os

def Backup(Origin, Destination):
    Origin = os.path.normpath(Origin)
    Destination = os.path.normpath(Destination)

    command = ['robocopy', Origin, Destination, '/E', '/R:3', '/W:0']

    print("Ejecutando comando:", " ".join(command))
    
    result = subprocess.run(command, capture_output=True, text=True)
    print("SALIDA:")
    print(result.stdout)
    print("ERRORES:")
    print(result.stderr)
