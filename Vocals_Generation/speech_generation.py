from gtts import gTTS
from Text_Generation.Text_Generation import image_description
from Image_Loading.Image_processing import image_loading
import os
import pygame
import time

def speech(text , file_name="description.mp3" , lang='en'):
    speech = gTTS(text,lang=lang,slow=False)
    speech.save(file_name)
    
    pygame.mixer.init()
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    
    pygame.mixer.music.unload()


