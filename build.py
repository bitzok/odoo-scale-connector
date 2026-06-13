import PyInstaller.__main__
import os

APP_NAME = "OdooBalanzaService"

PyInstaller.__main__.run([
    'app/main.py',
    f'--name={APP_NAME}',
    '--onefile',
    '--noconsole',
    '--clean',
    # '--icon=app/icon.ico'
])

print(f"Construcción finalizada. Revisa la carpeta 'dist/' para ver tu {APP_NAME}.exe")