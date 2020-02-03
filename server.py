# Import socket module
from socket import *
import sys  # In order to terminate the program
import pickle

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

class Notes:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty stack. Data is stored in a Python list.
        Use: stack = Stack()
        -------------------------------------------------------
        Returns:
            a new Stack object (Stack)
        -------------------------------------------------------
        """
        self._values = []


    def post(self, msg):
        """
        -------------------------------------------------------
        Put note in the server
        -------------------------------------------------------
        Parameters:
            msg - breaks the messages down into separate attributes
        Returns:
            None
        -------------------------------------------------------
        """
        lst = msg.split(" ")

        status = False
        xpos = int(lst[0])
        ypos = int(lst[1])
        width = int(lst[2])
        height = int(lst[3])
        color = lst[4]
        msg1 = ""

        for i in range(5, len(lst)):
            msg1 += lst[i] + " "

        self._values.append(Note(msg1, status, xpos, ypos, width, height, color))

        return

    def get(self, condition):
        """
        -------------------------------------------------------
        Returns all notes stored in the array that satisfy properties described in <params>.
        -------------------------------------------------------
        Parameters:
            condition: A string of conditions on what note object to return
            None: returns all messages
        Returns:
            list of notes object - the message note on the server
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty list"

        notes = []
        # return all
        if len(condition) == 0:
            notes = self._values
            return notes

        lst = condition.split(" ")

        position = 0


        #first filter for the condition
        if lst[position].startswith("color="):
            for value in self._values:
                if value.color == lst[position][6:]:
                    notes.append(value)
            position += 1

        elif lst[position].startswith("refersTo="):
            for value in self._values:
                if lst[position][9:] in value.msg:
                    notes.append(value)
            position += 1

        elif lst[position].startswith("contains="):
            xpos = int(lst[position + 1])
            ypos = int(lst[position + 2])
            position += 3
            for value in self._values:
                if (xpos >= value.xposition and xpos <= (value.xposition + value.height)) and \
                        (ypos >= value.yposition and ypos <= (value.yposition + value.height)):
                    notes.append(value)

        elif lst[position].startswith("PINS"):
            for value in self._values:
                if value.status > 0:
                    notes.append(value)
            position += 1

        #second filter for the condition
        if len(lst) > position:
            if lst[position].startswith("color="):
                for value in range(len(notes)):
                    if notes[value].color != lst[position][6:]:
                        notes.pop(value)

            elif lst[position].startswith("refersTo="):
                for value in range(len(notes)):
                    if lst[position][9:] not in notes[value].msg:
                        notes.pop(value)

            elif lst[position].startswith("contains="):
                xpos = int(lst[position + 1])
                ypos = int(lst[position + 2])
                for value in range(len(notes)):
                    if (xpos < notes[value].xposition and xpos > (notes[value].xposition + notes[value].height)) and \
                            (ypos < notes[value].yposition and ypos > (notes[value].yposition + notes[value].height)):
                        notes.pop(value)

            elif lst[position].startswith("PINS"):
                for value in range(len(notes)):
                    if notes[value].status == 0:
                        notes.pop(value)
        return notes

    def pin(self, pos):
        """
        -------------------------------------------------------
        Pins a note
        -------------------------------------------------------
        Parameters:
            pos - string of two numbers (string)
        Returns:
            None
        -------------------------------------------------------
        """
        positions = pos.split(",")
        xpos = int(positions[0])
        ypos = int(positions[1])

        for value in self._values:
            if (xpos >= value.xposition and xpos <= (value.xposition + value.height)) and \
                    (ypos >= value.yposition and ypos <= (value.yposition + value.height)):
                value.status += 1

        return


    def unpin(self, pos):
        """
        -------------------------------------------------------
        Unpins a note
        -------------------------------------------------------
        Parameters:
            pos - string of two numbers (string)
        Returns:
            None
        -------------------------------------------------------
        """
        positions = pos.split(",")
        xpos = int(positions[0])
        ypos = int(positions[1])

        for value in self._values:
            if (xpos >= value.xposition and xpos <= (value.xposition + value.height)) and \
                    (ypos >= value.yposition and ypos <= (value.yposition + value.height)) and value.status != 0:
                value.status -= 1

        return


    def clear(self):
        """
        -------------------------------------------------------
        forgets all notes that are not pinned
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        for i in range(len(self._values)):
            if self._values[i].status == 0:
                self._values.pop(i)

        return

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

#Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
serverPort = 4554

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
