import re
from enum import Enum, auto
from dataclasses import dataclass
from collections import namedtuple

class TokenType(Enum):
    VAR_NAME = auto()
    PAREN_OPEN = auto()
    PAREN_CLOSE = auto()
    CURLY_OPEN = auto()
    CURLY_CLOSE = auto()
    COLON = auto()
    COMMA = auto()
    KEYWORD = auto()
    NUMBER = auto()
    STRING = auto()
    OPERATOR = auto()
    IDENTIFIER = auto()
    COMMENT = auto()

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

def lex_line_comment(input, current):
    """Lex a single line comment"""
    consumed = 2
    value = ''
    if input[current] == '/' and input[current + 1] == '/':
        char = input[current + consumed]
        while char != '\n':
            value += char
            consumed += 1
            char = input[current + consumed]
        return TokenizeResult(consumed, None) # currently just ignoring comments
    return TokenizeResult(0, None)

def lex_multiline_comment(input, current):
    """Lex a multiline comment"""
    consumed = 2
    value = ''
    if input[current] == '/' and input[current + 1] == '*':
        char = input[current + consumed]
        next_char = input[current + consumed + 1]
        while char != '*' and next_char != '/':
            value += char
            consumed += 1
            char = input[current + consumed]
            next_char = input[current + consumed + 1]
        return TokenizeResult(consumed, None) # currently just ignoring comments
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

def lex_string(input, current):
    if input[current] == '"':
        value = ''
        consumed = 1
        char = input[current + consumed]
        while char != '"':
            if char is None:
                raise Exception('unterminated string')
            value += char
            consumed += 1
            char = input[current + consumed]

        return TokenizeResult(consumed + 1, Token(TokenType.STRING, value))
    return TokenizeResult(0, None)

def build_keyword_lambda(token_type, keyword):
    return lambda i, c: lex_keyword(token_type, keyword, i, c)

def build_string_tokenizers(strings, token_type):
    tokenizers = []

    for s in strings:
        fn = build_keyword_lambda(token_type, s) # needed to properly capture variables in loop
        tokenizers.append(fn)

    return tokenizers

def tokenize(input):
    """Read file and parse contents into token array"""
    # TODO
    # - add newline token? (maybe needed to denote end of expression)
    tokenizers = [
        lex_skip_whitespace,
        lex_line_comment,
        lex_multiline_comment,
        lex_paren_open,
        lex_paren_close,
        lex_curly_open,
        lex_curly_close,
        lex_colon,
        lex_comma,
    ]
    # match keywords before indentifiers
    keywords = ['fun', 'if', 'else', 'case', 'struct', 'interface', 'type', 'impl', 'enum', 'let', 'while', 'for', 'import', 'scope']
    tokenizers += build_string_tokenizers(keywords, TokenType.KEYWORD)
    operators = [
        'and',
        'or',
        'not',
        '=>',
        '+=',
        '-=',
        '*=',
        '/='
        '==',
        '!=',
        '<=',
        '>=',
        '+',
        '-',
        '*',
        '/',
        '=',
        '.',
        '<',
        '>',
        ]
    tokenizers += build_string_tokenizers(operators, TokenType.OPERATOR)
    tokenizers += [
        lex_identifier,
        lex_number,
        lex_string,
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