"""Test comment lexing"""

from unittest import TestCase

from app.lexer.token import TokenizeResult, LexContext
from app.lexer.core import lex_line_comment, lex_multiline_comment

class TestLexLineComment(TestCase):
    """Test lexing line comments"""
    def test_lex_line_comment(self):
        input = '//this is a comment\n'
        exp_result = TokenizeResult(19, None)
        ctx = LexContext(input, 0)

        result = lex_line_comment(ctx)

        self.assertEqual(result, exp_result)

class TestLexMultilineComment(TestCase):
    """Test lexing multiline comments"""
    def test_lex_multiline_comment(self):
        input = '/*\nthis is a multi* \nline comment\nfoobar bat\n*/\n'
        exp_result = TokenizeResult(47, None)
        ctx = LexContext(input, 0)

        result = lex_multiline_comment(ctx)

        self.assertEqual(result, exp_result)