import options
import std/strformat

import keywords
import lex_funcs
import token

type
  tokenize_func = proc (ctx: LexContext): TokenizeResult

func build_keyword_lambda(tok_type: TokenType, keyword: string): tokenize_func =
  return proc (ctx: LexContext): TokenizeResult = lex_keyword(tok_type, keyword, ctx) 

func build_string_tokenizers(strings: seq[string], tok_type: TokenType): seq[tokenize_func] =
  result = @[]
  for s in strings:
    let fn = build_keyword_lambda(tok_type, s)
    result.add(fn)

iterator tokenize*(input: seq[char]): Token {. closure .} =
  var
    tokenizers: seq[tokenize_func] = @[]
    ctx = LexContext(data: input, idx: 0)
    current_line = 1
    current_column = 1
    tokenized = false
    token = none(Token)

  tokenizers.add(lex_skip_whitespace)
  tokenizers.add(lex_line_comment)
  tokenizers.add(lex_multiline_comment)
  tokenizers.add(lex_paren_open)
  tokenizers.add(lex_paren_close)
  tokenizers.add(lex_curly_open)
  tokenizers.add(lex_curly_close)
  tokenizers.add(lex_square_open)
  tokenizers.add(lex_square_close)
  tokenizers.add(lex_colon)
  tokenizers.add(lex_comma)
  tokenizers.add(build_string_tokenizers(KEYWORDS, TokenType.KEYWORD))
  tokenizers.add(build_string_tokenizers(OPERATORS, TokenType.OPERATOR))
  tokenizers.add(lex_identifier)
  tokenizers.add(lex_number)
  tokenizers.add(lex_string)
  tokenizers.add(build_string_tokenizers(RESERVED_WORDS, TokenType.RESERVED))

  while ctx.has_next():
    tokenized = false
    for lex_function in tokenizers:
      token = none(Token)
      if tokenized:
        break

      var
        res = lex_function(ctx)
        consumed_chars = res.consumed_chars
        token = res.token

      if token.isSome():
        var t = token.get() # NOTE see comment below
        t.start_line = current_line
        t.start_column = current_column

      # calculate consumed lines/columns
      for i in (ctx.idx)..<(ctx.idx + consumed_chars):
        current_column += 1
        if input[i] == '\n':
          current_line += 1
          current_column = 1

      if consumed_chars > 0:
        ctx.consume(consumed_chars)
        tokenized = true

      if token.isSome():
        var t = token.get()
        t.end_line = current_line
        t.end_column = current_column - 1
        yield t

    if not tokenized:
      raise newException(Exception, &"Character not recognized: {ctx.current}")
      