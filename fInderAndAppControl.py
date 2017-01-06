from subprocess import call
def openApp(appName):
    call(['open','-a',appName])