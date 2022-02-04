import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")

engine.setProperty("rate", 120)
engine.setProperty("voice", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()