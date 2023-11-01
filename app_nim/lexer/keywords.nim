discard """Language keywords, operators, etc"""

let 
  KEYWORDS* = @[
    # imports
    "import",

    # vars
    "let",

    # functions
    "fun", "fn", "done",

    # types
    "interface", "type", "struct", "enum", "union", "impl", "prop",

    # logical
    "if", "else", "case",

    # loops
    "loop", "break", "continue",

    # misc
    "scope",
  ]

  RESERVED_WORDS* = @[
    "class",
    "as",
    "private",
    "public",
    "pub",
    "export",
    "module",
    "mod",
    "namespace",
    "const",
    "with",
    "while",
    "do",
    "for",
    "in",
  ]

  OPERATORS* = @[
    # logical
    "and", "or", "not", "==", "!=", "<=", ">=", "<", ">",

    # pattern match
    "=>",

    # math
    "+", "-", "*", "/", "%",

    # bitwise
    "&", "|", "^", "<<", ">>", "~",

    # assignment
    "=",

    # field access
    ".",
    ]