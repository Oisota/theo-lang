import pytest

from app.token import Token, TokenType, TokenizeResult, LexContext
from app.lexer import Lexer


@pytest.mark.parametrize('char, expected', [
    ('{', TokenizeResult(1, Token(TokenType.CURLY_OPEN, '{'))),
    ('}', TokenizeResult(1, Token(TokenType.CURLY_CLOSE, '}'))),
])
def test_lex_char(char, expected):
    lexer = Lexer(char)
    result = lexer.lex_char(expected.token.type, char)
    assert result == expected
    assert result.token == expected.token