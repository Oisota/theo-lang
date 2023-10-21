"""Functions for handling lexing"""

import re

from .token import TokenType, Token, TokenizeResult, LexContext

# generic lexing functions
def lex_char(type, value, ctx: LexContext) -> TokenizeResult:
    """Generic function for lexing a single character"""
    if value == ctx.current:
        return TokenizeResult(1, Token(type, value))
    return TokenizeResult(0, None)

def lex_pattern(type, pattern, ctx: LexContext) -> TokenizeResult:
    """Generic function for lexing a regexp pattern"""
    consumed_chars = 0
    value = ''
    char = ctx.current
    if pattern.match(char):
        while char and pattern.match(char):
            consumed_chars += 1
            value += char
            try:
                char = ctx.char_at_offset(consumed_chars)
            except IndexError:
                break

        return TokenizeResult(consumed_chars, Token(type, value))
    return TokenizeResult(0, None)

def lex_keyword(type, keyword, ctx: LexContext) -> TokenizeResult:
    """Generic function for lexing a keyword"""
    consumed_chars = 0
    while ctx.index + consumed_chars < len(ctx.data) and consumed_chars < len(keyword) and keyword[consumed_chars] == ctx.char_at_offset(consumed_chars):
        consumed_chars += 1

    if len(keyword) == consumed_chars:
        return TokenizeResult(consumed_chars, Token(type, keyword))
    return TokenizeResult(0, None)

def lex_line_comment(ctx: LexContext) -> TokenizeResult:
    """Lex a single line comment"""
    consumed = 2
    value = ''
    if ctx.current == '/' and ctx.char_at_offset(1) == '/':
        char = ctx.char_at_offset(consumed)
        while char != '\n':
            value += char
            consumed += 1
            char = ctx.char_at_offset(consumed)
        return TokenizeResult(consumed, None) # currently just ignoring comments
    return TokenizeResult(0, None)

def lex_multiline_comment(ctx: LexContext) -> TokenizeResult:
    """Lex a multiline comment"""
    consumed = 2
    value = ''
    if ctx.current == '/' and ctx.char_at_offset(1) == '*':
        char = ctx.char_at_offset(consumed)
        next_char = ctx.char_at_offset(consumed + 1)
        while not (char == '*' and next_char == '/'):
            value += char
            consumed += 1
            char = ctx.char_at_offset(consumed)
            next_char = ctx.char_at_offset(consumed + 1)
        consumed += 2
        return TokenizeResult(consumed, None) # currently just ignoring comments
    return TokenizeResult(0, None)

# concrete lexing functions
def lex_paren_open(ctx: LexContext) -> TokenizeResult:
    return lex_char(TokenType.PAREN_OPEN, '(', ctx)

def lex_paren_close(ctx: LexContext) -> TokenizeResult:
    return lex_char(TokenType.PAREN_CLOSE, ')', ctx)

def lex_curly_open(ctx: LexContext) -> TokenizeResult:
    return lex_char(TokenType.CURLY_OPEN, '{', ctx)

def lex_curly_close(ctx: LexContext) -> TokenizeResult:
    return lex_char(TokenType.CURLY_CLOSE, '}', ctx)

def lex_square_open(ctx: LexContext) -> TokenizeResult:
    return lex_char(TokenType.SQUARE_OPEN, '[', ctx)

def lex_square_close(ctx: LexContext) -> TokenizeResult:
    return lex_char(TokenType.SQUARE_CLOSE, ']', ctx)

def lex_colon(ctx: LexContext) -> TokenizeResult:
    return lex_char(TokenType.COLON, ':', ctx)

def lex_comma(ctx: LexContext) -> TokenizeResult:
    return lex_char(TokenType.COMMA, ',', ctx)

def lex_number(ctx: LexContext) -> TokenizeResult:
    pattern = re.compile('[0-9]|(\.)|(_)')
    end_pattern = re.compile('x|b|[A-F]|[a-f]|[0-9]|(\.)|(_)')
    #return lex_pattern(TokenType.NUMBER, pattern, input, current)
    consumed_chars = 0
    value = ''
    char = ctx.current
    if pattern.match(char):
        while char and end_pattern.match(char):
            consumed_chars += 1
            value += char
            try:
                char = ctx.char_at_offset(consumed_chars)
            except IndexError:
                break

        value = value.replace('_', '')
        # check if int or float literal
        token_type = TokenType.INTEGER
        if '.' in value:
            token_type = TokenType.FLOAT
        return TokenizeResult(consumed_chars, Token(token_type, value))
    return TokenizeResult(0, None)

def lex_identifier(ctx: LexContext) -> TokenizeResult:
    pattern = re.compile('([A-Z]|[a-z]|_|[0-9])+')
    initial_pattern = re.compile('([A-Z]|[a-z]|_)+')
    consumed_chars = 0
    value = ''
    char = ctx.current
    if initial_pattern.match(char):
        while char and pattern.match(char):
            consumed_chars += 1
            value += char
            try:
                char = ctx.char_at_offset(consumed_chars)
            except IndexError:
                break

        return TokenizeResult(consumed_chars, Token(TokenType.IDENTIFIER, value))
    return TokenizeResult(0, None)

def lex_skip_whitespace(ctx: LexContext) -> TokenizeResult:
    # NOTE this func and a few others may be the only ones that need to
    # count new lines, since only certain tokens may span a newline
    pattern = re.compile('\s')
    consumed = 0
    try:
        char = ctx.char_at_offset(consumed)
    except IndexError:
        return TokenizeResult(consumed, None)
    while pattern.match(char):
        consumed += 1
        try:
            char = ctx.char_at_offset(consumed)
        except IndexError:
            break
    return TokenizeResult(consumed, None)

def lex_string(ctx: LexContext) -> TokenizeResult:
    char = ctx.current
    if char == '"' or char == "'":
        value = ''
        consumed = 1
        closing_quote = char
        char = ctx.char_at_offset(consumed)
        while char != closing_quote:
            if char is None:
                raise Exception('unterminated string')
            value += char
            consumed += 1
            char = ctx.char_at_offset(consumed)

        return TokenizeResult(consumed + 1, Token(TokenType.STRING, value))
    return TokenizeResult(0, None)