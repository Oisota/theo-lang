from unittest import TestCase

from app.lexer.token import Token, TokenType, TokenizeResult, LexContext
from app.lexer.lex_funcs import lex_char

class TestLexChar(TestCase):

    def test_lex_char(self):

        tests = [
            ('{', TokenizeResult(1, Token(TokenType.CURLY_OPEN, '{'))),
            ('}', TokenizeResult(1, Token(TokenType.CURLY_CLOSE, '}'))),
        ]

        for char, expected in tests:
            with self.subTest(char=char):
                ctx = LexContext(char, 0)
                result = lex_char(expected.token.type, char, ctx)
                self.assertEqual(result, expected)
                self.assertEqual(result.token, expected.token)