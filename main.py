import time
from Image_Loading.Image_processing import image_loading
from Text_Generation.Text_Generation import image_description
from Vocals_Generation.speech import speak
from Voice_recorder import listen_command , listen_wake_up
from intent_detection import detect_task , get_intent
from chat_model import chat_response
from image_loader import capture_image

while True:
    if listen_wake_up():

        while True:
            text = listen_command()

            task , score = detect_task(text)
            intent = get_intent(task)
            print(intent)
            
            if "stop" in text or "exit" in text:
                print(" Assistant stopped")
                break

            if intent == "vision":
                img = capture_image()
                description = image_description(img)
                speak(description)

            else:
                text = chat_response(text)
                speak(text)

