import speech_recognition as sr

def listen_and_convert():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        return text

print(listen_and_convert())
