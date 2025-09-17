from unittest import TestCase

from app.lexer.token import Token, TokenType
from app.parser.parser import parse_imports, match
from app.parser.ast import Import

class TestParser(TestCase):

    def test_match(self):

        tests = [
            (
                'found match',
                Token(TokenType.KEYWORD, 'import'),
                Token(TokenType.KEYWORD, 'import'),
                True,
            ),
            (
                'no match, wrong text',
                Token(TokenType.KEYWORD, 'import'),
                Token(TokenType.KEYWORD, 'fun'),
                False,
            ),
            (
                'no match, wrong type',
                Token(TokenType.KEYWORD, 'import'),
                Token(TokenType.PAREN_OPEN, '('),
                False,
            ),
        ]

        for msg, t1, t2, consumed in tests:
            with self.subTest(msg=msg):
                result = match(t1, t2)
                self.assertEqual(result, consumed)

    def test_parse_imports(self):
        tokens = [
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
        ]

        expected = (
            [
            Import('std/common', ''),
            Import('std/io', ''),
            Import('std/math', '*'),
            Import('std/crypto', 'foo'),
            Import('cinclude/stdio', ''),
            Import('app/models', ''),
            Import('./util', ''),
            ],
            12
        )

        result = parse_imports(0, tokens)

        self.assertEqual(result, expected)
