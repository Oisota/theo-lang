"""Test comment lexing"""

from unittest import TestCase

from app.lexer.token import Token, TokenType, TokenizeResult
from app.lexer.lexer import lex_line_comment, lex_multiline_comment

class TestLexLineComment(TestCase):
    """Test lexing line comments"""
    def test_lex_line_comment(self):
        input = '//this is a comment\n'
        exp_result = TokenizeResult(19, None)

        result = lex_line_comment(input, 0)

        self.assertEqual(result, exp_result)

class TestLexMultilineComment(TestCase):
    """Test lexing multiline comments"""
    def test_lex_multiline_comment(self):
        input = '/*\nthis is a multi* \nline comment\nfoobar bat\n*/\n'
        exp_result = TokenizeResult(47, None)

        result = lex_multiline_comment(input, 0)

        self.assertEqual(result, exp_result)