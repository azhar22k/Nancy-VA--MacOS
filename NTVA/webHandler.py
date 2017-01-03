from webbrowser import open_new_tab
from pyperclip import paste

#open Google Maps of a Location
def openMaps(address):
    if address == "":
        address = paste()
    open_new_tab("http://www.google.com/maps/place/"+address)

#open a url in new tab
def browseUrl(text):
    from google import lucky
    from audioOutput import speak
    try:
        url=lucky(text)
        open_new_tab(url)
        speak("here it is")
    except:
        speak('Something went wrong!!!')

