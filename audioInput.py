import speech_recognition
from notify import notify
from audioOutput import speak
recognizer = speech_recognition.Recognizer()

def listen():
    	speak('Listening!')
    	with speech_recognition.Microphone() as source:
    		recognizer.adjust_for_ambient_noise(source)
    		audio = recognizer.listen(source)
    	try:
    		return recognizer.recognize_google(audio)
    	except speech_recognition.UnknownValueError:
            notify(message="Could not understand audio")
    	except speech_recognition.RequestError as e:
            notify(message="Connection Problem")
    	return ""