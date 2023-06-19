import speech_recognition as sr
import pyttsx3

# Inisialisasi recognizer
r = sr.Recognizer()

# Inisialisasi text-to-speech engine
engine = pyttsx3.init()

# Fungsi untuk mengubah teks menjadi suara
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Fungsi untuk mengenali suara dan mengubahnya menjadi teks
def recognize_speech():
    with sr.Microphone() as source:
        print("Silakan mulai berbicara...")
        audio = r.listen(source)

        try:
            print("Mengenali suara...")
            text = r.recognize_google(audio, language='id-ID')
            print("Anda mengatakan: ", text)
            return text
        except sr.UnknownValueError:
            print("Maaf, tidak dapat mengenali suara.")
        except sr.RequestError as e:
            print("Terjadi kesalahan pada layanan pengenalan suara: ", str(e))
    
    return None

# Contoh penggunaan
while True:
    speech_text = recognize_speech()
    if speech_text:
        speak("Anda mengatakan: " + speech_text)

