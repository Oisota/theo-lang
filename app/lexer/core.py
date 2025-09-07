"""Core tokenize function"""

from .lex_funcs import (
    lex_skip_whitespace, 
    lex_line_comment,
    lex_multiline_comment,
    lex_paren_open,
    lex_paren_close,
    lex_curly_open,
    lex_curly_close,
    lex_square_open,
    lex_square_close,
    lex_colon,
    lex_comma,
    lex_keyword,
    lex_identifier,
    lex_number,
    lex_string,
    )
from .keywords import KEYWORDS, OPERATORS, RESERVED_WORDS
from .token import TokenType, LexContext

def build_keyword_lambda(type, keyword):
    return lambda ctx: lex_keyword(type, keyword, ctx)

def build_string_tokenizers(strings, type):
    tokenizers = []

    for s in strings:
        fn = build_keyword_lambda(type, s) # needed to properly capture variables in loop
        tokenizers.append(fn)

    return tokenizers

def tokenize(input):
    """Read file and parse contents into token array"""
    # TODO
    # - add newline token? (maybe needed to denote end of expression)
    tokenizers = [
        lex_skip_whitespace,
        lex_line_comment,
        lex_multiline_comment,
        lex_paren_open,
        lex_paren_close,
        lex_curly_open,
        lex_curly_close,
        lex_square_open,
        lex_square_close,
        lex_colon,
        lex_comma,
        *build_string_tokenizers(RESERVED_WORDS, TokenType.RESERVED),
        *build_string_tokenizers(KEYWORDS, TokenType.KEYWORD),
        *build_string_tokenizers(OPERATORS, TokenType.OPERATOR),
        lex_identifier,
        lex_number,
        lex_string,
    ]

    ctx = LexContext(input, 0)
    #current = 0
    len_input = len(input)
    current_line = 1
    current_column = 1
    while ctx.index < len_input:
        tokenized = False
        for lex_function in tokenizers:
            token = None
            if tokenized:
                break

            result = lex_function(ctx)
            consumed_chars = result.consumed_chars
            token = result.token
            if token:
                token.start_line = current_line
                token.start_column = current_column

            #calculate consumed lines/columns
            for i in range(ctx.index, ctx.index + consumed_chars):
                current_column += 1
                if input[i] == '\n':
                    current_line += 1
                    current_column = 1

            if consumed_chars:
                ctx.index += consumed_chars
                #current += consumed_chars
                tokenized = True


            if token:
                token.end_line = current_line
                token.end_column = current_column - 1
                print(token)
                yield token

        if not tokenized:
            raise Exception('Character not recognized: {}'.format(ctx.current))