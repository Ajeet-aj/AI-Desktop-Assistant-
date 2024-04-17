import speech_recognition as sr
import os

def Listen():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print(f"User said:{query}\n  ")


    except:
        return ""
    query = str(query).lower()
    print(query)
    return query


def WakeupDetected():
    queery = Listen().lower()

    if "wakw up" in queery:
        os.startfile(r"C:\Users\priya\PycharmProjects\Jarvis AI\Main.py")

    else:
        pass
while True:
    WakeupDetected()