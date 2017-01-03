#wolframalpha settings
from wolframalpha import Client
app_id = "TGRUL2-794AT5556P"
client = Client(app_id)

#getting user directory
from subprocess import getoutput
homeDir = getoutput('echo $HOME')
