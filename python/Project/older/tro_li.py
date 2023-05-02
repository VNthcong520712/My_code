import speech_recognition
import pyttsx3
from datetime import date, datetime
ass_ear = speech_recognition.Recognizer()
ass_mouth = pyttsx3.init()



while True:
	with speech_recognition.Microphone() as mic:
		print("I am listening")
		audio =  ass_ear.listen(mic)

	try:
	    you = ass_ear.recognize_google(audio)
	except:
		you = ""
	print('You:  ' + (you))

	if "ok" in you.lower() or "okay" in you.lower():

		if 'hello' in you.lower() or 'hi' in you.lower():
			ass_brain = 'Hello Cong, have a nice day'
		elif 'how are you' in you.lower():
			ass_brain = "I'm fine, thank you, and you" 
		elif 'old' in you.lower():
			ass_brain = "1 old, probably so"
		elif 'president' in you.lower():
			if 'japan' in you.lower():
				ass_brain = "Shinzo Abe"
			elif 'america' in you.lower():
				ass_brain = 'Joe Biden'
			elif 'vietnam' in you.lower():
				ass_brain = '''prime minister is: Nguyen Xuan Phuc
		and president is: Pham Minh Chinh'''
			else:
			     ass_brain = 'Can you say more about it'
		elif you.lower() == 'stop':
		    ass_brain = "I will turn off"
		elif 'today' in you.lower():
			today = date.today()
			ass_brain = today.strftime("%B %d, %Y")
		elif 'time' in you.lower():
			now = datetime.now()
			ass_brain = now.strftime("%H hours %M minutes %S seconds")
		elif you == "":
			ass_brain = "(*￣3￣)╭"
		elif 'bye' in you.lower():
			ass_brain = "Good bye"
			print('Robot: ' + (ass_brain))
			ass_mouth.say(ass_brain)
			ass_mouth.runAndWait()
			break
		else:
		 	ass_brain = "I don't understand, can you try again"
		print('Robot: ' + (ass_brain))


		if ass_brain != "(*￣3￣)╭":
			ass_mouth.say(ass_brain)
			ass_mouth.runAndWait()
	else:
		continue