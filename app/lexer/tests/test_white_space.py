from unittest import TestCase

from app.lexer.lex_funcs import lex_skip_whitespace
from app.lexer.token import LexContext

class TestLexWhiteSpace(TestCase):

    def test_all_white_space(self):
        input = "   \n \t \r\n"
        len_input = len(input)
        ctx = LexContext(input, 0)

        result = lex_skip_whitespace(ctx)

        self.assertEqual(result.consumed_chars, len_input)
        self.assertEqual(result.token, None)

    def test_non_white_space(self):
        input = "Here_is_some_non_white_space"
        ctx = LexContext(input, 0)

        result = lex_skip_whitespace(ctx)

        self.assertEqual(result.consumed_chars, 0)
        self.assertEqual(result.token, None)

    def test_initial_white_space(self):
        input = "    Initial_White_Space"
        ctx = LexContext(input, 0)

        result = lex_skip_whitespace(ctx)

        self.assertEqual(result.consumed_chars, 4)
        self.assertEqual(result.token, None)

    def test_trailing_white_space(self):
        input = "Initial_White_Space    "
        ctx = LexContext(input, 0)

        result = lex_skip_whitespace(ctx)

        self.assertEqual(result.consumed_chars, 0)
        self.assertEqual(result.token, None)