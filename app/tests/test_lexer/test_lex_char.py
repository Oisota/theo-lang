from unittest import TestCase

from app.lexer import Token, TokenType, TokenizeResult, lex_char

class TestLexString(TestCase):

    def test_lex_string_double_quotes(self):

        input = '{'
        token = Token(TokenType.CURLY_OPEN, '{')
        exp_result = TokenizeResult(len(input), token)

        result = lex_char(TokenType.CURLY_OPEN, '{', input, 0)

        self.assertEqual(result, exp_result)
        self.assertEqual(result.token, token)