# AI Vision and Voice Assistant Prototype

**Note:** This repository contains a prototype created strictly for educational purposes and as part of learning Machine Learning (ML), Computer Vision, and Natural Language Processing. It is not intended for production use.

## Description
This project explores the integration of various AI and hardware components to create a voice-interactive vision assistant. It uses a webcam to capture images, evaluates image sharpness, uses the `moondream2` small vision language model to describe the scene, and fetches product data using the Open Food Facts API. It also utilizes Google Translate and Text-to-Speech (TTS) for voice interaction.

## Files Included
* **`main.py`**: The core application script integrating vision, text-to-speech, and API calls.
* **`test_focus.py`**: A utility script to calibrate and test camera focus using Laplacian variance.
* **`test_gpu.py`**: A diagnostic script to verify DirectML GPU acceleration.
* **`vision_test.py`**: A standalone test for the `moondream2` model running on the CPU.
* **`voice_test.py`**: A standalone test for Text-to-Speech functionality using `gTTS` and `pygame`.

## Requirements
Ensure you have the required libraries installed. You will need:
* `opencv-python`
* `torch`
* `transformers`
* `Pillow`
* `gtts`
* `deep-translator`
* `pygame`
* `requests`
* `torch-directml` (if using DirectML on Windows)