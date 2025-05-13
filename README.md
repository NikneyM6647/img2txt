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

## Будущие возможности: 
### 1. Будет добавлен нормальный GUI.(и в него все будущие функции связанные с GUI)

### 2.Будет добавлена история изображений и текста, которая будет хранится в отдельной папке с еще двумя папками в которых будут все файлы.
Все будет выглядеть примерно так:
img2txt/history/img/001_img.png
img2txt/history/txt/001_txt.txt

### 3.Добавлю файл языков чтоб не бежать по другим репозиториям.

### 4. Скрипт скомпилируется в .exe файл


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
     

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   
## Future opportunities: 
### 1. A normal GUI will be added.(and all future GUI-related functions
will be added to it) 
### 2. The history of images and text will be added, which will be stored in a separate folder with two more folders in which all files will be.
It will look something like this:
img2txt/history/img/001_img.png
img2txt/history/txt/001_txt.txt
### 3.I will add a language file so as not to run through other repositories.
### 4. The script is compiled into an .exe file.