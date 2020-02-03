# Import socket module
from socket import *
import sys # In order to terminate the program
import pickle

serverName = 'localhost'
# Assign a port number
serverPort = 1234

# Bind the socket to server address and server port
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))
sentence = input(' Input note (FUNCTION xPos yPos width height color msg): ')
clientSocket. send(sentence.encode("utf-8"))


modifiedSentence = clientSocket.recv(1024)
if sentence.startswith("GET") == False:
    pass
elif modifiedSentence == b'':
    print("No notes")
else:
    lst = pickle.loads(modifiedSentence)

    for attribute in lst:
        print("""
        msg: {}
        pinned status: {}
        xposition: {}
        yposition: {}
        width: {}
        height: {}
        color: {}""".format(attribute.msg, attribute.status, attribute.xposition, attribute.yposition, attribute.width, attribute.height, attribute.color))

clientSocket.close()

