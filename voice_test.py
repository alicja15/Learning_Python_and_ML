from gtts import gTTS
import pygame
import os
import time

def speak(text, lang='pl'):
    print(f"Generuję mowę: {text}")
    tts = gTTS(text=text, lang=lang)
    filename = "speech.mp3"
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    
    pygame.mixer.quit()
    os.remove(filename) # Sprzątamy po sobie

speak("Cześć! Widzę kobietę trzymającą jedzenie. Czy mogę ci jeszcze w czymś pomóc?")