# Import socket module
from socket import *
import sys # In order to terminate the program
import pickle # Used to return objects
class Note:
    def __init__(self, msg, status, xposition, yposition, width, height, color):
        """
        -------------------------------------------------------
        Put note in the server
        -------------------------------------------------------
        Parameters:
            msg - note given by the client (string)
            status - number of times pinned (int > 0)
            xposition - x coordinate value of the lower left corner (int)
            yposition - y coordinate value of the lower left corner (int)
            width - width of the note (int)
            height - height of the note (int)
            color - color of the note (string)
        Returns:
            None
        -------------------------------------------------------
        """
        self.msg = msg
        self.status = status
        self.xposition = xposition
        self.yposition = yposition
        self.width = width
        self.height = height
        self.color = color

        return

serverName = "localhost"
# Assign a port number
serverPort = 4554

print("""Server name: {}
Port number: {}""".format(serverName,serverPort))

# Bind the socket to server address and server port
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))
sentence = input(' Input note (FUNCTION xPos yPos width height color msg): ')
clientSocket. send(sentence.encode("utf-8"))
#recieve from the server
returned_data = clientSocket.recv(1024)
if sentence.startswith("GET") == False:
    pass
elif returned_data == b'':
    print("No notes")
else:
    lst = pickle.loads(returned_data)

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

