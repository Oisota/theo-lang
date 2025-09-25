import pytest

from app.lexer.token import Token, TokenType
from app.parser.parser import Parser
from app.parser.ast import Import

@pytest.mark.parametrize('t1, t2, consumed', [
    pytest.param(
        Token(TokenType.KEYWORD, 'import'),
        Token(TokenType.KEYWORD, 'import'),
        1,
        id='found match',
    ),
    pytest.param(
        Token(TokenType.KEYWORD, 'import'),
        Token(TokenType.KEYWORD, 'fun'),
        0,
        id='no match, wrong text',
    ),
    pytest.param(
        Token(TokenType.KEYWORD, 'import'),
        Token(TokenType.PAREN_OPEN, '('),
        0,
        id='no match, wrong type',
    ),
])
def test_match(t1, t2, consumed):
    p = Parser([t2])
    p.match(t1)
    assert consumed == p.consumed

def test_next():
    p = Parser([])
    assert p.consumed == 0
    p.next()
    assert p.consumed == 1

@pytest.mark.parametrize('tokens, imports, consumed', [
    pytest.param(
        [
            Token(TokenType.KEYWORD, 'import', 5, 5, 1, 6),
            Token(TokenType.PAREN_OPEN, '(', 5, 5, 8, 8),
            Token(TokenType.STRING, 'std/common', 6, 6, 2, 13),
            Token(TokenType.STRING, 'std/io', 7, 7, 2, 9),
            Token(TokenType.STRING, 'std/math', 8, 8, 2, 11),
            Token(TokenType.OPERATOR, '*', 8, 8, 13, 13),
            Token(TokenType.STRING, 'std/crypto', 9, 9, 2, 13),
            Token(TokenType.IDENTIFIER, 'foo', 9, 9, 15, 17),
            Token(TokenType.STRING, 'cinclude/stdio', 10, 10, 2, 17),
            Token(TokenType.STRING, 'app/models', 11, 11, 2, 13),
            Token(TokenType.STRING, './util', 12, 12, 2, 9),
            Token(TokenType.PAREN_CLOSE, ')', 13, 13, 1, 1),
        ],
        [
            Import('std/common', ''),
            Import('std/io', ''),
            Import('std/math', '*'),
            Import('std/crypto', 'foo'),
            Import('cinclude/stdio', ''),
            Import('app/models', ''),
            Import('./util', ''),
        ],
        12,
        id='kitchen sink example',
    ),
    pytest.param(
        [
            Token(TokenType.KEYWORD, 'import', 5, 5, 1, 6),
            Token(TokenType.PAREN_OPEN, '(', 5, 5, 8, 8),
            Token(TokenType.PAREN_CLOSE, ')', 13, 13, 1, 1),
        ],
        [],
        3,
        id='empty imports',
    ),
    pytest.param(
        [
            Token(TokenType.KEYWORD, 'import', 5, 5, 1, 6),
            Token(TokenType.PAREN_OPEN, '(', 5, 5, 8, 8),
            Token(TokenType.KEYWORD, 'import', 5, 5, 1, 6),
            Token(TokenType.IDENTIFIER, 'foo', 5, 5, 1, 6),
            Token(TokenType.PAREN_CLOSE, ')', 13, 13, 1, 1),
        ],
        [],
        2,
        id='invalid imports',
    ),
])
def test_parse_imports(tokens, imports, consumed):
    p = Parser(tokens)
    result = p.parse_imports()
    assert result == imports
    assert consumed == p.consumed
