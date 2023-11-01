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
    'loop', 'break', 'continue',

    # misc
    'scope',
    ]

# reserved words for possible future use
RESERVED_WORDS = [
    'class',
    'as',
    'private',
    'public',
    'pub',
    'export',
    'module',
    'mod',
    'namespace',
    'const',
    'with',
    'while',
    'do',
    'for',
    'in',
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