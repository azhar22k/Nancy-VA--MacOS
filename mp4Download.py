from os import chdir
from pytube import YouTube
from pprint import pprint
from audioOutput import  speak
from settings import homeDir
from google import lucky


def vid_download(link):
    chdir(homeDir+'/Downloads/')
    yt = YouTube(link)

    pprint(yt.get_videos())
    quality = ['720p', '480p', '360p']
    for i in quality:
        try:
            video = yt.get('mp4', i)
            speak('Downloading in ' + i + " " + yt.filename)
            video.download('.')
            speak('Download Complete')
            break
        except:
            continue
    else:
        return 'Not found in good quality'


def youtube_link(text):
    link = lucky(text+' youtube')
    vid_download(link)


#youtube_link(input() + ' youtube')
#vid_download('https://www.youtube.com/watch?v=Ib8XaRKCAfo')
