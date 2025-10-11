"""Language keywords, operators, etc"""

KEYWORDS = set([
    # imports
    'import',

    # vars
    'let',

    # functions
    'fun', 'fn', 'done', 'recur',

    # types
    'class', 'interface', 'type', 'enum', 'union', 'distinct',

    # OOP stuff
    'construct', 'abstract', 'static', 'prop',

    # logical
    'case',

    # loops
    'loop', 'break', 'continue',

    # misc
    'scope',
    ])

# reserved words for possible future use
RESERVED_WORDS = set([
    'as',
    'pub',
    'private',
    'public',
    'protected',
    'export',
    'module',
    'mod',
    'const',
    'with',
    'while',
    'do',
    'for',
    'in',
    'constructor',
    'init',
    'struct',
    ])

OPERATORS = set([
    # logical
    'and', 'or', 'not', '==', '!=', '<=', '>=', '<', '>',

    # pattern match
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
    ])