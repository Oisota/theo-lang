from unittest import TestCase

from app.lexer.token import Token, TokenType, TokenizeResult, LexContext
from app.lexer.lex_funcs import lex_number

class TestLexNumber(TestCase):
    """Test number literal lexing"""
    def test_lex_numbers(self):
        input = '1234'
        tests = [
            ('1234', TokenizeResult(4, Token(TokenType.INTEGER, '1234'))),
            ('0x1546BEEF', TokenizeResult(10, Token(TokenType.INTEGER, '0x1546BEEF'))),
            ('0b01101001', TokenizeResult(10, Token(TokenType.INTEGER, '0b01101001'))),
            ('12.34', TokenizeResult(5, Token(TokenType.FLOAT, '12.34'))),
            ('10_000', TokenizeResult(6, Token(TokenType.INTEGER, '10000'))),
            ('10_000.00', TokenizeResult(9, Token(TokenType.FLOAT, '10000.00'))),
        ]

        for (num, expected) in tests:
            with self.subTest(num=num):
                ctx = LexContext(num, 0)
                result = lex_number(ctx)
                self.assertEqual(result.consumed_chars, expected.consumed_chars)
                self.assertEqual(result, expected)
                self.assertEqual(result.token, expected.token)