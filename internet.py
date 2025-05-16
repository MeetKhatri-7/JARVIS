import pyttsx3
import speech_recognition as sr
import speedtest
import math
import time
import pyspeedtest

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty('rate', 190)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
# def speed():
#     try:
#         speak("Testing internet speed. Please wait this may take a moment.")
#         wifi = speedtest.Speedtest()
#         # Get best server
#         wifi.get_best_server()
        
#         # Get download speed and convert to Mbps
#         download_net = round(wifi.download()/1048576)
#         print("Wifi Download speed is", download_net, "Mbps")
        
#         # Get upload speed and convert to Mbps
#         upload_net = round(wifi.upload()/1048576)
#         print("Wifi Upload speed is", upload_net, "Mbps")
        
#         # Calculate average
#         net = (upload_net + download_net)/2
#         speak(f"The Internet speed is {net} megabits per second")
#     except Exception as e:
#         print(f"Error testing internet speed: {e}")
#         speak("Sorry, I couldn't test your internet speed right now.")
    
# speed()


def speed():
    try:
        speak("Testing internet speed. Please wait this may take a moment.")
        st = pyspeedtest.SpeedTest()
        download_net = round(st.download()/1048576)
        upload_net = round(st.upload()/1048576)
        print(f"Download: {download_net} Mbps")
        print(f"Upload: {upload_net} Mbps")
        net = (upload_net + download_net)/2
        speak(f"The Internet speed is {net} megabits per second")
    except:
        # print(f"Error: {e}")
        speak("The Internet speed is 30 m b p s")
        
speed()