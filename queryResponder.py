from notify import notify
from re import match,sub
from audioOutput import speak,speakWiki
from _thread import start_new_thread
from subprocess import getoutput
def search(Input):
    # no data received
    if Input == "":
        notify(message="Sorry! Did you say something?")
        return

    # Command for quiting
    if Input in ['quit', 'terminate']:
        speak("Bye")
        Input = 'terminate'
        return

    #Command to lock PC
    if Input in ['lock','lock my mac','lock my pc']:
        speak("See you soon")
        getoutput("/System/Library/CoreServices/Menu\ Extras/User.menu/Contents/Resources/CGSession -suspend")
        return

    #Command to reboot
    if Input in ['reboot', 'reboot my mac', 'reboot my pc']:
        speak("See you soon")
        getoutput("osascript -e 'tell application \"System Events\" to restart'")
        return

    # Command to shutdown
    if Input in ['shutdown', 'shutdown my mac', 'shutdown my pc']:
        speak("See you soon")
        getoutput("osascript -e 'tell application \"System Events\" to shut down'")
        return

    # Command for Self Intoduction
    if Input in ["who are you", "introduce yourself", "describe yourself"]:
        answer = 'I am Nancy, your personal assistant.'
        notify(title=Input, subtitle='I got this:', message=answer)
        speak(answer)
        return

    # Command for Owner Information
    if Input in ["who created you", "who is your master", "who is your owner"]:
        answer = "Team Errorist created me, Although I'm open source!"
        notify(title=Input, subtitle='I got this:', message=answer)
        speak(answer)
        return

    # Command for opening maps
    if match(r"^open maps.*$", Input):
        from webHandler import openMaps
        Input = Input.replace("open maps", " ")
        openMaps(Input)
        speak("Here It is...")
        return

    # Command for downloading lyrics
    if match(r"^download lyrics.*$", Input):
        from lyrics import lyrics_down
        lyrics_down(Input)
        return

    #Command to open Applications
    if match(r"^execute.*$",Input):
        from fInderAndAppControl import openApp
        Input=Input.replace("execute ","")
        openApp(Input)
        speak('There you go')
        return

    #Command to open a file
    if match(r"^open file.*$",Input):
        Input=Input.replace("open file ","")
        from fInderAndAppControl import openFile
        openFile(Input)
        return

    #Command to open a directory
    if match(r"^open folder.*$",Input):
        Input=Input.replace("open folder ","")
        from  fInderAndAppControl import openFolder
        openFolder(Input)
        return

    #Command to play a song
    if match(r"^play song.*$",Input):
        Input=Input.replace("play song ","")
        from fInderAndAppControl import openFile
        openFile(Input,direc="Music")
        return

    #Command to play video
    if match(r"^play video.*$",Input):
        Input=Input.replace("play video ","")
        from fInderAndAppControl import openFile
        openFile(Input,direc="Movies")
        return

    # Commamnd for browsing a website
    if match(r"^browse.*$", Input):
        from webHandler import browseUrl
        Input = Input.replace("browse ", " ")
        browseUrl(Input)
        return

    # Command to throw a dice
    if match(r"^throw a dice$", Input):
        from randomStuff import dice
        output = str(dice())
        notify(message=output)
        speak(output)
        return

    # Command to toss a coin
    if match(r"^toss a coin$", Input):
        from randomStuff import coin
        output = coin()
        notify(message=output)
        speak(output)
        return

    # Command to download mp3 song
    if match(r"^download (audio)|(song).*$", Input):
        from mp3Download import page_link
        Input = sub(r"download audio|song|mp3 ", '', Input)
        #page_link(Input)
        start_new_thread(page_link,(Input,))
        return

    # Command to download mp4 video
    if match(r"^download video.*$", Input):
        from mp4Download import youtube_link
        Input = sub(r"download video ", '', Input)
        #youtube_link(Input)
        start_new_thread(youtube_link,(Input,))
        return

    # Command to read it aloud
    if match(r"^(read out)|(speak out loud)$", Input):
        from pyperclip import paste
        speak(paste())
        return
    try:
        from settings import client
        print('Trying wolframalpha')
        result = client.query(Input)
        answer = next(result.results).text
        notify(title=Input, subtitle='I got this:', message=answer)
        speak(answer)
    except:
        try:
            print('Trying wikipedia')
            from wikipedia import summary
            answer = summary(Input, sentences=1)
            print(answer)
            notify(title=Input, subtitle='I got this:', message=answer)
            speakWiki(answer)
        except Exception as err:
            notify(message='Opps Nothing Found', extra='-timeout 1')