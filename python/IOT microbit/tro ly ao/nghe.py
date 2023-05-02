import speech_recognition
voice = speech_recognition . Recognizer ()
try:
	with speech_recognition . Microphone () as mic :
		print ("I am listenning ... ")
		audio = voice . listen (mic)
		input_text = voice . recognize_google ( audio )
	print ( input_text )
except:
	print("I can't listen")