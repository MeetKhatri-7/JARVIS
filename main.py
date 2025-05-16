import pyttsx3
import speech_recognition as sr
from Greetme import greetme
import datetime
import webbrowser
from google import genai
from dictapp import dictapp,openappweb,closeappweb
import os
import pyautogui
from keyboard import volumeup,volumedown
import random
from calculate import wolframalpha, Calc
from schedule import scheduleday, showschedule
from news import news
import speedtest
from internet import speed
from plyer import notification
import requests
from bs4 import BeautifulSoup
from intro import play_gif
# import keyboard
# import wikipedia

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty('rate', 190)


def speak(audio):
    """Function to make the assistant speak"""
    engine.say(audio)
    engine.runAndWait()

speak("Enter Password to open Me: ")

for i in range(3):
    a=input("Enter Password to open Me: ")
    pw_file=open("render.txt","r")
    pw=pw_file.read()
    pw_file.close()
    if (a==pw):
        speak("Welcome sir. Please Speak Wake up to Load me up!")
        break
    
    elif(i==2 and a!=pw):
        exit()
        
    elif(a!=pw):
        speak("Try again!")
        
play_gif

api="AIzaSyCx9IOR6I_xtoyBkybS5-phOWl67ma0osQ"

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

def alarm(query):
    timehere=open("alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

if __name__ == "__main__":
    while True:
        query = takecommand().lower()
        if "wake up" in query:
            greetme()

            while True:
                query = takecommand().lower()
                if "go to sleep" in query or "good bye" in query:
                    speak("Ok sir, You can call me anytime")
                    break

                elif "hello" in query:
                    speak("Hello sir, how are you")
                    print("Hello sir, how are you")

                elif "i am fine" in query or "i m fine" in query:  # Fixed condition
                    speak("That's great sir")
                    print("That's great sir")

                elif "how are you" in query:  # Removed trailing space
                    speak("Perfect sir!")
                    print("Perfect sir!")

                elif "thank you" in query:
                    speak("You're welcome, Sir!")  # Fixed spelling
                    print("You're welcome, Sir!")
                    
                elif "remember that" in query:
                    rememberMessage = query.replace("remember", "")
                    rememberMessage = query.replace("jarvis", "")
                    speak("You told me to remember that " +rememberMessage)
                    with open("remember.txt","w") as r:
                        r.write(rememberMessage)
                        r.close()
                
                elif "what do you remember" in query:
                    remember = open("remember.txt","r")
                    speak("You told me to remember that "+remember.read())
                    remember.close()

                elif "gemini" in query:
                    query = query.replace("gemini", "")
                    query = query.replace("ask", "")
                    engine.setProperty("voice", voices[1].id)

                    client = genai.Client(api_key=api)

                    response = client.models.generate_content(
                        model="gemini-2.0-flash", contents=query
                    )
                    print(response.text)
                    speak(response.text)
                    
                elif "open" in query:
                    query = query.replace("open","")
                    query = query.replace("jarvis", "")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    # pyautogui.sleep(2)
                    pyautogui.press("enter")
                    
                elif "google" in query:
                    webbrowser.open("google.com")

                elif "youtube" in query:
                    webbrowser.open("youtube.com")

                elif "wikipedia" in query:
                    webbrowser.open("wikipedia.org")

                elif "the time" in query:
                    strTime= datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, The time is {strTime}")

                elif "see you" in query:
                    speak("Ok, See you again sir")
                    exit()

                elif "open" in query:
                    openappweb(query)

                elif "close" in query:
                    closeappweb(query)
                    
                elif "set an alarm" in query:
                    print("input time example - 10 and 10 and 10")
                    speak("Set the alarm")
                    a= input("Please tell the time - ")
                    alarm(a)
                    speak("Done, sir")
                    
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("Video Paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("Video played")
                    
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                
                elif "volume up" in query:
                    volumeup()
                
                elif "volume down" in query:
                    volumedown()
                    
                elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    b=random.randint(1, 3)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=Z8IRRphKFZA")
                    if b==2:
                        webbrowser.open("https://www.youtube.com/watch?v=KNxv88wUgnM")
                    if b==3:
                        webbrowser.open("https://www.youtube.com/watch?v=XTp5jaRU3Ws")
                        
                elif "news" in query:
                    news(query)
                    
                    
                elif "calculate" in query:
                    query=query.replace("calculate","")
                    query=query.replace("jarvis","")
                    Calc(query)
                    
                elif "shutdown" in query:
                    speak("Are You want to shutdown the System")
                    shutdown=input("do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")
                        
                    elif shutdown == "no":
                        break
                    
                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password \n")
                    with open("render.txt", "w") as newp:
                        newp.write(new_pw)
                    speak("Done sir")
                    speak(f"Your new password is {new_pw}")
                    
                elif "schedule my day" in query:
                    scheduleday(query)
                            
                elif "show my schedule" in query:
                    showschedule()
                    
                elif "internet speed" in query:
                    speed()
                    
                elif "ipl score" in query:
                    url = "https://www.cricbuzz.com/"
                    page=requests.get(url)
                    soup = BeautifulSoup(page.text,"html.parser")
                    team1=soup.find_all(class_ = "cb-ovr-flo cb-hmcg-tm-nm")[0].get_text()
                    team2=soup.find_all(class_ = "cb-ovr-flo cb-hmcg-tm-nm")[1].get_text()
                    team1_score=soup.find_all(class_="cb-ovr-flo")[8].get_text()
                    team2_score=soup.find_all(class_="cb-ovr-flo")[10].get_text()
                    
                    a=print(f"{team1} : {team1_score}")
                    b=print(f"{team2} : {team2_score}")
                    
                    notification.notify(
                        title="IPL SCORE",
                        message = f"{a}\n{b}",
                        timeout=5
                    )
                    
                elif "screenshot" in query:
                    im=pyautogui.screenshot()
                    im.save("ss.jpg")
                    
                elif "click my photo" in query:
                    query = query.replace("open","")
                    query = query.replace("jarvis", "")
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    # pyautogui.sleep(2)
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")
                    
                else :
                    query = query.replace("jarvis", "")
                    query = query.replace("ask", "")
                    client = genai.Client(api_key=api)

                    response = client.models.generate_content(
                        model="gemini-2.0-flash", contents=query
                    )
                    print(response.text)
                    speak(response.text)

                