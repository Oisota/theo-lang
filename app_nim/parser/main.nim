import lexer/token

type
  NodeType* = enum
    FUNC_DEF,
    LET_EXPR

  ParseTree = ref object
    node_type*: NodeType

func parse(tokens: seq[Token]): ParseTree =
