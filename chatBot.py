from chatterbot import ChatBot

chatbot = ChatBot('Nancy',read_only=True)



# Get a response to an input statement
while(True):
    print(chatbot.get_response(input("You:")))

