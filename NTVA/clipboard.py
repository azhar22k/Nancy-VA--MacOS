from pyperclip import paste
a=paste()
from subprocess import call
call(['say',a])