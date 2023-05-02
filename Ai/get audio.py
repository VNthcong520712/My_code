import speech_recognition as sp
r = sp.Recognizer()
with sp.Microphone() as au:
    print("Me: ", end = '')
    audio = r.listen(au, phrase_time_limit=10)
    try:
        text = r.recognize_google(audio, language="vi-VN")
        print(text)
    except:
        print("...?")