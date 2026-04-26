import speech_recognition as sr

# def listen(timeout=5,phrase_time_limit=8):
#     recognizer = sr.Recognizer()

#     with sr.Microphone() as source:
#         print("Listening...")
#         recognizer.adjust_for_ambient_noise(source=source,duration=0.3)

#         try:
#             audio = recognizer.listen(
#                 source=source,
#                 timeout=timeout,
#                 phrase_time_limit=phrase_time_limit
#             )

#             print("Audio listened successfully!!")
#             text = recognizer.recognize_google(audio_data=audio)
#             print("Text:" , text)

#             return text.lower()

#         except sr.WaitTimeoutError:
#             print("No speech detected!!")
#             return ""

#         except sr.UnknownValueError:
#             print("Audio is not audible!!")
#             return ""
#         except sr.RequestError:
#             print("API error")
#             return ""
        

# if __name__ == "__main__":
#     while True:
#         user_text = listen()

#         if user_text:
#             print(" Final Output:", user_text)

def listen_wake_up():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening..")
        print("Waiting for the Hey Assistant to wake up the assistant!!")
        audio = recognizer.listen(source=source)

        try:
            text = recognizer.recognize_google(audio).lower()

            print("Heard:",text)

            if "assistant" or "hey assistant" in text:
                return True
            return False

        except:
            return False
        
def listen_command():
    recognizer = sr.Recognizer()
    

    with sr.Microphone() as source:
        print("Listening..")
        audio = recognizer.listen(source=source)

        try:
            text = recognizer.recognize_google(audio)
            print(text)
            return text
        except:
            return ""
# while True:
#     if listen_wake_up():
#         while True:
#             command = listen_command()
#             print("Final:", command)    