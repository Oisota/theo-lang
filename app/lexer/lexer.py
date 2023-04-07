import re

from .keywords import KEYWORDS, OPERATORS
from .token import TokenType, Token, TokenizeResult

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
            try:
                char = input[current + consumed_chars]
            except IndexError:
                break

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
        while not (char == '*' and next_char == '/'):
            value += char
            consumed += 1
            char = input[current + consumed]
            next_char = input[current + consumed + 1]
        consumed += 2
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

def lex_square_open(input, current):
    return lex_char(TokenType.SQUARE_OPEN, '[', input, current)

def lex_square_close(input, current):
    return lex_char(TokenType.SQUARE_CLOSE, ']', input, current)

def lex_colon(input, current):
    return lex_char(TokenType.COLON, ':', input, current)

def lex_comma(input, current):
    return lex_char(TokenType.COMMA, ',', input, current)

def lex_number(input, current):
    pattern = re.compile('[0-9]|(\.)|(_)')
    end_pattern = re.compile('x|b|[A-F]|[a-f]|[0-9]|(\.)|(_)')
    #return lex_pattern(TokenType.NUMBER, pattern, input, current)
    consumed_chars = 0
    value = ''
    char = input[current]
    if pattern.match(char):
        while char and end_pattern.match(char):
            consumed_chars += 1
            value += char
            try:
                char = input[current + consumed_chars]
            except IndexError:
                break

        value = value.replace('_', '')
        # check if int or float literal
        token_type = TokenType.INTEGER
        if '.' in value:
            token_type = TokenType.FLOAT
        return TokenizeResult(consumed_chars, Token(token_type, value))
    return TokenizeResult(0, None)

def lex_identifier(input, current):
    pattern = re.compile('([A-Z]|[a-z]|_|[0-9])+')
    initial_pattern = re.compile('([A-Z]|[a-z]|_)+')
    consumed_chars = 0
    value = ''
    char = input[current]
    if initial_pattern.match(char):
        while char and pattern.match(char):
            consumed_chars += 1
            value += char
            try:
                char = input[current + consumed_chars]
            except IndexError:
                break

        return TokenizeResult(consumed_chars, Token(TokenType.IDENTIFIER, value))
    return TokenizeResult(0, None)

def lex_skip_whitespace(input, current):
    # NOTE this func and a few others may be the only ones that need to
    # count new lines, since only certain tokens may span a newline
    pattern = re.compile('\s')
    consumed = 0
    try:
        char = input[current + consumed]
    except IndexError:
        return TokenizeResult(consumed, None)
    while pattern.match(char):
        consumed += 1
        try:
            char = input[current + consumed]
        except IndexError:
            break
    return TokenizeResult(consumed, None)

def lex_string(input, current):
    char = input[current]
    if char == '"' or char == "'":
        value = ''
        consumed = 1
        closing_quote = char
        char = input[current + consumed]
        while char != closing_quote:
            if char is None:
                raise Exception('unterminated string')
            value += char
            consumed += 1
            char = input[current + consumed]

        return TokenizeResult(consumed + 1, Token(TokenType.STRING, value))
    return TokenizeResult(0, None)

def build_keyword_lambda(type, keyword):
    return lambda i, c: lex_keyword(type, keyword, i, c)

def build_string_tokenizers(strings, type):
    tokenizers = []

    for s in strings:
        fn = build_keyword_lambda(type, s) # needed to properly capture variables in loop
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
        lex_square_open,
        lex_square_close,
        lex_colon,
        lex_comma,
    ]
    tokenizers += build_string_tokenizers(KEYWORDS, TokenType.KEYWORD)
    tokenizers += build_string_tokenizers(OPERATORS, TokenType.OPERATOR)
    tokenizers += [
        lex_identifier,
        lex_number,
        lex_string,
    ]

    current = 0
    len_input = len(input)
    current_line = 1
    current_column = 1
    while current < len_input:
        tokenized = False
        for lex_function in tokenizers:
            token = None
            if tokenized:
                break
        
            result = lex_function(input, current)
            consumed_chars = result.consumed_chars
            token = result.token
            if token:
                token.start_line = current_line
                token.start_column = current_column

            #calculate consumed lines/columns
            for i in range(current, current + consumed_chars):
                current_column += 1
                if input[i] == '\n':
                    current_line += 1
                    current_column = 1

            if consumed_chars:
                current += consumed_chars
                tokenized = True


            if token:
                token.end_line = current_line
                token.end_column = current_column - 1
                print(token)
                yield token

        if not tokenized:
            raise Exception('Character not recognized: {}'.format(input[current]))