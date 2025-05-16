import pyttsx3
import datetime
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty('rate', 190)


def speak(audio):
    """Function to make the assistant speak"""
    engine.say(audio)
    engine.runAndWait()
    
extractedtime=open("alarmtext.txt", 'rt')
time=extractedtime.read()
Time=str(time)
extractedtime.close()

deletetime=open("alarmtext.txt","r+")
deletetime. truncate(0)
deletetime.close()

def ring(time):
    timeset=str(time)
    timenow=timeset.replace("jarvis","")
    timenow=timeset.replace("set alarm","")
    timenow=timeset.replace(",","")
    timenow=timeset.replace(" ","")
    timenow=timeset.replace("and",":")
    Alarmtime=str(timenow)
    print(Alarmtime)
    while True:
        currenttime=datetime.datetime.now().strtime("%H:%M:%S")
        if currenttime == Alarmtime:
            speak("Alarm ringing, sir")
            os.startfile("alarm.mp3")
        elif currenttime + "00:00:00" == Alarmtime:
            exit()
            
ring(time)