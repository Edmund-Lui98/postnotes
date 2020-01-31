"""
-------------------------------------------------------
Array of note objects
-------------------------------------------------------
Author:  Edmund Lui
ID:      160635540
Email:   luix5540@gmail.com
Section: CP372
-------------------------------------------------------
"""
from copy import deepcopy
from note import Note

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

        for i in range(5, len(lst)):
            msg += msg[i]
            msg += " "

        self._values.append(Note(msg, status, xpos, ypos, width, height, color))

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
        if len(condition) == 0:
            return notes
        else:
            return


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
        xpos = positions[0]
        ypos = positions[1]

        for n in self._values:
            if n._xposition == xpos and n._yposition == ypos:
                n._status += 1

        return


    def unpin(self, source1, source2):
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
        xpos = positions[0]
        ypos = positions[1]

        for n in self._values:
            if n._xposition == xpos and n._yposition == ypos and n._status != 0:
                n._status -= 1

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
            if self._values[i]._status == 0:
                self._values.pop(i)

        return