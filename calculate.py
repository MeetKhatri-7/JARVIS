import wolframalpha
import pyttsx3
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty('rate', 190)


def speak(audio):
    """Function to make the assistant speak"""
    engine.say(audio)
    engine.runAndWait()
    
    
def wolframalpha(query):
    apikey="UE9THU-AX7V9VQ3EV"
    requester = wolframalpha.Client(apikey)
    requested=requester.query(query)
    
    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")
        
def Calc(query):
    Term=str(query)
    Terms= Term.replace("jarvis","")
    Terms= Term.replace("into","*")
    Terms= Term.replace("divide by","/")
    Terms= Term.replace("plus","+")
    Terms= Term.replace("minus","-")
    
    Final=str(Term)
    try:
        result = wolframalpha(Final)
        print(f"{result}")
        speak(f"{result}")
        
    except:
        speak("The value is not answerable")
        