import pytest

from app.lexer.token import Token, TokenType, TokenizeResult, LexContext
from app.lexer import Lexer

@pytest.mark.parametrize('var, expected', [
    ('foo', TokenizeResult(3, Token(TokenType.IDENTIFIER, 'foo'))),
    ('foo_bar', TokenizeResult(7, Token(TokenType.IDENTIFIER, 'foo_bar'))),
    ('foo_12', TokenizeResult(6, Token(TokenType.IDENTIFIER, 'foo_12'))),
    ('_foo', TokenizeResult(4, Token(TokenType.IDENTIFIER, '_foo'))),
    ('__foo__', TokenizeResult(7, Token(TokenType.IDENTIFIER, '__foo__'))),
    ('1__foo__', TokenizeResult(0, None)),
    ('foo?', TokenizeResult(3, Token(TokenType.IDENTIFIER, 'foo'))),
])
def test_lex_identifier(var, expected):
    lexer = Lexer(var)
    result = lexer.lex_identifier()
    assert result == expected
    assert result.token == expected.token