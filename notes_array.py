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

class notes:

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

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the stack is empty.
        Use: b = stack.is_empty()
        -------------------------------------------------------
        Returns:
            True if stack is empty, False otherwise
        -------------------------------------------------------
        """
        return len(self._values) == 0

    def post(self, value):
        """
        -------------------------------------------------------
        Put note in the server
        -------------------------------------------------------
        Parameters:
            value - object to be added to server (?)
        Returns:
            None
        -------------------------------------------------------
        """

        return

    def get(self):
        """
        -------------------------------------------------------
        Returns a copy of the value at the top of the stack.
        Attempting to peek at an empty stack throws an exception.
        Use: value = stack.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the top of stack (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty stack"

        value = deepcopy(self._values[-1])
        return value

    def pin(self):
        """
        -------------------------------------------------------
        Reverses the contents of the source stack.
        Use: stack.reverse()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """


    def unpin(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source stacks into the current target stack.
        When finished, the contents of source1 and source2 are
        interlaced into target and source1 and source2 are empty.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based stack (Stack)
            source2 - an array-based stack (Stack)
        Returns:
            None
        -------------------------------------------------------
        """


    def clear(self):
        """
        -------------------------------------------------------
        Splits the source stack into separate target stacks with values
        alternating into the targets. At finish source stack is empty.
        (iterative algorithm)
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Stack)
            target2 - contains other alternating values from source (Stack)
        -------------------------------------------------------
        """
