"RU"
# Распознавание текста на изображении

Это приложение позволяет распознавать текст на изображениях с помощью Tesseract OCR. Поддерживаются английский и русский языки.

## Установка

1. Установите Python (версия 3.8 или выше):
   - [Скачать Python](https://www.python.org/downloads/ )

2. Установите Tesseract OCR:
   - Для Windows: скачайте и установите [Tesseract OCR](https://github.com/tesseract-ocr/tesseract ).
     - Добавьте путь к Tesseract в переменную окружения `PATH`.
   - Для Linux:
     ```bash
     sudo apt install tesseract-ocr tesseract-ocr-rus
     ```
   - Для macOS:
     ```bash
     brew install tesseract tesseract-lang
     ```

3. Установите зависимости Python:
   ```bash
   pip install -r requirements.txt
  "ENG"
  # Recognition of text in an image

This application allows you to recognize text in images using Tesseract OCR. English and Russian languages are supported.

## Installation

1. Install Python (version 3.8 or higher):
- [Download Python](https://www.python.org/downloads / )

2. Install Tesseract OCR:
- For Windows: Download and install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract ).
     - Add the path to Tesseract to the environment variable `PATH'.
   - For Linux:
     ```bash
     sudo apt install tesseract-ocr tesseract-ocr-rus
     ``
- For macOS:
     ```bash
     brew install tesseract tesseract-lang
     ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
