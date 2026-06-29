import cv2
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image
from gtts import gTTS
from deep_translator import GoogleTranslator
import pygame
import os
import time
import requests

# --- CONFIGURATION ---
DEVICE = "cpu"
MODEL_ID = "vikhyatk/moondream2"
REVISION = "2024-03-06"

PROMPT_PLAN_A = "Read the nutrition table and tell me the sugar content per 100g."
PROMPT_PLAN_B = "Identify the product: name the brand, product type, and specify its size or flavor based on the packaging."

def speak(text_en):
    """Translates English text to local language (or keeps it English) and plays it via TTS."""
    # 1. Translate to English (or target language) - kept as EN to EN for consistency in this English version
    try:
        text_translated = GoogleTranslator(source='en', target='en').translate(text_en)
        print(f"EN: {text_en}")
        print(f"Translated: {text_translated}")
    except Exception:
        text_translated = "Translation error"

    # 2. Read the text aloud
    tts = gTTS(text=text_translated, lang='en')
    tts.save("temp.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()
    
    # Wait until audio finishes playing
    while pygame.mixer.music.get_busy(): 
        time.sleep(0.1)
        
    pygame.mixer.quit()
    os.remove("temp.mp3")

# Store the last recognized product data
last_recognized_product = {
    "description": None, # e.g., "Green juice 500ml"
    "sugar_info": None   # e.g., "10g"
}

def search_open_food_facts(product_description):
    """Searches the Open Food Facts API for the given product description."""
    # Create the query URL (searching by name)
    url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={product_description}&search_simple=1&action=process&json=1"
    
    response = requests.get(url)
    data = response.json()
    
    products = data.get('products', [])
    
    if not products:
        return "Product not found in the database."

    # Select the first 3 results
    results = []
    for p in products[:3]:
        name = p.get('product_name', 'Unknown product')
        sugar = p.get('nutriments', {}).get('sugars_100g', 'no data')
        results.append(f"{name} (Sugar: {sugar}g)")
    
    return results

def listen_for_voice(timeout=5):
    """Dummy function to simulate voice listening. Replace with actual STT logic."""
    print("Listening for user input...")
    time.sleep(1)
    return "timeout" # Returning timeout as placeholder

def handle_user_choice(products_list):
    """Handles the user's selection from a list of found products."""
    # products_list example: [("Juice Brand A", 10), ("Juice Brand B", 12)]
    
    attempts = 0
    while attempts < 2:
        # 1. Read the list aloud
        speak("I found a few matching products:")
        for i, (name, sugar) in enumerate(products_list, 1):
            speak(f"Number {i}: {name}")
        
        speak("Say the product number or say 'average' to get the approximate value.")

        # 2. Listen for response (with a 5-second timeout)
        user_input = listen_for_voice(timeout=5)

        if user_input == "timeout":
            speak("I didn't hear an answer. Should I repeat the list or provide the average?")
            attempts += 1
        elif "average" in user_input:
            avg_sugar = sum(p[1] for p in products_list) / len(products_list)
            speak(f"The average sugar content is approximately {avg_sugar:.1f} grams.")
            return
        elif user_input.isdigit():
            idx = int(user_input) - 1
            if 0 <= idx < len(products_list):
                name, sugar = products_list[idx]
                speak(f"You selected {name}. It contains {sugar} grams of sugar.")
                return

def calculate_focus(frame):
    """Calculates the sharpness of the image using Laplacian variance."""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return cv2.Laplacian(gray, cv2.CV_64F).var()

print("Loading AI model (please wait)...")
model = AutoModelForCausalLM.from_pretrained(MODEL_ID, trust_remote_code=True, revision=REVISION).to(DEVICE)
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, revision=REVISION)

# Check camera index (usually 0, if it doesn't work, try 1)
cap = cv2.VideoCapture(0)

print("\n--- ASSISTANT READY ---")
print("SPACE - Describe photo | Q - Quit")

low_focus_start_time = None  # Time when the image started being blurry
attempt_counter = 0

while True:
    ret, frame = cap.read()
    if not ret: 
        break

    cv2.imshow('Camera View', frame)
    key = cv2.waitKey(1)

    # Calculate focus constantly for background tracking
    focus_value = calculate_focus(frame)
    
    if focus_value < 20:
        if low_focus_start_time is None:
             low_focus_start_time = time.time()
        # If blurry for more than 3 seconds - reset counters
        elif time.time() - low_focus_start_time > 3:
            if attempt_counter > 0:
                print("Product removed. Resetting counter.")
                attempt_counter = 0
            low_focus_start_time = None
    else:
        # Image is sharp - user is holding something
        low_focus_start_time = None

    # Handle spacebar press
    if key == ord(' '):
        print("Analyzing image...")
        color_converted = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(color_converted)

        # Encode and process the image through the AI model
        enc_image = model.encode_image(pil_image)
        description = model.answer_question(enc_image, "Describe in 1 short sentence what is in front of the camera.", tokenizer)
        
        speak(description)

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()