import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image
import requests

# 1. Wymuszamy CPU - to zadziała na każdym komputerze
device = "cpu" 
print(f"Używam urządzenia: {device}")

# reszta kodu pozostaje bez zmian (model_id, image_url itd.)
model_id = "vikhyatk/moondream2"
revision = "2024-03-06"

print("Ładowanie modelu na CPU...")
model = AutoModelForCausalLM.from_pretrained(
    model_id, 
    trust_remote_code=True, 
    revision=revision
).to(device)

tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)

print("Pobieranie obrazka...")
image_url = "https://raw.githubusercontent.com/vikhyat/moondream/main/assets/demo-1.jpg"
image = Image.open(requests.get(image_url, stream=True).raw)

print("Analizuję na CPU (może to potrwać 10-20 sekund)...")
enc_image = model.encode_image(image)
answer = model.answer_question(enc_image, "Describe this image in detail.", tokenizer)

print("-" * 30)
print(f"WYNIK: {answer}")
print("-" * 30)