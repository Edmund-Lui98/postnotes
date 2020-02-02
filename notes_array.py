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
            xpos = lst[position + 1]
            ypos = lst[position + 2]
            position += 3
            for value in self._values:
                if xpos < value.xposition <= (xpos + value.height) and ypos <= value.yposition <= (ypos + value.width):
                    notes.append(value)

        elif lst[position].startswith("PINS"):
            for value in self._values:
                if value.status > 0:
                    notes.append(value)
            position += 1
        #
        #
        # #second filter for the condition
        # if lst[position].startswith("color="):
        #     for value in range(len(notes)):
        #         if notes[value].color != lst[position][6:]:
        #             notes.pop(value)
        #
        # elif lst[position].startswith("refersTo="):
        #     for value in range(len(notes)):
        #         if lst[position][9:] not in notes[value].msg:
        #             notes.pop(value)
        #
        # elif lst[position].startswith("contains="):
        #     xpos = lst[position + 1]
        #     ypos = lst[position + 2]
        #     for value in range(len(notes)):
        #         if xpos >= notes[value].xposition > (xpos + notes[value].height) and ypos > \
        #                 notes[value].yposition > (ypos + notes[value].width):
        #             notes.pop(value)

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