import pyttsx3
import threading

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def speak_async(text):
    threading.Thread(target=speak, args=(text,), daemon=True).start()