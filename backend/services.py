import webbrowser
import pyautogui
from datetime import datetime


# ---------------- BROWSER ----------------

def open_browser():
    webbrowser.open("https://www.google.com")


def close_browser():
    pyautogui.hotkey("alt", "f4")


def open_youtube():
    webbrowser.open("https://www.youtube.com")


# ---------------- SCREENSHOT ----------------

def take_screenshot():
    filename = f"../screenshots/{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    pyautogui.screenshot(filename)
    print("Saved:", filename)


# ---------------- VOLUME ----------------

def volume_up():
    pyautogui.press("volumeup")


def volume_down():
    pyautogui.press("volumedown")


def volume_mute():
    pyautogui.press("volumemute")


# ---------------- MEDIA ----------------

def play_pause_music():
    pyautogui.press("playpause")