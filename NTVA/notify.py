from os import system

# The notifier function
def notify(title='Nancy: The Virtual Assistant', subtitle='', message='', extra=''):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    return system('terminal-notifier {}'.format(' '.join([m, t, s,extra,'-sound default','-appIcon ./logo.png',])))

# Calling the function
#notify()
#notify(title    = 'A Real Notification',subtitle = 'with python',message  = 'Hello, this is me, notifying you!',extra = '')