from subprocess import call,getoutput
from audioOutput import speak
from _thread import start_new_thread

def openApp(appName):
    start_new_thread(getoutput,('open -a '+appName,))

def openFile(fileName,direc=""):
    speak("Fetching results, please wait")
    fileWithPath=getoutput("find $HOME/"+direc+" -type f -iname '*"+fileName+"*' 2> /dev/null|head -1 ")
    print(fileWithPath)
    getoutput("open '"+fileWithPath+"'")

#openFile(input())