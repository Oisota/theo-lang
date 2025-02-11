discard """Language keywords, operators, etc"""

let 
  KEYWORDS* = @[
    # module stuff
    "import",
    "pub",

    # vars
    "let",

    # functions
    "fun", "fn", "done", "recur",

    # types
    "interface", "type", "struct", "enum", "union", "impl", "distinct",

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
    "prop",
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

    # assignment/mutation
    "=", ":=",

    # field access
    ".",

    # type annotation
    ":",
    ]
