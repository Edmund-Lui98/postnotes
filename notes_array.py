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
        msg1 = ""

        for i in range(5, len(lst)):
            msg1 += lst[i] + " "

        self._values.append(Note(msg1, status, xpos, ypos, width, height, color))

        return msg1

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

        for attribute in range(len(lst)):
            if lst[attribute].startswith("color="):
                for value in self._values:
                    if value.color == lst[6:]:
                        notes.append(value)

            if lst[attribute].startswith("refersTo="):
                for value in self._values:
                    if value._msg in attribute[9:]:
                        notes.append(value)

            if lst[attribute].startswith("contains="):
                xpos = lst[attribute + 1]
                ypos = lst[attribute + 2]
                attribute += 2
                for value in self._values:
                    if xpos < value._xposition <= (xpos + value._height) and ypos <= value._yposition <= (ypos + value._width):
                        notes.append(value)

            if lst[attribute].startswith("PINS"):
                for value in self._values:
                    if value._status > 0:
                        notes.append(value)

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
        xpos = positions[0]
        ypos = positions[1]

        for n in self._values:
            if xpos < n._xposition <= (xpos + n._height) and ypos <= n._yposition <= (ypos + n._width):
                n._status += 1

        return

        #chaimultetso
        #ta shi he

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
        xpos = positions[0]
        ypos = positions[1]

        for n in self._values:
            if xpos < n._xposition <= (xpos + n._height) and ypos <= n._yposition <= (ypos + n._width) and n._status != 0:
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