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
else:
    x = pickle.loads(modifiedSentence)
    print("""msg {}
    status {}
    xpos {}
    ypos {}
    width {}
    height {}
    color {}""".format(x.msg, x.status, x.xposition,x.yposition, x.width,x.height,x.color))
    print('From server: ', x)


clientSocket.close()

