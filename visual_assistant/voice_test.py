from gtts import gTTS
import pygame
import os
import time

def speak(text, lang='en'):
    """Generates and plays Text-to-Speech audio from a given string."""
    print(f"Generating speech: {text}")
    tts = gTTS(text=text, lang=lang)
    filename = "speech.mp3"
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    # Keep script running while audio plays
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    
    pygame.mixer.quit()
    os.remove(filename) # Clean up the temporary file

# Test the function
speak("Hello! I see a woman holding food. Can I help you with anything else?")