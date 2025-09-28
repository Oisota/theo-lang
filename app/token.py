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

    def matches(self, other):
        """Check if another token matches this one"""
        return (
            (other.type == self.type) and
            (other.value == self.value)
        )

    def __repr__(self):
        return (
            "Token({}, '{}', line: {}-{}, column: {}-{})".format(
                self.type.name,
                self.value,
                self.start_line,
                self.end_line,
                self.start_column,
                self.end_column
            )
        )

@dataclass
class TokenizeResult:
    consumed_chars: int
    token: Token

    def __repr__(self):
        return f'TokenizeResult({self.consumed_chars}, {self.token})'