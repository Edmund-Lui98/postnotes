# Import socket module
from socket import *
from notes_array import Notes
import sys  # In order to terminate the program
import pickle

# Create a TCP server socket
# (AF_INET is used for IPv4 protocols)
# (SOCK_STREAM is used for TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
serverPort = 1234

# Bind the socket to server address and server port
serverSocket.bind(('', serverPort))

# Listen to at most 1 connection at a time
serverSocket.listen(1)

print('The server is ready to receive')

# Server should be up and running and listening to the incoming connections

#initialize the notes array
notes = Notes()

while True:
    print('The server is ready to receive')

    # Set up a new connection from the client
    connectionSocket, addr = serverSocket.accept()

    cmd = connectionSocket.recv(1024).decode("utf-8")

    #Enter code below

    returns = None
    returns1 = None

    if cmd.startswith("POST"):
        notes.post(cmd[5:])
    elif cmd.startswith("GET"):
        returns1 = notes.get(cmd[4:])
    elif cmd.startswith("PIN"):
        notes.pin(cmd[4:])
    elif cmd.startswith("UNPIN"):
        notes.unpin(cmd[6:])
    elif cmd.startswith("CLEAR"):
        notes.clear()
    elif cmd.startswith("DISCONNECT"):
        break
    else:
        pass

    #this is to send something to the client
    #print(returns1)
    if returns1 != None:
        for x in returns1:
            msg = pickle.dumps(x)
            connectionSocket.send(msg)
    connectionSocket.close()

serverSocket.close()
print("server closed")
sys.exit()# Terminate the program after sending the corresponding data
