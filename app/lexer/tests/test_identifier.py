from unittest import TestCase

from app.lexer.token import Token, TokenType, TokenizeResult, LexContext
from app.lexer.lex_funcs import lex_identifier

class TestLexIdentifier(TestCase):
    """Test lexing identifiers"""
    def test_lex_identifier(self):
        var_names = [
            ('foo', TokenizeResult(3, Token(TokenType.IDENTIFIER, 'foo'))),
            ('foo_bar', TokenizeResult(7, Token(TokenType.IDENTIFIER, 'foo_bar'))),
            ('foo_12', TokenizeResult(6, Token(TokenType.IDENTIFIER, 'foo_12'))),
            ('_foo', TokenizeResult(4, Token(TokenType.IDENTIFIER, '_foo'))),
            ('__foo__', TokenizeResult(7, Token(TokenType.IDENTIFIER, '__foo__'))),
            ('1__foo__', TokenizeResult(0, None)),
            ('foo?', TokenizeResult(3, Token(TokenType.IDENTIFIER, 'foo'))),
        ]
        for (var, expected) in var_names:
            with self.subTest(var=var):
                ctx = LexContext(var, 0)

                result = lex_identifier(ctx)

                self.assertEqual(result, expected)
                self.assertEqual(result.token, expected.token)