"""Pregenerated token classes

Pre-generate token instances for keywords/operates/syntax for easier
reference in lexing/parsing code. For Ex: Keywords.IMPORT vs having
to construct Token(TokenType.KEYWORD, 'import')
"""

from .keywords import KEYWORDS, RESERVED_WORDS, OPERATORS
from .token import Token, TokenType

def set_tokens(cls):
    """Set static token instances on a class"""
    for t in cls.token_list:
        token = Token(cls.token_type, t)
        setattr(cls, t.upper(), token)

class Keywords:
    """Pregenerated keyword tokens"""
    token_list = KEYWORDS
    token_type = TokenType.KEYWORD

set_tokens(Keywords)


class Reserved:
    """Pregenerated reserved word tokens"""
    token_list = RESERVED_WORDS
    token_type = TokenType.RESERVED

set_tokens(Reserved)


class Syntax:
    """Pregenerated syntax tokens"""
    PAREN_OPEN = Token(TokenType.PAREN_OPEN, '(')
    PAREN_CLOSE = Token(TokenType.PAREN_CLOSE, ')')
    CURLY_OPEN = Token(TokenType.CURLY_OPEN, '{')
    CURLY_CLOSE = Token(TokenType.CURLY_CLOSE, '}')
    SQUARE_OPEN = Token(TokenType.SQUARE_OPEN, '[')
    SQUARE_CLOSE = Token(TokenType.SQUARE_CLOSE, ']')

class Operators:
    """Pregenerated operator tokens"""
    AND = Token(TokenType.OPERATOR, 'and')
    OR = Token(TokenType.OPERATOR, 'or')
    NOT = Token(TokenType.OPERATOR, 'not')
    EQ = Token(TokenType.OPERATOR, '==')
    NE = Token(TokenType.OPERATOR, '!=')
    LTE = Token(TokenType.OPERATOR, '<=')
    GTE = Token(TokenType.OPERATOR, '>=')
    LT = Token(TokenType.OPERATOR, '<')
    GT = Token(TokenType.OPERATOR, '>')
    MATCH = Token(TokenType.OPERATOR, '=>')
    PLUS = Token(TokenType.OPERATOR, '+')
    MINUS = Token(TokenType.OPERATOR, '-')
    MULT = Token(TokenType.OPERATOR, '*')
    DIV = Token(TokenType.OPERATOR, '/')
    MOD = Token(TokenType.OPERATOR, '%')
    BW_AND = Token(TokenType.OPERATOR, '&')
    BW_OR = Token(TokenType.OPERATOR, '|')
    BW_XOR = Token(TokenType.OPERATOR, '^')
    BW_RSHIFT = Token(TokenType.OPERATOR, '>>')
    BW_LSHIFT = Token(TokenType.OPERATOR, '<<')
    BW_NEGATE = Token(TokenType.OPERATOR, '~')
    ASSIGN = Token(TokenType.OPERATOR, '=')
    DOT = Token(TokenType.OPERATOR, '.')
    TYPE_ANNOTATE = Token(TokenType.OPERATOR, ':')
