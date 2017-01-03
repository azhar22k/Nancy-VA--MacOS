from random import randint
#Throw a dice
def dice():
    return randint(1,6)

#Toss a coin
def coin():
    output=['heads','tails']
    return "It's "+output[randint(0,1)]

#check Net connection
import socket

def connectionStatus():
    ipaddress = socket.gethostbyname(socket.gethostname())
    if ipaddress == "127.0.0.1":
        return False
    else:
        return True