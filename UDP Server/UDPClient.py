from socket import *
import string
import random
import time
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
#message = input("Input lowercase sentence:")
#print("Original message: " + message)

#sending first message
#clientSocket.sendto(message.encode(),(serverName,serverPort))
#modifiedMessage,serverAddress = clientSocket.recvfrom(2048)
#print("Modified message: " + modifiedMessage.decode())

#message2 = "message"
#print("Original message: " + message2)

#sending second message
#clientSocket.sendto(message2.encode(),(serverName,serverPort))
#modifiedMessage2,serverAddress = clientSocket.recvfrom(2048)
#print("Modified message2: " + modifiedMessage2.decode())

while True:
    #printing lowercase
    letters=string.ascii_lowercase
    rand_message=''.join(random.choice(letters)for i in range(10))
    print(rand_message)

    clientSocket.sendto(rand_message.encode(),(serverName,serverPort))
    modifiedMessage,serverAddress=clientSocket.recvfrom(2048)
    print("Modified Message: " + modifiedMessage.decode())
    time.sleep(1)

clientSocket.close()