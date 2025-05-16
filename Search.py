import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import wikipedia as googleScrap
from google import genai
import webbrowser

api ="AIzaSyCx9IOR6I_xtoyBkybS5-phOWl67ma0osQ"
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        print(e)
        return 'none'

    return query

query = takecommand().lower()

engine = pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty('rate',190)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query:
        speak("This is what I found on google")
        query = query.replace("google", "")
        query = query.replace("jarvis", "")
        try:
            pywhatkit.search(query)
            result=googleScrap.summary(query,1)
            speak(result)

        except :
            speak("No speakable out available")

def searchYoutube(query):
    if "youtube" in query:
        speak("This is what I found for your search!")
        query = query.replace("youtube search", "")
        query = query.replace("youtube", "")
        query = query.replace("jarvis", "")
        web = f"https://www.youtube.com/results?search_query={query}"
        webbrowser.open(web)
        pywhatkit.playony(query)
        speak("Done, sir!")

def searchWikipedia(query):
    if"wikipedia" in query:
        speak("Searching...")
        query = query.replace("wikipedia", "")
        query = query.replace("search", "")
        query = query.replace("jarvis", "")
        results=wikipedia.summary(query, sentences=3)
        print(results)
        speak(results)