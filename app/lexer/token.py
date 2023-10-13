"""Token Data Structures"""

from enum import Enum, auto
from dataclasses import dataclass

class TokenType(Enum):
    PAREN_OPEN = auto()
    PAREN_CLOSE = auto()
    CURLY_OPEN = auto()
    CURLY_CLOSE = auto()
    SQUARE_OPEN = auto()
    SQUARE_CLOSE = auto()
    COLON = auto()
    COMMA = auto()
    KEYWORD = auto()
    INTEGER = auto()
    FLOAT = auto()
    STRING = auto()
    OPERATOR = auto()
    IDENTIFIER = auto()
    COMMENT = auto()
    RESERVED = auto()

@dataclass
class Token:
    type: TokenType
    value: str
    start_line: int = 0
    end_line: int = 0
    start_column: int = 0
    end_column: int = 0

    def __repr__(self):
        return "Token({}, '{}', line: {}-{}, column: {}-{})".format(self.type.name, self.value, self.start_line, self.end_line, self.start_column, self.end_column)

@dataclass
class TokenizeResult:
    consumed_chars: int
    token: Token

@dataclass
class LexContext:
    data: list[str]
    index: int

    @property
    def current(self):
        return self.data[self.index]

    def char_at_offset(self, offset: int):
        return self.data[self.index + offset]