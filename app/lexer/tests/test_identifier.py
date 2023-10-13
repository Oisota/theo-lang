from unittest import TestCase

from app.lexer.token import Token, TokenType, TokenizeResult, LexContext
from app.lexer.lex_funcs import lex_identifier

class TestLexIdentifier(TestCase):
    """Test lexing identifiers"""
    def test_lex_identifier(self):
        input = 'foo'
        token = Token(TokenType.IDENTIFIER, 'foo')
        exp_result = TokenizeResult(3, token)
        ctx = LexContext(input, 0)

        result = lex_identifier(ctx)

        self.assertEqual(result, exp_result)
        self.assertEqual(result.token, token)

    def test_lex_identifier_underscore(self):
        input = 'foo_bar'
        token = Token(TokenType.IDENTIFIER, 'foo_bar')
        exp_result = TokenizeResult(7, token)
        ctx = LexContext(input, 0)

        result = lex_identifier(ctx)

        self.assertEqual(result, exp_result)
        self.assertEqual(result.token, token)

    def test_lex_identifier_number(self):
        input = 'foo_12'
        token = Token(TokenType.IDENTIFIER, 'foo_12')
        exp_result = TokenizeResult(6, token)
        ctx = LexContext(input, 0)

        result = lex_identifier(ctx)

        self.assertEqual(result, exp_result)
        self.assertEqual(result.token, token)

    def test_lex_identifier_leading_underscore(self):
        input = '_foo'
        token = Token(TokenType.IDENTIFIER, '_foo')
        exp_result = TokenizeResult(4, token)
        ctx = LexContext(input, 0)

        result = lex_identifier(ctx)

        self.assertEqual(result, exp_result)
        self.assertEqual(result.token, token)