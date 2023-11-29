from gtts import gTTS
import os

def read_book(file_path):
    try:
        with open(file_path, 'r') as book:
            book_text = book.read()
            tts = gTTS(text=book_text, lang='pl') # Można zmienić język, jeśli potrzebujesz
            tts.save("book.mp3") # Zapisuje wypowiedziane słowa do pliku mp3
    except FileNotFoundError:
        print(f"Nie znaleziono pliku: {file_path}")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

    # Odtwarzanie pliku mp3
    os.system("start book.mp3") # 'start' dla Windows, 'open' dla macOS lub 'xdg-open' dla Linux

# Użycie funkcji
read_book("book.txt")
