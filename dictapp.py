import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep
import subprocess

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty('rate', 190)


def speak(audio):
    """Function to make the assistant speak"""
    engine.say(audio)
    engine.runAndWait()

dictapp ={
    "commandprompt":"cmd",
    "word":"winword",
    "paint":"paint",
    "excel":"excel",
    "chrome":"chrome",
    "vscode":"code",
    "powershell":"powershell"
}

def openappweb(query):
    # speak("Launching, sir")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("jarvis", "")
        query = query.replace("launch", "")
        query = query.replace(" ", "")
        webbrowser.open(f"https://www.{query}")
        speak("Website opened")

    else:
        keys=list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start{dictapp[app]}")
        speak("Application opened")


def closeappweb(query):
    speak("closing application")
    if "one tab" in query or "1 tab" in query:
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("tab closed")

    else:
        keys=list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
