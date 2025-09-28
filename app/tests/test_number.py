import pytest

from app.token import Token, TokenType, TokenizeResult
from app.lexer import Lexer

@pytest.mark.parametrize('num, expected', [
    ('1234', TokenizeResult(4, Token(TokenType.INTEGER, '1234'))),
    ('0x1546BEEF', TokenizeResult(10, Token(TokenType.INTEGER, '0x1546BEEF'))),
    ('0b01101001', TokenizeResult(10, Token(TokenType.INTEGER, '0b01101001'))),
    ('12.34', TokenizeResult(5, Token(TokenType.FLOAT, '12.34'))),
    ('10_000', TokenizeResult(6, Token(TokenType.INTEGER, '10000'))),
    ('10_000.00', TokenizeResult(9, Token(TokenType.FLOAT, '10000.00'))),
])
def test_lex_number(num, expected):
    """Test number literal lexing"""
    lexer = Lexer(num)
    result = lexer.lex_number()
    assert result.consumed_chars == expected.consumed_chars
    assert result == expected
    assert result.token == expected.token