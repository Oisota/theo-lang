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
    tree = program(tokens)
    return tree

def program(tokens):
    """Parse tokens into AST"""
    tree = ast.Program()
    tree = parse_import(tree, tokens)
    return tree

def parse_import(tree, tokens):
    """Parse import expression"""
    #if match(TokenType.KEYWORD, 'import')