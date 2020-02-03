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