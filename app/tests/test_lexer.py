from unittest import TestCase

from ..lexer import *

class TestLexWhiteSpace(TestCase):

    def test_all_white_space(self):
        input = "   \n \t \r\n"
        len_input = len(input)

        result = lex_skip_whitespace(input, 0)

        self.assertEqual(result.consumed_chars, len_input)
        self.assertEqual(result.token, None)

    def test_non_white_space(self):
        input = "Here_is_some_non_white_space"

        result = lex_skip_whitespace(input, 0)

        self.assertEqual(result.consumed_chars, 0)
        self.assertEqual(result.token, None)

    def test_initial_white_space(self):
        input = "    Initial_White_Space"

        result = lex_skip_whitespace(input, 0)

        self.assertEqual(result.consumed_chars, 4)
        self.assertEqual(result.token, None)

    def test_trailing_white_space(self):
        input = "Initial_White_Space    "

        result = lex_skip_whitespace(input, 0)

        self.assertEqual(result.consumed_chars, 0)
        self.assertEqual(result.token, None)

class TestLexNumber(TestCase):
    """Test number literal lexing"""
    def test_lex_integer(self):
        input = '1234'
        token = Token(TokenType.INTEGER, '1234')
        exp_result = TokenizeResult(4, token)
        
        result = lex_number(input, 0)

        self.assertEqual(result.consumed_chars, 4)
        self.assertEqual(result, exp_result)
        self.assertEqual(result.token, token)

    def test_lex_float(self):
        input = '12.34'
        token = Token(TokenType.FLOAT, '12.34')
        exp_result = TokenizeResult(5, token)
        
        result = lex_number(input, 0)

        self.assertEqual(result.consumed_chars, 5)
        self.assertEqual(result, exp_result)
        self.assertEqual(result.token, token)

    def test_lex_int_underscore(self):
        input = '10_000'
        token = Token(TokenType.INTEGER, '10000')
        exp_result = TokenizeResult(6, token)
        
        result = lex_number(input, 0)

        self.assertEqual(result.consumed_chars, 6)
        self.assertEqual(result, exp_result)
        self.assertEqual(result.token, token)

    def test_lex_float_underscore(self):
        input = '10_000.00'
        token = Token(TokenType.FLOAT, '10000.00')
        exp_result = TokenizeResult(9, token)
        
        result = lex_number(input, 0)

        self.assertEqual(result.consumed_chars, 9)
        self.assertEqual(result, exp_result)
        self.assertEqual(result.token, token)

class TestLexIdentifier(TestCase):
    """Test lexing identifiers"""
    def test_lex_identifier(self):
        input = 'foo'
        token = Token(TokenType.IDENTIFIER, 'foo')
        exp_result = TokenizeResult(3, token)

        result = lex_identifier(input, 0)

        self.assertEqual(result, exp_result)
        self.assertEqual(result.token, token)

    def test_lex_identifier_underscore(self):
        input = 'foo_bar'
        token = Token(TokenType.IDENTIFIER, 'foo_bar')
        exp_result = TokenizeResult(7, token)

        result = lex_identifier(input, 0)

        self.assertEqual(result, exp_result)
        self.assertEqual(result.token, token)

    def test_lex_identifier_number(self):
        input = 'foo_12'
        token = Token(TokenType.IDENTIFIER, 'foo_12')
        exp_result = TokenizeResult(6, token)

        result = lex_identifier(input, 0)

        self.assertEqual(result, exp_result)
        self.assertEqual(result.token, token)

    def test_lex_identifier_leading_underscore(self):
        input = '_foo'
        token = Token(TokenType.IDENTIFIER, '_foo')
        exp_result = TokenizeResult(4, token)

        result = lex_identifier(input, 0)

        self.assertEqual(result, exp_result)
        self.assertEqual(result.token, token)

class TestLexString(TestCase):

    def test_lex_string_double_quotes(self):

        input = '"Here is a test string"'
        token = Token(TokenType.STRING, 'Here is a test string')
        exp_result = TokenizeResult(len(input), token)

        result = lex_string(input, 0)

        self.assertEqual(result, exp_result)
        self.assertEqual(result.token, token)

    def test_lex_string_single_quotes(self):

        input = "'Here is a test string'"
        token = Token(TokenType.STRING, 'Here is a test string')
        exp_result = TokenizeResult(len(input), token)

        result = lex_string(input, 0)

        self.assertEqual(result, exp_result)
        self.assertEqual(result.token, token)