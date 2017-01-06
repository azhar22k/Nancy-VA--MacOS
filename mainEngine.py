from notify import notify
from audioInput import listen
from subprocess import getoutput
from datetime import datetime
from queryResponder import search
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
        search(Input)


if __name__ == '__main__':
    main()