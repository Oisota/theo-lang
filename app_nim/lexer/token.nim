import std/options
import std/strformat

type
  TokenType* = enum
    PAREN_OPEN,
    PAREN_CLOSE,
    CURLY_OPEN,
    CURLY_CLOSE,
    SQUARE_OPEN,
    SQUARE_CLOSE,
    COLON,
    COMMA,
    KEYWORD,
    INTEGER,
    FLOAT,
    STRING,
    OPERATOR,
    IDENTIFIER,
    COMMENT,
    RESERVED

  Token* = ref object
    tok_type*: TokenType
    value*: string
    start_line*: int = 0
    end_line*: int = 0
    start_column*: int = 0
    end_column*: int = 0

  TokenizeResult* = object
    consumed_chars*: int
    token*: Option[Token]

  # context type for easily passing data around
  LexContext* = ref object
    data*: seq[char]
    idx*: int

proc has_next*(ctx: LexContext): bool =
  result = ctx.idx < len(ctx.data)
proc consume*(ctx: LexContext, n: int): void =
  ctx.idx = ctx.idx + n

proc current*(ctx: LexContext): char =
  return ctx.data[ctx.idx]

proc peek*(ctx: LexContext, offset: int): char =
  return ctx.data[ctx.idx + offset]

proc `$`*(t: Token): string =
  result = &"Token(type: {t.tok_type}, value: '{t.value}', lines: {t.start_line}-{t.end_line}, cols: {t.start_column}-{t.end_column})"