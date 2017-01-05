import requests, bs4, google, os
from audioOutput import speak
from settings import homeDir
from subprocess import call
from notify import notify

def lyrics_down(text):
    text = text.split()
    text = ' '.join(text[text.index('lyrics') + 1:])
    print(text)
    addr = google.lucky(text + 'lyrics.wikia.com')#"http://lyrics.wikia.com/wiki/Twenty_One_Pilots:Ride"
    res = requests.get(addr)
    try:
        res.raise_for_status()
    except:
        notify(message='Error in downloading lyrics')
        speak('Error in downloading lyrics')

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    s = soup.select('.lyricbox')
    n = soup.select('h1')
    col = n[0].get_text().find(':')
    name = n[0].get_text()[:col] + ' ' + n[0].get_text()[col+1:]
    name=name+".txt"
    print(name)

    os.chdir(homeDir+'/Downloads/')
    lyrics = open(name, 'w')

    for i in s[0].get_text('\n').split('\n'):
        lyrics.write('\n')
        lyrics.write(i)
    lyrics.close()
    call(['open','-e',homeDir+'/Downloads/'+name])
    speak("Here are your Lyrics")

#lyrics_down('download lyrics spirits')
