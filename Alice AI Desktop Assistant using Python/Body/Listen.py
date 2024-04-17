import speech_recognition as sr
from googletrans import Translator


# 1 - Listen : Hindi or English

def Listen():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='hi')
        print(f"User said:{query}\n  ")


    except Exception as e:
        print("Say that again please...")
        return ""
    query = str(query).lower()
    return query

print(Listen())

# 2 - Translation

def TranslationHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"You : {data}.")
    return data

# TranslationHinToEng("write text in hindi check this function")

# 3 - Connect

def MicExecution():
    query = Listen()
    data = TranslationHinToEng(query)
    return data

# MicExecution()
