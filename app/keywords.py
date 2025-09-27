"""Language keywords, operators, etc"""

KEYWORDS = [
    # imports
    'import', 'pub',

    # vars
    'let',

    # functions
    'fun', 'fn', 'done', 'recur',

    # types
    'class', 'interface', 'type', 'struct', 'enum', 'union', 'distinct',

    # OOP stuff
    'abstract', 'static', 'implements', 'prop',

    # logical
    'case',

    # loops
    'loop', 'break', 'continue',

    # misc
    'scope',
    ]

# reserved words for possible future use
RESERVED_WORDS = [
    'as',
    'private',
    'public',
    'export',
    'module',
    'mod',
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