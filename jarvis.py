import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import tflearn
import tensorflow
import random

import json
with open('intents.json') as file:
    data = json.load(file)

words = []
labels = []
docs_x = []
docs_y = []


#20

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)

def wishme():
    h = int(datetime.datetime.now().hour)
    if h >= 0 and h < 12:
        speak("Good Morning Boss!")
    elif h >= 12 and h < 18 :
        speak("Good AfterNoon Boss!")
    else :
        speak("Good Evening Boss!")
    speak("What can I do for you?")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def hear():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    
    except Exception as e:
        #print(e)
        print("Say that again please..")
        speak("Say that again please")
        return "None"
    return query
        
        

if __name__ == '__main__':
    wishme()
    #speak("Hello Vijay")
    while True:
        query = hear().lower()
        
        if "take care" in query or 'good night' in query or "bye" in query :
            print("Lab's all wrapped up boss, night night!")
            speak("Lab's all wrapped up boss, night night!")
            exit()
        
        elif 'wikipedia' in query:
            speak("Searching Wikipedia..")
            query = query.replace("Wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak("Well I found that,")
            print(results)
            speak(results)
        
        elif 'open google' in query:
            speak("Okay!")
            webbrowser.open("google.com")
        
        elif 'open youtube' in query:
            speak("Okay!")
            webbrowser.open("youtube.com")
        
        elif 'the time' in query:
             strTime = datetime.datetime.now().strftime("%H:%M")
             speak(f"It is {strTime}")
        
        