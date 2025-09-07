from unittest import TestCase

from app.lexer.lex_funcs import lex_skip_whitespace
from app.lexer.token import LexContext

class TestLexWhiteSpace(TestCase):

    def test_all_white_space(self):
        tests = [
            ("   \n \t \r\n", 9),
            ("Here_is_some_non_white_space", 0),
            ("    Initial_White_Space", 4),
            ("Trailing_White_Space    ", 0),
        ]

        for text, expected in tests:
            with self.subTest(text=text):
                ctx = LexContext(text, 0)
                result = lex_skip_whitespace(ctx)
                self.assertEqual(result.consumed_chars, expected)
                self.assertEqual(result.token, None)