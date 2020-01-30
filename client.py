# Import socket module
from socket import *
import sys # In order to terminate the program

serverName = 'localhost'
# Assign a port number
serverPort = 1234

# Bind the socket to server address and server port
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))
sentence = input(' Input note: ')
clientSocket. send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)

print('From server: ', modifiedSentence.decode())
clientSocket.close()

