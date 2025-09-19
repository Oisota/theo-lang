"""Test comment lexing"""

from unittest import TestCase

from app.lexer.token import TokenizeResult, LexContext
from app.lexer import Lexer

class TestLexComment(TestCase):
    """Test lexing line comments"""
    def test_lex_line_comment(self):
        tests = [
            ('//this is a comment\n', TokenizeResult(19, None), 'lex_line_comment'),
            ('/*\nthis is a multi* \nline comment\nfoobar bat\n*/\n', TokenizeResult(47, None), 'lex_multiline_comment'),
        ]

        for text, expected, func in tests:
            with self.subTest(func=func):
                lexer = Lexer(text)
                result = getattr(lexer, func)()
                self.assertEqual(result, expected)