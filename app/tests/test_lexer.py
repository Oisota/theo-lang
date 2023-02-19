from unittest import TestCase

from ..lexer import lex_skip_whitespace

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