from subprocess import getoutput
from audioOutput import speak
from _thread import start_new_thread

def openApp(appName):
    start_new_thread(getoutput,('open -a '+appName,))

def openFile(fileName,direc=""):
    speak("Fetching results, please wait")
    fileWithPath=getoutput("find $HOME/"+direc+" -type f -iname '"+fileName+"*' 2> /dev/null|head -1 ")
    print(fileWithPath)
    getoutput("open '"+fileWithPath+"'")
    speak("Here it is")

def openFolder(folderName):
    speak("Fetching results plaese wait")
    fileWithPath = getoutput("find $HOME/ -type d -iname '" + folderName + "*' 2> /dev/null|head -1 ")
    print(fileWithPath)
    getoutput("open '" + fileWithPath + "'")
    speak("here it is")

#openFile(input())