@echo off
setlocal enabledelayedexpansion

echo --------------------------------------------
echo Instalador Automático de Paquetería Básica
echo --------------------------------------------

:: Obtener letra de la unidad actual
set "usb_drive=%~d0"
echo Ejecutando desde: %usb_drive%

:: Definir rutas relativas de los instaladores
set ruta_instalador1=AcroRdrDC2300320269_es_ESwin11.exe

:: Lista de variables definidas
set lista=ruta_instalador1

:: Ejecutar cada instalador
for %%I in (%lista%) do (
    call set "archivo=%%%I%%"
    set ruta_completa=%usb_drive%\!archivo!"

    echo DEBUG: Nombre lógico = %%I
    echo DEBUG: Archivo       = !archivo!
    echo DEBUG: Ruta completa = !ruta_completa!

    if exist "!ruta_completa!" (
        echo Ejecutando !ruta_completa!
        if /I "!ruta_completa:~-4!"==".exe" (
            powershell -Command "Start-Process '!ruta_completa!' -Verb runAs"
        ) else (
            call "!ruta_completa!"
        )
        timeout /t 5 > nul
    ) else (
        echo Instalador no encontrado: !ruta_completa!
    )
)

echo --------------------------------------------
echo Instalación finalizada. Presiona una tecla...
pause > nul
exit
