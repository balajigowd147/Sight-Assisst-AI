import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.stop()  # stop any previous speech
    engine.say(text)
    engine.runAndWait()