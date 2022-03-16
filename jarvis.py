from unittest import result
import pyttsx3  # importing module which provides engine used for speaking function to convert text to speech
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia


engine = pyttsx3.init()  # engine definition
# define voices, taking properties from engine
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):  # function for converting text to speech
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def takecommand():  # To convert voice into text and take input from user
    r = sr.Recognizer()  # defining recognizer as r
    with sr.Microphone() as source:  # takes command from user
        print("listening....")
        r.pause_threshhold = 1  # to extend the listening period
        audio = r.listen(source, timeout=1, phrase_time_limit=5)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")  # formatted string

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query


def wish():
    hour = int(datetime.datetime.now().hour)  # gives the exact time

    if hour >= 0 and hour <= 12:
        speak("Good Morning")
    elif hour > 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis, please tell me how can I help you?")


if __name__ == "__main__":
    takecommand()
    wish()
    #speak("this is advanced jarvis")
    while True:
        if 1:
            # defining query for whenever user gives input (It is stored in the query)
            query = takecommand().lower()

        # logic building for tasks STARTS
        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            # To capture--internal camera=0 , external cam=1(watv port)
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "D:\\Music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            for song in songs:
                if songs.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, songs[0]))

        elif "IP address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            print(results)
            print("Arsh is dumb")
