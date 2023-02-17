class Reader:
    """Class to track lexer position in a file"""
    def __init__(self, file):
        self.current = 0
        self.file = file
        # TODO maybe have this class keep track of current line?
        # Maybe make the lexer functions not have to calculate lines themselves?

    def next(self):
        """Return next char and increment position"""
        char = self.file.read(1)
        self.current += 1
        return char

    def peek(self):
        """Return next char and leave current position as is"""
        char = self.file.read(1)
        self.file.seek(self.current)
        return char
