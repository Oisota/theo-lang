"""Language keywords, operators, etc"""

KEYWORDS = [
    # imports
    'import',

    # vars
    'let',

    # functions
    'fun', 'fn', 'end',

    # types
    'interface', 'type', 'struct', 'enum', 'union', 'impl', 'prop',

    # logical
    'if', 'else', 'case',

    # loops
    'while', 'for', 'break', 'continue',

    # misc
    'scope', 'with', # might not need 'with', could just use a built in function
    ]

# reserved words for possible future use
RESERVED_WORDS = [
    'class'
    'as',
    'private',
    'public',
    'pub',
    'export',
    'module',
    'mod',
    'namespace',
    'loop',
    ]

OPERATORS = [
    # logical
    'and', 'or', 'not', '==', '!=', '<=', '>=', '<', '>',

    # pattern match and lambda expressions
    '=>',

    # math assignment might not be needed, want mutation to have lots of ceremony
    # '+=', '-=', '*=', '/='

    # math
    '+', '-', '*', '/', '%',

    # bitwise
    '&', '|', '^', '<<', '>>', '~',

    # assignment
    '=',

    # field access
    '.',
    ]