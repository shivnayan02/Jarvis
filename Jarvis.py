import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak (audio):
    engine.say(audio)
    engine.runAndWait()


def wishME():
    hour  = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good morning Sir")

    elif hour>=12 and hour<18:
        speak("Good afternoon Sir!")

    else:
        speak("Good evening Sir!")  

    speak("I am Jarvis  Please tell me  how may i help u?")  



def takeCommand():
    r = sr.Recognizer()
    my_mic = sr.Microphone(device_index=1) #my device index is 1, you have to put your device index
    with my_mic as source:
        print("Listening..................",)
        r.adjust_for_ambient_noise(source) #reduce noise
        audio = r.listen(source) #take voice input from the microphone
        
        

    print("you said:  " +r.recognize (audio))
    
    


if __name__ == "__main__":
    wishME()
    takeCommand()
    # while True:
    #     query = takeCommand()

    #     # if 'wikipedia' in query:
    #     #     speak('searching wikipedia......')
    #     #     query = query.replace("wikipedia","")
    #     #     results = wikipedia.summary(query, sentences=3)
    #     #     speak("According to wikipedia")
    #     #     print("results")
    #     #     speak("results")

    #     if 'open youtube' in query:
    #         webbrowser.open("youtube.com")

    
