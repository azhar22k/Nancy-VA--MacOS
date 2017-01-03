from notify import notify
from audioInput import listen
from subprocess import getoutput
from audioOutput import speak,speakWiki
from datetime import datetime
from re import match,sub
def decor(func):
    def wrap():
        with open("welcome.txt") as fin:
            print(fin.read())
            func()
        print("------------------------------------------------------------------")

    return wrap


@decor
def main():
    Input=""
    notify(message="Service Started",extra="-contentImage ./logo.png -timeout 0.2")
    while Input != "terminate":
        Input = getoutput("terminal-notifier -title Nancy:The_Virtual_Assistant -message Ask_me_something -appIcon ./final.png -sound default -reply Type_Your_Query_Here")
        print('Query= ' + Input)
        #Take Input From Microphone
        if Input == '@CLOSED' or Input == '@CONTENTCLICKED':
            Input = listen()
            from logUpdator import update_log
            update_log(str(datetime.utcnow()),Input)
            print("You said: " + Input)
        Input=Input.lower()
        #no data received
        if Input=="":
            notify(message="Sorry! Did you say something?")
            continue
        #Command for quiting
        if Input in ['quit','terminate']:
            speak("Bye")
            Input='terminate'
            continue
        #Command for Self Intoduction
        if Input in ["who are you", "introduce yourself","describe yourself"]:
                answer='I am Nancy, your personal assistant.'
                notify(title=Input, subtitle='I got this:', message=answer)
                speak(answer)
                continue
        #Command for Owner Information
        if Input in ["who created you", "who is your master","who is your owner"]:
                answer="Team Errorist created me, Although I'm open source!"
                notify(title=Input, subtitle='I got this:', message=answer)
                speak(answer)
                continue
        #Command for opening maps
        if match(r"^open maps.*$",Input):
                from webHandler import openMaps
                Input=Input.replace("open maps"," ")
                openMaps(Input)
                speak("Here It is...")
                continue
        #if match(r"^open $",Input):
         #   continue
        #Commamnd for browsing a website
        if match(r"^browse .*$",Input):
            from webHandler import browseUrl
            Input = Input.replace("browse "," ")
            browseUrl(Input)
            continue
        #Command to throw a dice
        if match(r"^throw a dice$",Input):
            from randomStuff import dice
            output=str(dice())
            notify(message=output)
            speak(output)
            continue
        #Command to toss a coin
        if match(r"^toss a coin$",Input):
            from randomStuff import coin
            output=coin()
            notify(message=output)
            speak(output)
            continue

        #Command to download mp3 song
        if match(r"^download (audio)|(song) .*$",Input):
            from mp3Download import page_link
            Input=sub(r"download audio|song|mp3 ", '',Input)
            page_link(Input)
            continue

        #Command to download mp4 video
        if match(r"^download video .*$",Input):
            from mp4Download import youtube_link
            Input=sub(r"download video ", '',Input)
            youtube_link(Input)
            continue
        #Command to read it aloud
        if match(r"^(read out)|(speak out loud)$",Input):
            from pyperclip import paste
            speak(paste())
            continue
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


if __name__ == '__main__':
    main()