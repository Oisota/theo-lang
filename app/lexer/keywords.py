"""Language keywords, operators, etc"""

KEYWORDS = [
    # imports
    'import', 'pub',

    # vars
    'let',

    # functions
    'fun', 'fn', 'done', 'recur',

    # types
    'class', 'interface', 'type', 'struct', 'enum', 'union', 'impl', 'distinct',

    # logical
    'case',

    # loops
    'loop', 'break', 'continue',

    # misc
    'scope', 'static',
    ]

# reserved words for possible future use
RESERVED_WORDS = [
    'as',
    'private',
    'public',
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

    # math
    '+', '-', '*', '/', '%',

    # bitwise
    '&', '|', '^', '<<', '>>', '~',

    # assignment
    '=',

    # field access
    '.',

    # type annotation
    ':',
    ]