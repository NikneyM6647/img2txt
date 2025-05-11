import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
from PIL import Image, ImageTk
import pytesseract
import threading

# Укажите путь к Tesseract (если требуется)
pytesseract.pytesseract.tesseract_cmd = r"D:\Programms\forTesseract\tesseract.exe"

def recognize_text_from_image(image_path, lang_code):
    """
    Распознает текст на изображении с использованием Tesseract OCR.
    :param image_path: Путь к изображению
    :param lang_code: Код языка для распознавания (например, 'eng', 'rus')
    """
    try:
        # Открываем изображение с помощью Pillow
        image = Image.open(image_path)
        
        # Используем pytesseract для распознавания текста
        config = '--psm 6 --oem 1'
        text = pytesseract.image_to_string(image, lang=lang_code, config=config)
        
        return text
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")
        return ""


def select_image():
    """
    Открывает диалоговое окно для выбора изображения.
    """
    file_path = filedialog.askopenfilename(
        title="Выберите изображение",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.tiff")]
    )
    if file_path:
        entry_image_path.delete(0, tk.END)  # Очищаем поле ввода
        entry_image_path.insert(0, file_path)  # Вставляем путь к выбранному файлу
        
        # Показываем предварительный просмотр изображения
        show_image_preview(file_path)


def show_image_preview(image_path):
    """
    Показывает предварительный просмотр изображения.
    """
    try:
        # Открываем изображение с помощью Pillow
        image = Image.open(image_path)
        
        # Масштабируем изображение для предварительного просмотра
        max_size = (300, 300)  # Максимальный размер для предпросмотра
        image.thumbnail(max_size)
        
        # Преобразуем изображение для Tkinter
        tk_image = ImageTk.PhotoImage(image)
        
        # Обновляем метку с изображением
        image_label.config(image=tk_image)
        image_label.image = tk_image  # Сохраняем ссылку, чтобы избежать удаления garbage collector'ом
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось открыть изображение: {e}")


def process_image():
    """
    Обрабатывает выбранное изображение и выводит распознанный текст.
    """
    image_path = entry_image_path.get()
    if not image_path:
        messagebox.showwarning("Предупреждение", "Пожалуйста, выберите изображение.")
        return
    
    # Получаем выбранный язык
    lang_code = languages[selected_language.get()]
    
    # Запускаем распознавание текста в отдельном потоке
    threading.Thread(target=recognize_and_update_ui, args=(image_path, lang_code)).start()


def recognize_and_update_ui(image_path, lang_code):
    """
    Распознает текст и обновляет интерфейс пользователя.
    """
    # Включаем прогресс-бар
    progress_bar.start()
    
    # Распознаем текст
    text = recognize_text_from_image(image_path, lang_code)
    
    # Останавливаем прогресс-бар
    progress_bar.stop()
    
    # Очищаем текстовое поле и вставляем результат
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, text)


# Создаем главное окно
root = tk.Tk()
root.title("Распознавание текста на изображении")
root.geometry("800x600")
root.configure(bg="#f0f0f0")

# Поле для пути к изображению
label_image_path = tk.Label(root, text="Путь к изображению:", font=("Arial", 12), bg="#f0f0f0")
label_image_path.pack(pady=5)

entry_image_path = tk.Entry(root, width=50, font=("Arial", 12))
entry_image_path.pack(pady=5)

# Кнопка для выбора изображения
button_select_image = tk.Button(root, text="Выбрать изображение", font=("Arial", 12), command=select_image)
button_select_image.pack(pady=10)

# Предварительный просмотр изображения
image_label = tk.Label(root, bg="#f0f0f0")
image_label.pack(pady=10)

# Выпадающее меню для выбора языка
languages = {"Английский": "eng", "Русский": "rus", "Французский": "fra"}
selected_language = tk.StringVar(value="eng")

label_language = tk.Label(root, text="Выберите язык:", font=("Arial", 12), bg="#f0f0f0")
label_language.pack()

dropdown_language = ttk.Combobox(root, textvariable=selected_language, values=list(languages.keys()), state="readonly")
dropdown_language.pack(pady=5)

# Прогресс-бар
progress_bar = ttk.Progressbar(root, mode="indeterminate", length=400)
progress_bar.pack(pady=10)

# Кнопка для обработки изображения
button_process_image = tk.Button(root, text="Распознать текст", font=("Arial", 14), bg="#4CAF50", fg="white", command=process_image)
button_process_image.pack(pady=20)

# Текстовое поле для вывода результата
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=10, font=("Arial", 12))
text_area.pack(pady=10)

# Запускаем главный цикл
root.mainloop()