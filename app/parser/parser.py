"""Parser Code

Parse the token stream into an AST
"""
from app.parser import ast
from app.lexer.token import TokenType

def match(expected_token_type, expected_token, current_token):
    type_match = expected_token_type == current_token.type
    value_match = expected_token == current_token.value
    return type_match and value_match

def parse(tokens):
    """Parse tokens into AST"""
    tree = parse_program(tokens)
    return tree

def parse_program(tokens):
    """Parse tokens into AST"""
    tree = ast.Program()
    import_tree = parse_imports(tree, tokens)
    tree.imports = import_tree
    return tree

def parse_imports(current, tokens):
    """Parse import list"""
    imports = []
    consumed = 0
    current_token = tokens[current]
    if match(TokenType.KEYWORD, 'import', current_token):
        consumed += 1
        current_token = tokens[current + consumed]
        if match(TokenType.PAREN_OPEN, '(', current_token):
            pass
            #while match(TokenType.)
            #= ast.Import()

def parse_import(current, tokens):
    """Parse a single import"""