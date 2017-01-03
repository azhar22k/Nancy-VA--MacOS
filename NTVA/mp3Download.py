import requests, bs4, os
from audioOutput import speak
from settings import  homeDir
from notify import notify

def download_song(link, name):
    os.chdir(homeDir+'/Downloads/')
    notify(message='Downloadling '+name+'...')
    speak('Downloading ' + name + '...')
    res = requests.get(link)
    try:
        res.raise_for_status()
    except:
        speak('Downloading Error')
        return False
    song = open(name, 'wb')
    for chunk in res.iter_content(100000):
        song.write(chunk)
    song.close()
    notify(message='Download Comlete: '+name+'...')
    speak('Download finished')
    return True


def download_link(addr):
    res = requests.get(addr)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    s = soup.select('a')
    link = []
    for i in s:
        try:
            if "Download In" in i.get_text('strong'):# and "Quality" in i.get_text('strong'):
                link.append(i.get('href'))
        except:
            pass
    try:
        name = link[-1][len(link[-1]) - link[-1][::-1].find('/'):]
    except IndexError:
        return False
    return download_song(link[-1], name)


def page_link(name):
    name += ' mp3mad'
    res = requests.get('https://google.com/search?q=' + name)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    opt = soup.select('.r a')
    for link in opt[:3]:
        try:
            addr = link.get('href')
            addr = addr[7:addr.index('&')]
            print('trying -> ' + addr)
            if download_link(addr):
                break
        except IndexError:
            pass
    else:
        return "No Link found"


#page_link(input())

