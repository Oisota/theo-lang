"""Lexer class"""

import re

from .processor import Processor
from .token import TokenType, Token, TokenizeResult 
from .keywords import RESERVED_WORDS, KEYWORDS, OPERATORS


class Lexer(Processor):

    def char_at_offset(self, offset: int):
        return self.data[self.index + offset]

    def lex(self):
        """Read file and parse contents into token array"""
        # TODO
        # - add newline token? (maybe needed to denote end of expression)
        tokenizers = [
            self.lex_skip_whitespace,
            self.lex_line_comment,
            self.lex_multiline_comment,
            self.create_char_lexer(TokenType.PAREN_OPEN, '('),
            self.create_char_lexer(TokenType.PAREN_CLOSE, ')'),
            self.create_char_lexer(TokenType.CURLY_OPEN, '{'),
            self.create_char_lexer(TokenType.CURLY_CLOSE, '}'),
            self.create_char_lexer(TokenType.SQUARE_OPEN, '['),
            self.create_char_lexer(TokenType.SQUARE_CLOSE, ']'),
            self.create_char_lexer(TokenType.COLON, ':'),
            self.create_char_lexer(TokenType.COMMA, ','),
            *self.build_string_tokenizers(RESERVED_WORDS, TokenType.RESERVED),
            *self.build_string_tokenizers(KEYWORDS, TokenType.KEYWORD),
            *self.build_string_tokenizers(OPERATORS, TokenType.OPERATOR),
            self.lex_identifier,
            self.lex_number,
            self.lex_string,
        ]

        len_input = len(self.data)
        current_line = 1
        current_column = 1
        while self.index < len_input:
            tokenized = False
            for lex_function in tokenizers:
                token = None
                if tokenized:
                    break

                result = lex_function()
                consumed_chars = result.consumed_chars
                token = result.token
                if token:
                    token.start_line = current_line
                    token.start_column = current_column

                #calculate consumed lines/columns
                for i in range(self.index, self.index + consumed_chars):
                    current_column += 1
                    if self.data[i] == '\n':
                        current_line += 1
                        current_column = 1

                if consumed_chars:
                    self.index += consumed_chars
                    #current += consumed_chars
                    tokenized = True

                if token:
                    token.end_line = current_line
                    token.end_column = current_column - 1
                    print(token)
                    yield token

            if not tokenized:
                raise Exception('Character not recognized: {}'.format(self.current))


    # generic lexing functions
    def lex_char(self, type, value) -> TokenizeResult:
        """Generic function for lexing a single character"""
        if value == self.current:
            return TokenizeResult(1, Token(type, value))
        return TokenizeResult(0, None)

    def lex_keyword(self, type, keyword) -> TokenizeResult:
        """Generic function for lexing a keyword"""
        consumed_chars = 0
        while (
            self.index + consumed_chars < len(self.data) and
            consumed_chars < len(keyword) and
            keyword[consumed_chars] == self.char_at_offset(consumed_chars)
        ):
            consumed_chars += 1

        if len(keyword) == consumed_chars:
            return TokenizeResult(consumed_chars, Token(type, keyword))
        return TokenizeResult(0, None)

    def lex_line_comment(self) -> TokenizeResult:
        """Lex a single line comment"""
        consumed = 2
        value = ''
        if self.current == '/' and self.char_at_offset(1) == '/':
            char = self.char_at_offset(consumed)
            while char != '\n':
                value += char
                consumed += 1
                char = self.char_at_offset(consumed)
            return TokenizeResult(consumed, None) # currently just ignoring comments
        return TokenizeResult(0, None)

    def lex_multiline_comment(self) -> TokenizeResult:
        """Lex a multiline comment"""
        consumed = 2
        value = ''
        if self.current == '/' and self.char_at_offset(1) == '*':
            char = self.char_at_offset(consumed)
            next_char = self.char_at_offset(consumed + 1)
            while not (char == '*' and next_char == '/'):
                value += char
                consumed += 1
                char = self.char_at_offset(consumed)
                next_char = self.char_at_offset(consumed + 1)
            consumed += 2
            return TokenizeResult(consumed, None) # currently just ignoring comments
        return TokenizeResult(0, None)

    def lex_number(self) -> TokenizeResult:
        pattern = re.compile('[0-9]|(\.)|(_)')
        end_pattern = re.compile('x|b|[A-F]|[a-f]|[0-9]|(\.)|(_)')
        #return lex_pattern(TokenType.NUMBER, pattern, input, current)
        consumed_chars = 0
        value = ''
        char = self.current
        if pattern.match(char):
            while char and end_pattern.match(char):
                consumed_chars += 1
                value += char
                try:
                    char = self.char_at_offset(consumed_chars)
                except IndexError:
                    break

            value = value.replace('_', '')
            # check if int or float literal
            token_type = TokenType.INTEGER
            if '.' in value:
                token_type = TokenType.FLOAT
            return TokenizeResult(consumed_chars, Token(token_type, value))
        return TokenizeResult(0, None)

    def lex_identifier(self) -> TokenizeResult:
        pattern = re.compile('([A-Z]|[a-z]|_|[0-9])+')
        initial_pattern = re.compile('([A-Z]|[a-z]|_)+')
        consumed_chars = 0
        value = ''
        char = self.current
        if initial_pattern.match(char):
            while char and pattern.match(char):
                consumed_chars += 1
                value += char
                try:
                    char = self.char_at_offset(consumed_chars)
                except IndexError:
                    break

            return TokenizeResult(consumed_chars, Token(TokenType.IDENTIFIER, value))
        return TokenizeResult(0, None)

    def lex_skip_whitespace(self) -> TokenizeResult:
        # NOTE this func and a few others may be the only ones that need to
        # count new lines, since only certain tokens may span a newline
        pattern = re.compile('\s')
        consumed = 0
        try:
            char = self.char_at_offset(consumed)
        except IndexError:
            return TokenizeResult(consumed, None)
        while pattern.match(char):
            consumed += 1
            try:
                char = self.char_at_offset(consumed)
            except IndexError:
                break
        return TokenizeResult(consumed, None)

    def lex_string(self) -> TokenizeResult:
        char = self.current
        if char == '"' or char == "'":
            value = ''
            consumed = 1
            closing_quote = char
            char = self.char_at_offset(consumed)
            while char != closing_quote:
                if char is None:
                    raise Exception('unterminated string')
                value += char
                consumed += 1
                char = self.char_at_offset(consumed)

            return TokenizeResult(consumed + 1, Token(TokenType.STRING, value))
        return TokenizeResult(0, None)

    def build_keyword_lambda(self, type, keyword):
        return lambda: self.lex_keyword(type, keyword)

    def build_string_tokenizers(self, strings, type):
        tokenizers = []

        for s in strings:
            fn = self.build_keyword_lambda(type, s) # needed to properly capture variables in loop
            tokenizers.append(fn)

        return tokenizers

    def create_char_lexer(self, tok_type, char):
        return lambda: self.lex_char(tok_type, char)
