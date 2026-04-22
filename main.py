import time
from Image_Loading.Image_processing import image_loading
from Text_Generation.Text_Generation import image_description
from Vocals_Generation.speech import speak_async

last_run = 0
last_response = ""


def get_navigation_query(mode="forward"):
    if mode == "forward":
        return "Is it safe to move forward?"
    elif mode == "left":
        return "Is it safe to move left?"
    elif mode == "right":
        return "Is it safe to move right?"
    else:
        return "What is directly in front of me?"


while True:
    image_path = "image_bikes.jpeg"  # replace with webcam frame later
    image = image_loading(image_path)

    if time.time() - last_run > 2:  # run every 2 sec
        query = get_navigation_query("forward")
        response = image_description(image, query)

        if response != last_response:
            print("AI:", response)
            speak_async(response)
            last_response = response

        last_run = time.time()