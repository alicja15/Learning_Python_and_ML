import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image
import requests

# 1. Force CPU usage - this will work on any computer
device = "cpu" 
print(f"Using device: {device}")

# Model configuration
model_id = "vikhyatk/moondream2"
revision = "2024-03-06"

print("Loading model on CPU...")
model = AutoModelForCausalLM.from_pretrained(
    model_id, 
    trust_remote_code=True, 
    revision=revision
).to(device)

tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)

print("Downloading image...")
image_url = "https://raw.githubusercontent.com/vikhyat/moondream/main/assets/demo-1.jpg"
image = Image.open(requests.get(image_url, stream=True).raw)

print("Analyzing on CPU (this may take 10-20 seconds)...")
enc_image = model.encode_image(image)
answer = model.answer_question(enc_image, "Describe this image in detail.", tokenizer)

print("-" * 30)
print(f"RESULT: {answer}")
print("-" * 30)