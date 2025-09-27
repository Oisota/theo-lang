class Processor:
    """Base class for lexer/parser

    Just implements some common functionality
    """
    def __init__(self, data: list):
        self.data = data
        self.index = 0

    @property
    def current(self):
        return self.data[self.index]

    def next(self):
        self.index += 1
