from unittest import TestCase

from app.lexer.token import Token, TokenType, TokenizeResult, LexContext
from app.lexer import Lexer

class TestLexChar(TestCase):

    def test_lex_char(self):

        tests = [
            ('{', TokenizeResult(1, Token(TokenType.CURLY_OPEN, '{'))),
            ('}', TokenizeResult(1, Token(TokenType.CURLY_CLOSE, '}'))),
        ]

        for char, expected in tests:
            with self.subTest(char=char):
                lexer = Lexer(char)
                result = lexer.lex_char(expected.token.type, char)
                self.assertEqual(result, expected)
                self.assertEqual(result.token, expected.token)