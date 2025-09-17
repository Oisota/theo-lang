"""Parser Code

Parse the token stream into an AST
"""
from app.parser.ast import Import
from app.lexer.token import Token, TokenType

def match(expected_token, current_token):
    return (
        (expected_token.type == current_token.type) and
        (expected_token.value == current_token.value)
        )

def parse(tokens: list):
    """Parse tokens into AST"""
    tree = parse_program(tokens)
    return tree

def parse_program(tokens: list):
    """Parse tokens into AST"""
    tree = ast.Program()
    imports, consumed = parse_imports(tree, tokens)
    tree.imports = imports
    return tree

def parse_imports(current: int, tokens: list):
    """Parse import list"""
    imports = []
    consumed = 0
    current_token = tokens[current]
    if match(Token(TokenType.KEYWORD, 'import'), current_token):
        consumed += 1
        current_token = tokens[current + consumed]
        if match(Token(TokenType.PAREN_OPEN, '('), current_token):
            consumed += 1
            current_token = tokens[current + consumed]
            while current_token.type != TokenType.PAREN_CLOSE:
                # parse import path
                if current_token.type == TokenType.STRING:
                    imp = Import(current_token.value)
                    consumed += 1
                    current_token = tokens[current + consumed]

                if current_token.type in (TokenType.OPERATOR, TokenType.IDENTIFIER):
                    imp.qualifier = current_token.value
                    consumed += 1
                    current_token = tokens[current + consumed]

                imports.append(imp)

            consumed += 1

    return imports, consumed

def parse_import(current, tokens):
    """Parse a single import"""