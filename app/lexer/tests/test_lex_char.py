from unittest import TestCase

from app.lexer.token import Token, TokenType, TokenizeResult, LexContext
from app.lexer.lex_funcs import lex_char

class TestLexString(TestCase):

    def test_lex_string_double_quotes(self):

        input = '{'
        token = Token(TokenType.CURLY_OPEN, '{')
        exp_result = TokenizeResult(len(input), token)
        ctx = LexContext(input, 0)

        result = lex_char(TokenType.CURLY_OPEN, '{', ctx)

        self.assertEqual(result, exp_result)
        self.assertEqual(result.token, token)