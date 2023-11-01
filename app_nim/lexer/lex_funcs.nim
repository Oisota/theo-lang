import std/options
import re

import token

func empty_result(): TokenizeResult =
  result = TokenizeResult(consumed_chars: 0, token: none(Token))

# generic lexing functions
func lex_char(
  tok_type: TokenType,
  value: char,
  ctx: LexContext
  ): TokenizeResult =

  result = empty_result()
  if value == ctx.current:
    let tok = Token(tok_type: tok_type, value: $value)
    result = TokenizeResult(consumed_chars: 1, token: some(tok))

func lex_keyword*(
  tok_type: TokenType,
  keyword: string,
  ctx: LexContext): TokenizeResult =

  var
    consumed_chars = 0

  while ((ctx.idx + consumed_chars) < len(ctx.data)) and consumed_chars < len(keyword) and keyword[consumed_chars] == ctx.char_at_offset(consumed_chars):
    consumed_chars += 1

  result = empty_result()
  if len(keyword) == consumed_chars:
    let tok = Token(tok_type: tok_type, value: keyword)
    result = TokenizeResult(consumed_chars: consumed_chars, token: some(tok))

func lex_line_comment*(ctx: LexContext): TokenizeResult =
  var
    consumed = 2
    value = ""
  result = empty_result()

  if ctx.current == '/' and ctx.char_at_offset(1) == '/':
    var c = ctx.char_at_offset(consumed)
    while c != '\n':
      value.add(c)
      consumed += 1
      c = ctx.char_at_offset(consumed)
    result = TokenizeResult(consumed_chars: consumed, token: none(Token))

func lex_multiline_comment*(ctx: LexContext): TokenizeResult =
  var 
    consumed = 2
    value = ""

  result = empty_result()

  if ctx.current == '/' and ctx.char_at_offset(1) == '*':
    var
      c = ctx.char_at_offset(consumed)
      next_char = ctx.char_at_offset(consumed + 1)
    while not (c == '*' and next_char == '/'):
      value.add(c)
      consumed += 1
      c = ctx.char_at_offset(consumed)
      next_char = ctx.char_at_offset(consumed + 1)
    consumed += 2
    result = TokenizeResult(consumed_chars: consumed, token: none(Token))

func lex_paren_open*(ctx: LexContext): TokenizeResult =
  return lex_char(TokenType.PAREN_OPEN, '(', ctx)

func lex_paren_close*(ctx: LexContext): TokenizeResult =
  return lex_char(TokenType.PAREN_CLOSE, ')', ctx)

func lex_curly_open*(ctx: LexContext): TokenizeResult =
  return lex_char(TokenType.CURLY_OPEN, '{', ctx)

func lex_curly_close*(ctx: LexContext): TokenizeResult =
  return lex_char(TokenType.CURLY_CLOSE, '}', ctx)

func lex_square_open*(ctx: LexContext): TokenizeResult =
  return lex_char(TokenType.SQUARE_OPEN, '[', ctx)

func lex_square_close*(ctx: LexContext): TokenizeResult =
  return lex_char(TokenType.SQUARE_CLOSE, ']', ctx)

func lex_colon*(ctx: LexContext): TokenizeResult =
  return lex_char(TokenType.COLON, ':', ctx)

func lex_comma*(ctx: LexContext): TokenizeResult =
  return lex_char(TokenType.COMMA, ',', ctx)

func lex_number*(ctx: LexContext): TokenizeResult =
  var
    pattern = re(r"[0-9]|(\.)|(_)")
    end_pattern = re(r"x|b|[A-F]|[a-f]|[0-9]|(\.)|(_)")
    consumed_chars = 0
    value = ""
    c = ctx.current

  result = empty_result()

  if contains($c, pattern):
    while ($c != "") and contains($c, end_pattern):
      consumed_chars += 1
      value.add(c)
      try:
        c = ctx.char_at_offset(consumed_chars)
      except IndexDefect:
        break
    
    value = value.replace(re("_"), "")
    var token_type = TokenType.INTEGER
    if contains(value, re(r"\.")):
      token_type = TokenType.FLOAT
    let token = Token(tok_type: token_type, value: value)
    result = TokenizeResult(consumed_chars: consumed_chars, token: some(token))


func lex_identifier*(ctx: LexContext): TokenizeResult =
  var
    pattern = re("([A-Z]|[a-z]|_|[0-9])+")
    initial_pattern = re("([A-Z]|[a-z]|_)+")
    consumed_chars = 0
    value = ""
    c = ctx.current

  result = empty_result()
  
  if contains($c, initial_pattern):
    while ($c != "") and contains($c, pattern):
      consumed_chars += 1
      value.add(c)
      try:
        c = ctx.char_at_offset(consumed_chars)
      except IndexDefect:
        break
    
    let tok = Token(tok_type: TokenType.IDENTIFIER, value: value)
    result = TokenizeResult(consumed_chars: consumed_chars, token: some(tok))

func lex_skip_whitespace*(ctx: LexContext): TokenizeResult =
  var
    pattern = re(r"\s")
    consumed = 0
    c = ' '

  try:
    c = ctx.char_at_offset(consumed)
  except IndexDefect:
    return TokenizeResult(consumed_chars: consumed, token: none(Token))

  while contains($c, pattern):
    consumed += 1
    try:
      c = ctx.char_at_offset(consumed)
    except IndexDefect:
      break
  
  return TokenizeResult(consumed_chars: consumed, token: none(Token))


func lex_string*(ctx: LexContext): TokenizeResult =
  var c = ctx.current
  result = empty_result()
  if c == '"' or c == '\'':
    var
      value = ""
      consumed = 1
      closing_quote = c
      c = ctx.char_at_offset(consumed)
    while c != closing_quote:
      value.add(c)
      consumed += 1
      c = ctx.char_at_offset(consumed)
    
    let token = some(Token(tok_type: TokenType.STRING, value: value))
    result = TokenizeResult(consumed_chars: consumed + 1, token: token)