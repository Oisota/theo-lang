import pytest

from app.lexer.token import Token, TokenType, TokenizeResult, LexContext
from app.lexer import Lexer

@pytest.mark.parametrize('text, expected', [
    ('"Here is a test string"', TokenizeResult(23, Token(TokenType.STRING, 'Here is a test string'))),
    ("'Here is a test string'", TokenizeResult(23, Token(TokenType.STRING, 'Here is a test string'))),
])
def test_lex_string_double_quotes(text, expected):
    lexer = Lexer(text)
    result = lexer.lex_string()
    assert result == expected
    assert result.token == expected.token