"""Test comment lexing"""

import pytest

from app.lexer.token import TokenizeResult, LexContext
from app.lexer import Lexer

@pytest.mark.parametrize('text, expected, func', [
    ('//this is a comment\n', TokenizeResult(19, None), 'lex_line_comment'),
    ('/*\nthis is a multi* \nline comment\nfoobar bat\n*/\n', TokenizeResult(47, None), 'lex_multiline_comment'),
])
def test_lex_line_comment(text, expected, func):
    lexer = Lexer(text)
    result = getattr(lexer, func)()
    assert result == expected