"""Test comment lexing"""

from unittest import TestCase

from app.lexer.token import TokenizeResult, LexContext
from app.lexer.core import lex_line_comment, lex_multiline_comment

class TestLexComment(TestCase):
    """Test lexing line comments"""
    def test_lex_line_comment(self):
        tests = [
            ('//this is a comment\n', TokenizeResult(19, None), lex_line_comment),
            ('/*\nthis is a multi* \nline comment\nfoobar bat\n*/\n', TokenizeResult(47, None), lex_multiline_comment),
        ]

        for text, expected, func in tests:
            with self.subTest(func=func):
                ctx = LexContext(text, 0)
                result = func(ctx)
                self.assertEqual(result, expected)