import re
from enum import Enum, auto
from dataclasses import dataclass
from collections import namedtuple

class TokenType(Enum):
    WHITE_SPACE = auto()
    VAR_NAME = auto()
    PAREN_OPEN = auto()
    PAREN_CLOSE = auto()
    CURLY_OPEN = auto()
    CURLY_CLOSE = auto()
    COLON = auto()
    COMMA = auto()
    KEYWORD = auto()
    NUMBER = auto()
    OPERATOR = auto()
    IDENTIFIER = auto()

@dataclass
class Token:
    token_type: TokenType
    value: str

    def __repr__(self):
        return "Token({}, '{}')".format(self.token_type.name, self.value)

@dataclass
class TokenizeResult:
    consumed_chars: int
    token: Token

# generic lexing functions
def lex_char(type, value, input, current):
    """Generic function for lexing a single character"""
    if value == input[current]:
        return TokenizeResult(1, Token(type, value))
    return TokenizeResult(0, None)

def lex_pattern(type, pattern, input, current):
    """Generic function for lexing a regexp pattern"""
    # TODO need to debug this, not working quite right
    consumed_chars = 0
    value = ''
    char = input[current]
    if pattern.match(char):
        while char and pattern.match(char):
            consumed_chars += 1
            value += char
            char = input[current + consumed_chars]

        return TokenizeResult(consumed_chars, Token(type, value))
    return TokenizeResult(0, None)

def lex_keyword(type, keyword, input, current):
    """Generic function for lexing a keyword"""
    consumed_chars = 0
    while current + consumed_chars < len(input) and consumed_chars < len(keyword) and keyword[consumed_chars] == input[current + consumed_chars]:
        consumed_chars += 1

    if len(keyword) == consumed_chars:
        return TokenizeResult(consumed_chars, Token(type, keyword))
    return TokenizeResult(0, None)

# concrete lexing functions
def lex_paren_open(input, current):
    return lex_char(TokenType.PAREN_OPEN, '(', input, current)

def lex_paren_close(input, current):
    return lex_char(TokenType.PAREN_CLOSE, ')', input, current)

def lex_curly_open(input, current):
    return lex_char(TokenType.CURLY_OPEN, '{', input, current)

def lex_curly_close(input, current):
    return lex_char(TokenType.CURLY_CLOSE, '}', input, current)

def lex_colon(input, current):
    return lex_char(TokenType.COLON, ':', input, current)

def lex_comma(input, current):
    return lex_char(TokenType.COMMA, ',', input, current)

def lex_number(input, current):
    pattern = re.compile('[0-9]')
    return lex_pattern(TokenType.NUMBER, pattern, input, current)

def lex_identifier(input, current):
    pattern = re.compile('^[^\d\W]\w*\Z')
    return lex_pattern(TokenType.IDENTIFIER, pattern, input, current)

def lex_skip_whitespace(input, current):
    pattern = re.compile('\s')
    if pattern.match(input[current]):
        return TokenizeResult(1, None)
    return TokenizeResult(0, None)

def build_keyword_lambda(token_type, keyword):
    return lambda i, c: lex_keyword(token_type, keyword, i, c)

def tokenize(input):
    """Read file and parse contents into token array"""
    tokenizers = [
        lex_skip_whitespace,
        lex_paren_open,
        lex_paren_close,
        lex_curly_open,
        lex_curly_close,
        lex_colon,
        lex_comma,
    ]
    # match keywords before indentifiers
    keywords = ['fun', 'if', 'else', 'struct', 'interface', 'let', 'while', 'for', 'import']
    for kw in keywords:
        fn = build_keyword_lambda(TokenType.KEYWORD, kw) # needed to properly capture variables in loop
        tokenizers.append(fn)
    operators = ['and', 'or', '+', '-', '*', '/', '=']
    for op in operators:
        fn = build_keyword_lambda(TokenType.OPERATOR, op) # needed to properly capture variables in loop
        tokenizers.append(fn)
    tokenizers += [
        lex_identifier,
        lex_number,
    ]

    tokens = []

    current = 0
    while current < len(input):
        tokenized = False
        for tokenizer in tokenizers:
            token = None
            if tokenized:
                break
        
            result = tokenizer(input, current)
            consumed_chars = result.consumed_chars
            token = result.token

            if consumed_chars != 0:
                tokenized = True
                current += consumed_chars

            if token:
                tokens.append(token)
        
        if not tokenized:
            raise Exception('Character not recognized: {}'.format(input[current]))

    return tokens