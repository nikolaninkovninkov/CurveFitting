import pyautogui
import time

def open_new_terminal():
    pyautogui.hotkey('ctrl', 'shift', '`')
    time.sleep(1)
def run(function):
    pyautogui.write(function)
    pyautogui.press("enter")
def run_client():
    run("cd client")
    run("npm run start")
def run_server():
    run("cd server")
    run("pipenv shell")
    time.sleep(5)
    run("python manage.py runserver")
def kill_terminal():
    pyautogui.hotkey('ctrl', 'p')
    pyautogui.write(">Terminal: Switch Active Terminal")
    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.hotkey('ctrl', 'p')
    pyautogui.write(">Terminal: Kill the Active Terminal Instance")
    pyautogui.press("enter")
open_new_terminal()
run_client()
open_new_terminal()
run_server()
kill_terminal()