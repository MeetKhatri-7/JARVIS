import pyttsx3
import speech_recognition as sr
from plyer import notification
from pygame import mixer
import plyer


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty('rate', 190)


def speak(audio):
    """Function to make the assistant speak"""
    engine.say(audio)
    engine.runAndWait()
    
def takecommand():
    """Function to take microphone input from the user and return string output"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
        return query.lower()


    except Exception as e:
        print("Say that again please...")
        print(e)
        return 'none'
    
def scheduleday(query):
    tasks =[]
    speak("Do you want to clear old tasks (Please 'Yes' or 'No')")
    query=takecommand().lower()
    if 'yes' in query:
        file = open ("tasks.txt", "w")
        file.write(f"")
        file.close()
        no_tasks = int(input("Enter the number of tasks : "))
        i=0
        for i in range(no_tasks):
            tasks.append(input("Enter the task: "))
            file = open("tasks.txt","a")
            file.write(f"{i}. {tasks[i]}")
            file.close()
                    
    elif 'no' in query:
        no_tasks = int(input("Enter the number of tasks : "))
        i=0
        for i in range(no_tasks):
                tasks.append(input("Enter the task: "))
                file = open("tasks.txt","a")
                file.write(f"{i}. {tasks[i]} \n")
                file.close()

def showschedule():
    file = open("tasks.txt","r")
    content= file.read()
    file.close()
    mixer.init()
    mixer.music.load("notification.mp3")
    mixer.music.play()
    notification.notify(
        title="Your Schedule",
        message=content,
        app_name='Python Notification',
        timeout=15  
    )
    