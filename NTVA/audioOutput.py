from subprocess import call,getoutput
from settings import homeDir
from gtts import gTTS
from randomStuff import connectionStatus

def speak(text):
    if connectionStatus()==True:
        path = homeDir + "/Downloads/speech.mp3"
        tts = gTTS(text, lang="hi")
        tts.save(path)
        getoutput("mpg123 " + path)
    else:
        call(['say', text])


#wikipedia coreection
def speakWiki(script):
    from re import sub
    script = sub(r"\(.*?\)", '',script)
    print(script)
    speak(script)

#speak("Heloo Azhar Khan")