# Import socket module
from socket import *
from notes_array import Notes
import sys  # In order to terminate the program
import pickle

#take args from the command line
arg = sys.argv
print(arg)
sport = arg[1]
boardWidth = int(arg[2])
boardHeight = int(arg[3])
colors = []
for i in range(4, len(arg)):
    colors.append(arg[i])

print("""Port Number: {}
Board width: {}
Board height: {}
Colors available: {}(default),{}""".format(sport, boardWidth, boardHeight, colors[0],colors[1:]))

# Create a TCP server socket
# (AF_INET is used for IPv4 protocols)
# (SOCK_STREAM is used for TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
serverPort = int(sport)

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

    if cmd.startswith("POST"):
        notes.post(cmd[5:])
    elif cmd.startswith("GET"):
        returns = notes.get(cmd[4:])
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

    #print(returns)
    if returns != None:
        msg = pickle.dumps(returns)
        connectionSocket.send(msg)
    connectionSocket.close()

serverSocket.close()
print("server closed")
sys.exit()# Terminate the program after sending the corresponding data
