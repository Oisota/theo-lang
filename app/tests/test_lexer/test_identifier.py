from unittest import TestCase

from app.lexer import Token, TokenType, TokenizeResult, lex_identifier

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