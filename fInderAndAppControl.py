from subprocess import call,getoutput
from audioOutput import speak

def openApp(appName):
    call(['open','-a',appName])

def openFile(fileName):
    speak("Fetching results, please wait")
    fileWithPath=getoutput("find $HOME -type f -iname '*"+fileName+"*'|head -1")
    print(fileWithPath)
    if '.mp3 ' in fileWithPath:
        call(['mpg123',fileWithPath])
    else:
        call(['open',fileWithPath])