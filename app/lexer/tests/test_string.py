from unittest import TestCase

from app.lexer.token import Token, TokenType, TokenizeResult, LexContext
from app.lexer import Lexer

class TestLexString(TestCase):

    def test_lex_string_double_quotes(self):

        tests = [
            ('"Here is a test string"', TokenizeResult(23, Token(TokenType.STRING, 'Here is a test string'))),
            ("'Here is a test string'", TokenizeResult(23, Token(TokenType.STRING, 'Here is a test string'))),
        ]

        for text, expected in tests:
            with self.subTest(text=text):
                lexer = Lexer(text)
                result = lexer.lex_string()
                self.assertEqual(result, expected)
                self.assertEqual(result.token, expected.token)