from unittest import TestCase

from app.lexer import Token, TokenType, TokenizeResult, lex_number

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

    def test_lex_hex_integer(self):
        input = '0x1546BEEF'
        token = Token(TokenType.INTEGER, '0x1546BEEF')
        exp_result = TokenizeResult(10, token)
        
        result = lex_number(input, 0)

        self.assertEqual(result.consumed_chars, 10)
        self.assertEqual(result, exp_result)
        self.assertEqual(result.token, token)

    def test_lex_binary_integer(self):
        input = '0b01101001'
        token = Token(TokenType.INTEGER, '0b01101001')
        exp_result = TokenizeResult(10, token)
        
        result = lex_number(input, 0)

        self.assertEqual(result.consumed_chars, 10)
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