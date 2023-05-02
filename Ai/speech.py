# su dung module google text to speech de chuyen doi chu sang ma am thanh va luu
# vao file mp3
# su dung module playsound de phat doan nhac da luu

from gtts import gTTS  
import playsound
def speech(text):
    # chuyen dona text o dang ngon ngw lang sang ma am thanh va gan cho bien
    output = gTTS(text,lang="vi")
    # luu doan ma vao file mp3
    output.save("output.mp3")
    # phat doan am thanh 
    playsound.playsound('output.mp3')