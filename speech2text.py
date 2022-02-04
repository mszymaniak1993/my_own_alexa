from ast import AugAssign
import speech_recognition as sr
from text2speech import *

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Alexa: Listening...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language = "pl-PL")
            print(f"master: {query}")
            if query == "cześć":
                speak("Witaj")
            return query
        except:
            print("Try Again")

print(command())