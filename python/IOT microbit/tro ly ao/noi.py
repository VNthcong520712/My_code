import pyttsx3

eng = pyttsx3.init()
voi = eng.getProperty("voices")
eng.setProperty("voice",voi[1].id)

eng.say("xin chào các bạn")
eng.runAndWait()