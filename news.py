import requests
import json
import pyttsx3
from google import genai

api="AIzaSyCx9IOR6I_xtoyBkybS5-phOWl67ma0osQ"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty('rate', 190)


def speak(audio):
    """Function to make the assistant speak"""
    engine.say(audio)
    engine.runAndWait()
    
    
def news(query):
    client = genai.Client(api_key=api)
    query = query.replace("give me some news about","")
    query = query.replace("givemesomenewsabout","")
    query = query.replace("news", "")
    query = query.replace(" ","")
    query = query.replace("jarvis","")
    
    response = client.models.generate_content(model="gemini-2.0-flash", contents=f"Give me some news about {query} in 2 to 3 lines")
    print(response.text)
    speak(response.text)
