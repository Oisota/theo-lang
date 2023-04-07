from unittest import TestCase

from app.lexer.token import Token, TokenType, TokenizeResult
from app.lexer.lexer import lex_string

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