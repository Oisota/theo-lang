from unittest import TestCase

from app.lexer import Lexer

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
                lexer = Lexer(text)
                result = lexer.lex_skip_whitespace()
                self.assertEqual(result.consumed_chars, expected)
                self.assertEqual(result.token, None)