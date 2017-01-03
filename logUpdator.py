#Function update logs for microphone Input
def update_log(timeStramp,text):
    with open('microphone_log.txt','a') as f:
        f.write(timeStramp+" "+text + '\n')