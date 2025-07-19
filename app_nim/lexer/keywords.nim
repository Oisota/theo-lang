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
    "class", "interface", "type", "struct", "enum", "union", "impl", "distinct",

    # logical
    "case",

    # loops
    "loop", "break", "continue",

    # scoping
    "scope", "static"
  ]

# Things we might want to use in the future, still deciding on these
  RESERVED_WORDS* = @[
    # module stuff
    "private", "public", "export", "module", "mod", "as",

    # variables
    "const",

    # loops 
    "while", "do", "for", "in",

    # logical 
    "if", "else",

    # misc
    "with", "prop",
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
    "=",

    # field access
    ".",

    # type annotation
    ":",
    ]
