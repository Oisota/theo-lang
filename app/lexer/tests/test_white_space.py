import pytest

from app.lexer import Lexer

@pytest.mark.parametrize('text, expected', [
    ("   \n \t \r\n", 9),
    ("Here_is_some_non_white_space", 0),
    ("    Initial_White_Space", 4),
    ("Trailing_White_Space    ", 0),
])
def test_all_white_space(text, expected):
    lexer = Lexer(text)
    result = lexer.lex_skip_whitespace()
    assert result.consumed_chars == expected
    assert result.token == None