import pyttsx3

def read_book(file_path):
    engine = pyttsx3.init()
    try:
        with open(file_path, 'r') as book:
            book_text = book.read()
            engine.say(book_text)
            engine.runAndWait()
    except FileNotFoundError:
        print(f"Nie znaleziono pliku: {file_path}")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

# Użycie funkcji
read_book("book.txt")